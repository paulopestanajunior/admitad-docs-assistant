"""
Ingestão de documentos no vector store.
Processa arquivos da pasta docs/, gera embeddings e salva no ChromaDB.
"""

import os
import re
import hashlib
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


DOCS_DIR = "docs"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "documentation"

# Modelo de embeddings multilíngue — bom pra PT e EN
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"

# Configurações de chunking
CHUNK_SIZE = 500         # caracteres por chunk
CHUNK_OVERLAP = 100      # overlap entre chunks
MIN_CHUNK_SIZE = 50      # chunks menores que isso são descartados

# Contador global pra garantir IDs únicos
_chunk_counter = 0


def _next_chunk_id(text: str, metadata: dict) -> str:
    """Gera um ID único para cada chunk usando contador global + hash."""
    global _chunk_counter
    _chunk_counter += 1
    unique_str = f"{metadata.get('filename', '')}-{_chunk_counter}-{text[:50]}"
    return hashlib.md5(unique_str.encode()).hexdigest()[:12]


def load_documents(docs_dir: str) -> list[dict]:
    """Carrega todos os documentos da pasta docs/."""
    documents = []
    supported_extensions = {".md", ".txt", ".html"}
    
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"Pasta '{docs_dir}' não encontrada. Crie a pasta e adicione seus documentos.")
        return []
    
    for filepath in sorted(docs_path.rglob("*")):
        if filepath.suffix.lower() not in supported_extensions:
            continue
        
        try:
            content = filepath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content = filepath.read_text(encoding="latin-1")
            except Exception as e:
                print(f"Erro ao ler {filepath}: {e}")
                continue
        
        if len(content.strip()) < MIN_CHUNK_SIZE:
            continue
        
        # Extrai metadados do frontmatter (se houver)
        metadata = extract_frontmatter(content)
        metadata["filename"] = filepath.name
        metadata["filepath"] = str(filepath)
        
        # Remove frontmatter do conteúdo
        content = remove_frontmatter(content)
        
        documents.append({
            "content": content,
            "metadata": metadata
        })
    
    print(f"Carregados {len(documents)} documentos")
    return documents


def extract_frontmatter(content: str) -> dict:
    """Extrai metadados do frontmatter YAML (---) se existir."""
    metadata = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        for line in match.group(1).split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
    return metadata


def remove_frontmatter(content: str) -> str:
    """Remove frontmatter do conteúdo."""
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)


def chunk_by_sections(content: str, metadata: dict) -> list[dict]:
    """
    Divide o conteúdo em chunks inteligentes.
    Tenta dividir por seções (headers markdown) primeiro,
    depois por parágrafos, e finalmente por tamanho.
    """
    chunks = []
    
    # Tenta dividir por headers markdown (## ou ###)
    sections = re.split(r'\n(?=#{1,3}\s)', content)
    
    for section in sections:
        section = section.strip()
        if len(section) < MIN_CHUNK_SIZE:
            continue
        
        # Extrai o título da seção (se for um header)
        section_title = ""
        title_match = re.match(r'^(#{1,3})\s+(.+?)$', section, re.MULTILINE)
        if title_match:
            section_title = title_match.group(2).strip()
        
        # Se a seção é pequena o suficiente, usa inteira
        if len(section) <= CHUNK_SIZE:
            chunks.append({
                "id": _next_chunk_id(section, metadata),
                "text": section,
                "metadata": {
                    **metadata,
                    "section": section_title,
                    "chunk_type": "section"
                }
            })
        else:
            # Divide seções grandes por parágrafos
            paragraphs = section.split("\n\n")
            current_chunk = ""
            
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                
                if len(current_chunk) + len(para) <= CHUNK_SIZE:
                    current_chunk += "\n\n" + para if current_chunk else para
                else:
                    if len(current_chunk) >= MIN_CHUNK_SIZE:
                        chunks.append({
                            "id": _next_chunk_id(current_chunk, metadata),
                            "text": current_chunk,
                            "metadata": {
                                **metadata,
                                "section": section_title,
                                "chunk_type": "paragraph"
                            }
                        })
                    current_chunk = para
            
            # Último chunk da seção
            if len(current_chunk) >= MIN_CHUNK_SIZE:
                chunks.append({
                    "id": _next_chunk_id(current_chunk, metadata),
                    "text": current_chunk,
                    "metadata": {
                        **metadata,
                        "section": section_title,
                        "chunk_type": "paragraph"
                    }
                })
    
    return chunks


def create_embeddings(chunks: list[dict], model: SentenceTransformer) -> list[list[float]]:
    """Gera embeddings para os chunks usando o modelo multilíngue."""
    # Para o modelo e5, prefixar com "passage: " para documentos
    texts = [f"passage: {chunk['text']}" for chunk in chunks]
    
    print(f"Gerando embeddings para {len(texts)} chunks...")
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=16,
        normalize_embeddings=True
    )
    
    return embeddings.tolist()


def store_in_chroma(chunks: list[dict], embeddings: list[list[float]], chroma_dir: str):
    """Salva chunks e embeddings no ChromaDB."""
    client = chromadb.PersistentClient(path=chroma_dir)
    
    # Deleta collection existente (se houver) para recriar
    try:
        client.delete_collection(COLLECTION_NAME)
        print("Collection anterior removida")
    except Exception:
        pass
    
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    
    # ChromaDB tem limite de batch, então divide em lotes
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size]
        
        collection.add(
            ids=[c["id"] for c in batch_chunks],
            documents=[c["text"] for c in batch_chunks],
            embeddings=batch_embeddings,
            metadatas=[c["metadata"] for c in batch_chunks]
        )
    
    print(f"Salvos {len(chunks)} chunks no ChromaDB em '{chroma_dir}/'")


def main():
    # 1. Carrega documentos
    documents = load_documents(DOCS_DIR)
    if not documents:
        print(f"\nNenhum documento encontrado em '{DOCS_DIR}/'.")
        print("Adicione seus arquivos .md, .txt ou .html lá, ou rode 'python scraper.py' primeiro.")
        return
    
    # 2. Divide em chunks
    all_chunks = []
    for doc in documents:
        chunks = chunk_by_sections(doc["content"], doc["metadata"])
        all_chunks.extend(chunks)
    
    print(f"Total de chunks: {len(all_chunks)}")
    
    if not all_chunks:
        print("Nenhum chunk gerado. Verifique se os documentos têm conteúdo suficiente.")
        return
    
    # 3. Carrega modelo de embeddings
    print(f"\nCarregando modelo de embeddings: {EMBEDDING_MODEL}")
    print("(Na primeira execução, vai baixar ~1.2GB)")
    model = SentenceTransformer(EMBEDDING_MODEL)
    
    # 4. Gera embeddings
    embeddings = create_embeddings(all_chunks, model)
    
    # 5. Salva no ChromaDB
    store_in_chroma(all_chunks, embeddings, CHROMA_DIR)
    
    print("\nIngestão concluída com sucesso!")
    print(f"  Documentos: {len(documents)}")
    print(f"  Chunks: {len(all_chunks)}")
    print(f"  Vector store: {CHROMA_DIR}/")


if __name__ == "__main__":
    main()