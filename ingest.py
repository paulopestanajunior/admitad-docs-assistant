"""
Ingestão de documentos no vector store.
Processa arquivos da pasta docs/, gera embeddings e salva no ChromaDB.

Uso:
    python ingest.py                        # usa modelo padrão (multilingual-e5-large)
    python ingest.py --model e5-large       # multilingual-e5-large (padrão)
    python ingest.py --model e5-instruct    # multilingual-e5-large-instruct
    python ingest.py --model bge-m3         # BAAI/bge-m3 (estado da arte)
"""

import os
import re
import sys
import hashlib
import argparse
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


DOCS_DIR = "docs"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "documentation"

# Configurações de chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MIN_CHUNK_SIZE = 50

# ── Modelos disponíveis ────────────────────────────────────────
MODELS = {
    "e5-large": {
        "name": "intfloat/multilingual-e5-large",
        "description": "Multilingual E5 Large — atual, boa qualidade EN+RU (~2.2GB)",
        "query_prefix": "query: ",
        "passage_prefix": "passage: ",
        "use_title_prefix": True,
    },
    "e5-instruct": {
        "name": "intfloat/multilingual-e5-large-instruct",
        "description": "Multilingual E5 Large Instruct — versão mais recente, melhor retrieval (~2.2GB)",
        "query_prefix": "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: ",
        "passage_prefix": "",
        "use_title_prefix": True,
    },
    "bge-m3": {
        "name": "BAAI/bge-m3",
        "description": "BGE-M3 — estado da arte em multilingual retrieval (~2.3GB)",
        "query_prefix": "",
        "passage_prefix": "",
        "use_title_prefix": True,
    },
}

DEFAULT_MODEL = "e5-large"

# Contador global pra garantir IDs únicos
_chunk_counter = 0


def _next_chunk_id(text: str, metadata: dict) -> str:
    global _chunk_counter
    _chunk_counter += 1
    unique_str = f"{metadata.get('filename', '')}-{_chunk_counter}-{text[:50]}"
    return hashlib.md5(unique_str.encode()).hexdigest()[:12]


def load_documents(docs_dir: str) -> list[dict]:
    documents = []
    supported_extensions = {".md", ".txt", ".html"}

    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"Pasta '{docs_dir}' não encontrada.")
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

        metadata = extract_frontmatter(content)
        metadata["filename"] = filepath.name
        metadata["filepath"] = str(filepath)

        content = remove_frontmatter(content)

        documents.append({"content": content, "metadata": metadata})

    print(f"Carregados {len(documents)} documentos")
    return documents


def extract_frontmatter(content: str) -> dict:
    metadata = {}
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        for line in match.group(1).split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
    return metadata


def remove_frontmatter(content: str) -> str:
    return re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)


def chunk_by_sections(content: str, metadata: dict) -> list[dict]:
    chunks = []
    sections = re.split(r'\n(?=#{1,3}\s)', content)

    for section in sections:
        section = section.strip()
        if len(section) < MIN_CHUNK_SIZE:
            continue

        section_title = ""
        title_match = re.match(r'^(#{1,3})\s+(.+?)$', section, re.MULTILINE)
        if title_match:
            section_title = title_match.group(2).strip()

        if len(section) <= CHUNK_SIZE:
            chunks.append({
                "id": _next_chunk_id(section, metadata),
                "text": section,
                "metadata": {**metadata, "section": section_title, "chunk_type": "section"}
            })
        else:
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
                            "metadata": {**metadata, "section": section_title, "chunk_type": "paragraph"}
                        })
                    current_chunk = para

            if len(current_chunk) >= MIN_CHUNK_SIZE:
                chunks.append({
                    "id": _next_chunk_id(current_chunk, metadata),
                    "text": current_chunk,
                    "metadata": {**metadata, "section": section_title, "chunk_type": "paragraph"}
                })

    return chunks


def build_passage_text(chunk: dict, model_config: dict) -> str:
    """Monta o texto do passage com prefixo e título conforme o modelo."""
    title = chunk["metadata"].get("title", chunk["metadata"].get("filename", ""))
    text = chunk["text"]

    # Adiciona título como contexto para ajudar o embedding a entender a origem
    if model_config["use_title_prefix"] and title:
        enriched = f"[{title}] {text}"
    else:
        enriched = text

    prefix = model_config["passage_prefix"]
    return f"{prefix}{enriched}" if prefix else enriched


def create_embeddings(chunks: list[dict], model: SentenceTransformer, model_config: dict) -> list[list[float]]:
    texts = [build_passage_text(chunk, model_config) for chunk in chunks]

    print(f"Gerando embeddings para {len(texts)} chunks...")
    print(f"  Exemplo de passage: {texts[0][:120]}...")

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=16,
        normalize_embeddings=True
    )

    return embeddings.tolist()


def store_in_chroma(chunks: list[dict], embeddings: list[list[float]], chroma_dir: str, model_key: str):
    client = chromadb.PersistentClient(path=chroma_dir)

    try:
        client.delete_collection(COLLECTION_NAME)
        print("Collection anterior removida")
    except Exception:
        pass

    # Salva qual modelo foi usado como metadata da collection
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={
            "hnsw:space": "cosine",
            "embedding_model": model_key,
        }
    )

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
    print(f"Modelo registrado na collection: {model_key}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Ingestão de documentos no ChromaDB com seleção de modelo de embedding."
    )
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()),
        default=DEFAULT_MODEL,
        help=(
            "Modelo de embedding a usar:\n"
            "  e5-large     — intfloat/multilingual-e5-large (padrão)\n"
            "  e5-instruct  — intfloat/multilingual-e5-large-instruct\n"
            "  bge-m3       — BAAI/bge-m3 (estado da arte)\n"
        )
    )
    return parser.parse_args()


def main():
    args = parse_args()
    model_key = args.model
    model_config = MODELS[model_key]

    print(f"\n{'='*60}")
    print(f"Modelo selecionado: {model_key}")
    print(f"  {model_config['description']}")
    print(f"  HuggingFace: {model_config['name']}")
    print(f"{'='*60}\n")

    # 1. Carrega documentos
    documents = load_documents(DOCS_DIR)
    if not documents:
        print(f"Nenhum documento encontrado em '{DOCS_DIR}/'.")
        print("Adicione seus arquivos .md, .txt ou .html, ou rode 'python scraper.py' primeiro.")
        return

    # 2. Divide em chunks
    all_chunks = []
    for doc in documents:
        chunks = chunk_by_sections(doc["content"], doc["metadata"])
        all_chunks.extend(chunks)

    print(f"Total de chunks: {len(all_chunks)}")

    if not all_chunks:
        print("Nenhum chunk gerado.")
        return

    # 3. Carrega modelo
    print(f"\nCarregando modelo: {model_config['name']}")
    print("(Na primeira execução, vai baixar o modelo)")
    model = SentenceTransformer(model_config["name"])

    # 4. Gera embeddings
    embeddings = create_embeddings(all_chunks, model, model_config)

    # 5. Salva no ChromaDB
    store_in_chroma(all_chunks, embeddings, CHROMA_DIR, model_key)

    # 6. Salva qual modelo foi usado num arquivo de config
    config_path = os.path.join(CHROMA_DIR, "embedding_model.txt")
    with open(config_path, "w") as f:
        f.write(f"{model_key}\n{model_config['name']}\n")
    print(f"Config salva em: {config_path}")

    print("\nIngestão concluída!")
    print(f"  Documentos : {len(documents)}")
    print(f"  Chunks     : {len(all_chunks)}")
    print(f"  Modelo     : {model_config['name']}")
    print(f"  Vector store: {CHROMA_DIR}/")
    print(f"\nIMPORTANTE: Atualize EMBEDDING_MODEL no api.py para '{model_config['name']}'")
    print(f"  e QUERY_PREFIX para '{model_config['query_prefix'][:50]}'")


if __name__ == "__main__":
    main()