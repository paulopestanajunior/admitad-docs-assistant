"""
FastAPI Backend with intelligent routing and multi-provider LLM:
- /ask       → Unified endpoint (classifier decides the route)
- /search    → Pure semantic search (no LLM)
- /chat      → RAG chat (search + generation via LLM)
- /providers → List and switch available providers
"""

import os
from contextlib import asynccontextmanager

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, CrossEncoder

from llm_providers import ProviderRegistry, discover_providers


load_dotenv()

# ── Configuration ──────────────────────────────────────────────
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "documentation"
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"
RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

TOP_K_RETRIEVAL = 10
TOP_K_RERANK = 5
TOP_K_SEARCH = 5

# ── Global models (loaded once at startup) ─────────────────────
embedder: SentenceTransformer = None
reranker: CrossEncoder = None
chroma_collection = None
registry: ProviderRegistry = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load models and connections at startup."""
    global embedder, reranker, chroma_collection, registry

    print("Loading models...")

    embedder = SentenceTransformer(EMBEDDING_MODEL)
    print(f"  ✓ Embeddings: {EMBEDDING_MODEL}")

    reranker = CrossEncoder(RERANKER_MODEL)
    print(f"  ✓ Reranker: {RERANKER_MODEL}")

    if not os.path.exists(CHROMA_DIR):
        raise RuntimeError(
            f"Vector store not found at '{CHROMA_DIR}/'. "
            "Run 'python ingest.py' first."
        )

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection = client.get_collection(COLLECTION_NAME)
    doc_count = chroma_collection.count()
    print(f"  ✓ ChromaDB: {doc_count} chunks loaded")

    print("Detecting LLM providers...")
    registry = discover_providers()

    print("Ready!\n")
    yield


app = FastAPI(
    title="RAG Chat API",
    description="Semantic search + RAG Chat — Multi-provider LLM",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Schemas ────────────────────────────────────────────────────

class SearchRequest(BaseModel):
    query: str
    top_k: int = TOP_K_SEARCH


class ChatRequest(BaseModel):
    query: str
    history: list[dict] = []
    provider: str | None = None
    api_key: str | None = None


class SearchResult(BaseModel):
    text: str
    filename: str
    section: str
    source_url: str
    relevance_score: float


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
    total_chunks_searched: int


class ChatResponse(BaseModel):
    query: str
    answer: str
    sources: list[SearchResult]
    provider_used: str
    model_used: str


class AskRequest(BaseModel):
    query: str
    history: list[dict] = []
    provider: str | None = None
    api_key: str | None = None
    mode: str = "auto_smart"  # "search_only", "auto_smart", "auto_llm", "always_chat"


class AskResponse(BaseModel):
    query: str
    mode: str
    reason: str
    answer: str | None = None
    results: list[SearchResult] = []
    total_chunks_searched: int = 0
    provider_used: str | None = None
    model_used: str | None = None


class SwitchProviderRequest(BaseModel):
    provider: str


# ── Helper: resolve LLM from request ──────────────────────────

def resolve_llm(provider: str | None = None, api_key: str | None = None):
    """
    Resolve which LLM to use:
    1. If user provides an api_key, create a temporary provider on the fly
    2. Otherwise use the server-side registry
    """
    # User-provided key takes priority
    if api_key and api_key.strip():
        return _create_provider_from_key(api_key.strip(), provider)

    # Fall back to server-configured providers
    if registry:
        return registry.get(provider)

    return None


def _create_provider_from_key(api_key: str, provider_hint: str | None = None):
    """Create a temporary LLM provider from a user-supplied API key."""
    # Auto-detect provider from key prefix
    if provider_hint:
        provider_name = provider_hint
    elif api_key.startswith("gsk_"):
        provider_name = "groq"
    elif api_key.startswith("sk-ant-"):
        provider_name = "anthropic"
    elif api_key.startswith("sk-"):
        provider_name = "openai"
    elif api_key.startswith("AI"):
        provider_name = "google"
    else:
        provider_name = "groq"  # default

    try:
        if provider_name == "groq":
            from groq import Groq
            client = Groq(api_key=api_key)
            return _OpenAICompatibleProvider(
                client=client,
                name="groq",
                model="llama-3.3-70b-versatile"
            )
        elif provider_name == "openai":
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            return _OpenAICompatibleProvider(
                client=client,
                name="openai",
                model="gpt-4o-mini"
            )
        elif provider_name == "anthropic":
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            return _AnthropicProvider(client=client)
        elif provider_name == "google":
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            return _GoogleProvider(genai=genai)
    except ImportError:
        print(f"Provider '{provider_name}' SDK not installed")
        return None
    except Exception as e:
        print(f"Error creating provider '{provider_name}': {e}")
        return None


class _LLMResponse:
    """Standardized LLM response."""
    def __init__(self, text: str, provider: str, model: str):
        self.text = text
        self.provider = provider
        self.model = model


class _OpenAICompatibleProvider:
    """Works for Groq and OpenAI (same API)."""
    def __init__(self, client, name: str, model: str):
        self.client = client
        self.name = name
        self.model = model

    def classify(self, system_prompt: str, query: str) -> str:
        r = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0,
            max_tokens=10,
        )
        return r.choices[0].message.content

    def complete(self, messages: list[dict], temperature=0.1, max_tokens=1024) -> _LLMResponse:
        r = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return _LLMResponse(
            text=r.choices[0].message.content,
            provider=self.name,
            model=self.model
        )


class _AnthropicProvider:
    """Anthropic provider."""
    def __init__(self, client, model="claude-sonnet-4-20250514"):
        self.client = client
        self.name = "anthropic"
        self.model = model

    def classify(self, system_prompt: str, query: str) -> str:
        r = self.client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=[{"role": "user", "content": query}],
            temperature=0,
            max_tokens=10,
        )
        return r.content[0].text

    def complete(self, messages: list[dict], temperature=0.1, max_tokens=1024) -> _LLMResponse:
        system = ""
        chat_msgs = []
        for msg in messages:
            if msg["role"] == "system":
                system += msg["content"] + "\n"
            else:
                chat_msgs.append(msg)

        kwargs = {
            "model": self.model,
            "messages": chat_msgs,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if system.strip():
            kwargs["system"] = system.strip()

        r = self.client.messages.create(**kwargs)
        return _LLMResponse(
            text=r.content[0].text,
            provider=self.name,
            model=self.model
        )


class _GoogleProvider:
    """Google Gemini provider."""
    def __init__(self, genai, model="gemini-1.5-flash"):
        self.genai = genai
        self.name = "google"
        self.model_name = model

    @property
    def model(self):
        return self.model_name

    def classify(self, system_prompt: str, query: str) -> str:
        model = self.genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system_prompt,
        )
        r = model.generate_content(query)
        return r.text

    def complete(self, messages: list[dict], temperature=0.1, max_tokens=1024) -> _LLMResponse:
        system = ""
        history = []
        for msg in messages:
            if msg["role"] == "system":
                system += msg["content"] + "\n"
            elif msg["role"] == "user":
                history.append({"role": "user", "parts": [msg["content"]]})
            elif msg["role"] == "assistant":
                history.append({"role": "model", "parts": [msg["content"]]})

        model = self.genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system.strip() if system.strip() else None,
            generation_config=self.genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
        )

        if len(history) == 1:
            r = model.generate_content(history[0]["parts"][0])
        else:
            chat = model.start_chat(history=history[:-1])
            r = chat.send_message(history[-1]["parts"][0])

        return _LLMResponse(
            text=r.text,
            provider=self.name,
            model=self.model_name
        )


# ── Helper functions ───────────────────────────────────────────

def retrieve_chunks(query: str, top_k: int = TOP_K_RETRIEVAL) -> list[dict]:
    """Retrieve similar chunks from ChromaDB using embeddings."""
    query_embedding = embedder.encode(
        f"query: {query}",
        normalize_embeddings=True
    ).tolist()

    results = chroma_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    chunks = []
    for i in range(len(results["ids"][0])):
        chunks.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return chunks


def rerank_chunks(query: str, chunks: list[dict], top_k: int = TOP_K_RERANK) -> list[dict]:
    """Rerank chunks using cross-encoder for better precision."""
    if not chunks:
        return []

    pairs = [(query, chunk["text"]) for chunk in chunks]
    scores = reranker.predict(pairs)

    for chunk, score in zip(chunks, scores):
        chunk["rerank_score"] = float(score)

    # Apply metadata relevance adjustment
    chunks = _adjust_scores_by_metadata(query, chunks)

    chunks.sort(key=lambda x: x["rerank_score"], reverse=True)
    return chunks[:top_k]


def _adjust_scores_by_metadata(query: str, chunks: list[dict]) -> list[dict]:
    """
    Adjust rerank scores based on document title/filename relevance.
    If a chunk comes from a document whose title doesn't match the query topic,
    penalize its score. If the title is highly relevant, boost it slightly.
    """
    query_lower = query.lower()

    # Extract key terms from query (simple keyword extraction)
    # Remove common stop words
    stop_words = {
        "what", "is", "the", "a", "an", "how", "to", "do", "does", "can",
        "between", "and", "or", "in", "for", "of", "with", "from", "by",
        "this", "that", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "will", "would", "could", "should",
        "which", "who", "whom", "where", "when", "why",
        "i", "you", "he", "she", "it", "we", "they", "my", "your",
        "difference", "explain", "compare", "describe", "tell", "me", "about",
    }

    query_terms = set()
    for word in query_lower.split():
        # Clean punctuation
        clean = word.strip("?.,!;:'\"")
        if clean and clean not in stop_words and len(clean) > 2:
            query_terms.add(clean)

    for chunk in chunks:
        filename = chunk["metadata"].get("filename", "").lower().replace("-", " ").replace("_", " ").replace(".md", "")
        title = chunk["metadata"].get("title", "").lower()
        section = chunk["metadata"].get("section", "").lower()

        # Combine all metadata into one string for matching
        meta_text = f"{filename} {title} {section}"

        # Count how many query terms appear in metadata
        matches = sum(1 for term in query_terms if term in meta_text)
        match_ratio = matches / max(len(query_terms), 1)

        # Apply adjustment
        if match_ratio >= 0.5:
            # Document title is relevant to the query — small boost
            chunk["rerank_score"] *= 1.1
        elif match_ratio == 0:
            # Document title has NO relation to query terms — penalize
            chunk["rerank_score"] *= 0.7
        # Otherwise leave score unchanged

    return chunks


def chunks_to_results(chunks: list[dict]) -> list[SearchResult]:
    """Convert internal chunks to SearchResult objects."""
    results = []
    for chunk in chunks:
        metadata = chunk["metadata"]
        raw_score = chunk.get("rerank_score", 1 - chunk.get("distance", 0.5))
        normalized = max(0, min(100, (raw_score + 5) * 10))

        results.append(SearchResult(
            text=chunk["text"],
            filename=metadata.get("filename", "unknown"),
            section=metadata.get("section", ""),
            source_url=metadata.get("source", ""),
            relevance_score=round(normalized, 1)
        ))

    return results


def build_rag_messages(query: str, chunks: list[dict], history: list[dict]) -> list[dict]:
    """Build LLM messages with RAG context."""
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        source = chunk["metadata"].get("filename", "doc")
        section = chunk["metadata"].get("section", "")
        source_label = source
        if section:
            source_label += f" · {section}"
        context_parts.append(f"[Source {i}: {source_label}]\n{chunk['text']}")

    context = "\n\n---\n\n".join(context_parts)

    system_prompt = f"""You are a specialized assistant that answers questions about technical documentation.

RULES:
- Answer ONLY based on the context provided below.
- If the information is not in the context, clearly state that you could not find the answer.
- ALWAYS cite the sources used in the format [Source N] after each statement.
- Answer in the same language the user asks in.
- If there is conflicting information between sources, mention both.

DOCUMENTATION CONTEXT:
{context}"""

    messages = [{"role": "system", "content": system_prompt}]

    for msg in history[-10:]:
        messages.append({
            "role": msg.get("role", "user"),
            "content": msg.get("content", "")
        })

    messages.append({"role": "user", "content": query})
    return messages


# ── Classifier ─────────────────────────────────────────────────

CLASSIFIER_PROMPT = """You are a query router. Your ONLY job is to classify the user's intent.

Reply with ONLY one of two words: SEARCH or CHAT

Use SEARCH when:
- The question seeks a specific, factual piece of data (deadline, value, link, name)
- The question can be answered with a direct excerpt from the documentation
- Questions like "what is", "where is", "how much", "what link"
- Short, objective questions

Use CHAT when:
- The question asks for explanation, comparison, or interpretation
- The question requires combining information from multiple sections
- Questions like "what is the difference", "why", "explain", "how does it work"
- The question is complex or has multiple parts
- The question references a previous conversation

Reply ONLY: SEARCH or CHAT"""


def classify_query_heuristic(query: str, history: list[dict]) -> dict:
    """Heuristic-based classification (fallback)."""
    q_lower = query.lower().strip()

    chat_signals = [
        "why", "explain", "how does", "what is the difference",
        "compare", "step by step", "in detail",
        "can you help", "what happens if",
        "por que", "porque", "explique", "como funciona",
        "qual a diferença", "compare", "passo a passo",
    ]

    for signal in chat_signals:
        if signal in q_lower:
            return {"mode": "chat", "reason": f"Pattern '{signal}' detected → needs explanation"}

    if history:
        return {"mode": "chat", "reason": "Ongoing conversation → context needed"}

    if len(query.split()) > 15:
        return {"mode": "chat", "reason": "Long question → likely complex"}

    return {"mode": "search", "reason": "Objective question → direct search"}


async def classify_query(query: str, history: list[dict], provider_name: str | None = None, api_key: str | None = None) -> dict:
    """Classify via LLM or heuristic."""
    llm = resolve_llm(provider_name, api_key)

    if not llm:
        result = classify_query_heuristic(query, history)
        result["reason"] += " (heuristic)"
        return result

    try:
        response = llm.classify(CLASSIFIER_PROMPT, query)

        if "CHAT" in response.upper():
            return {"mode": "chat", "reason": f"Classifier ({llm.name}): needs explanation"}
        else:
            return {"mode": "search", "reason": f"Classifier ({llm.name}): direct search"}
    except Exception as e:
        print(f"Classifier error, falling back to heuristic: {e}")
        return classify_query_heuristic(query, history)


# ── Endpoints ──────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "chunks_loaded": chroma_collection.count() if chroma_collection else 0,
        "llm_available": registry.is_available() if registry else False,
        "providers": registry.list_available() if registry else [],
        "default_provider": registry.default if registry else None,
    }


@app.get("/providers")
async def list_providers():
    """List available LLM providers."""
    return {
        "providers": registry.list_available() if registry else [],
        "default": registry.default if registry else None,
    }


@app.post("/providers/switch")
async def switch_provider(request: SwitchProviderRequest):
    """Switch the default provider."""
    provider = registry.get(request.provider)
    if not provider:
        available = [p["name"] for p in registry.list_available()]
        raise HTTPException(
            404,
            f"Provider '{request.provider}' not found. Available: {available}"
        )

    registry.default = request.provider
    return {
        "message": f"Provider switched to {request.provider}",
        "active": request.provider,
        "model": provider.model
    }


@app.post("/search", response_model=SearchResponse)
async def semantic_search(request: SearchRequest):
    """Pure semantic search (no LLM)."""
    if not chroma_collection:
        raise HTTPException(500, "Vector store not loaded")

    chunks = retrieve_chunks(request.query, top_k=TOP_K_RETRIEVAL)
    reranked = rerank_chunks(request.query, chunks, top_k=request.top_k)
    results = chunks_to_results(reranked)

    return SearchResponse(
        query=request.query,
        results=results,
        total_chunks_searched=chroma_collection.count()
    )


@app.post("/chat", response_model=ChatResponse)
async def rag_chat(request: ChatRequest):
    """RAG chat using the selected provider."""
    llm = resolve_llm(request.provider, request.api_key)
    if not llm:
        raise HTTPException(503, "No LLM provider available. Provide an API key or configure one in .env")

    if not chroma_collection:
        raise HTTPException(500, "Vector store not loaded")

    chunks = retrieve_chunks(request.query, top_k=TOP_K_RETRIEVAL)
    reranked = rerank_chunks(request.query, chunks, top_k=TOP_K_RERANK)
    messages = build_rag_messages(request.query, reranked, request.history)

    try:
        response = llm.complete(messages, temperature=0.1, max_tokens=1024)
    except Exception as e:
        raise HTTPException(503, f"Error calling {llm.name}: {str(e)}")

    sources = chunks_to_results(reranked)

    return ChatResponse(
        query=request.query,
        answer=response.text,
        sources=sources,
        provider_used=response.provider,
        model_used=response.model
    )


@app.post("/ask", response_model=AskResponse)
async def unified_ask(request: AskRequest):
    """
    Unified endpoint with 4 query modes:
    - search_only:  always returns raw document chunks (0 LLM calls)
    - auto_smart:   heuristic decides search vs chat (0-1 LLM calls)
    - auto_llm:     LLM classifier decides search vs chat (1-2 LLM calls)
    - always_chat:  always generates AI answer (1 LLM call)
    """
    if not chroma_collection:
        raise HTTPException(500, "Vector store not loaded")

    query_mode = request.mode or "auto_smart"

    # ── 1. Retrieval + Reranking (all modes need this) ─────────
    chunks = retrieve_chunks(request.query, top_k=TOP_K_RETRIEVAL)
    reranked = rerank_chunks(request.query, chunks, top_k=TOP_K_RERANK)
    results = chunks_to_results(reranked)
    total = chroma_collection.count()

    # ── 2. Route based on mode ─────────────────────────────────

    # Mode: Search Only — always return raw chunks
    if query_mode == "search_only":
        return AskResponse(
            query=request.query,
            mode="search",
            reason="Mode: Search Only — returning document excerpts",
            results=results,
            total_chunks_searched=total
        )

    # Mode: Always Chat — skip classification, go straight to LLM
    if query_mode == "always_chat":
        llm = resolve_llm(request.provider, request.api_key)
        if not llm:
            return AskResponse(
                query=request.query,
                mode="search",
                reason="Mode: Always Chat (fallback: no LLM available — returning search results)",
                results=results,
                total_chunks_searched=total
            )

        messages = build_rag_messages(request.query, reranked, request.history)
        try:
            response = llm.complete(messages, temperature=0.1, max_tokens=1024)
        except Exception as e:
            return AskResponse(
                query=request.query,
                mode="search",
                reason=f"Mode: Always Chat (fallback: {e} — returning search results)",
                results=results,
                total_chunks_searched=total
            )

        return AskResponse(
            query=request.query,
            mode="chat",
            reason="Mode: Always Chat — AI-generated answer",
            answer=response.text,
            results=results,
            total_chunks_searched=total,
            provider_used=response.provider,
            model_used=response.model
        )

    # Mode: Auto (Smart) — heuristic classification (free)
    if query_mode == "auto_smart":
        classification = classify_query_heuristic(request.query, request.history)
        mode = classification["mode"]
        reason = f"Auto (Smart): {classification['reason']}"

    # Mode: Auto (LLM) — LLM-based classification (1 extra call)
    elif query_mode == "auto_llm":
        classification = await classify_query(
            request.query, request.history, request.provider, request.api_key
        )
        mode = classification["mode"]
        reason = f"Auto (LLM): {classification['reason']}"

    else:
        # Unknown mode — default to auto_smart
        classification = classify_query_heuristic(request.query, request.history)
        mode = classification["mode"]
        reason = f"Auto (Smart, default): {classification['reason']}"

    # ── 3. If classifier chose search, return chunks ───────────
    if mode == "search":
        return AskResponse(
            query=request.query,
            mode="search",
            reason=reason,
            results=results,
            total_chunks_searched=total
        )

    # ── 4. If classifier chose chat, generate answer ───────────
    llm = resolve_llm(request.provider, request.api_key)
    if not llm:
        return AskResponse(
            query=request.query,
            mode="search",
            reason=reason + " (fallback: no LLM available)",
            results=results,
            total_chunks_searched=total
        )

    messages = build_rag_messages(request.query, reranked, request.history)

    try:
        response = llm.complete(messages, temperature=0.1, max_tokens=1024)
    except Exception as e:
        return AskResponse(
            query=request.query,
            mode="search",
            reason=reason + f" (fallback: {e})",
            results=results,
            total_chunks_searched=total
        )

    return AskResponse(
        query=request.query,
        mode="chat",
        reason=reason,
        answer=response.text,
        results=results,
        total_chunks_searched=total,
        provider_used=response.provider,
        model_used=response.model
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)