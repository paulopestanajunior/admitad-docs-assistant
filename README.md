# 🔍 Admitad Docs Assistant — RAG Chat with Smart Routing

An intelligent documentation assistant for the **Admitad Advertiser Knowledge Base**. Ask questions in natural language and get accurate answers with source citations — powered by semantic search and RAG (Retrieval-Augmented Generation).

## How It Works

```
User asks a question
        │
        ▼
┌──────────────────────┐
│   MODE SELECTOR       │ ← User chooses in sidebar
└──────────┬───────────┘
           │
    ┌──────┼──────────────────┐
    ▼      ▼                  ▼
┌────────┐ ┌────────────┐ ┌────────────┐
│SEARCH  │ │ AUTO MODE  │ │ ALWAYS     │
│ONLY    │ │            │ │ CHAT       │
│        │ │ Heuristic  │ │            │
│Returns │ │ or LLM     │ │ Always     │
│raw doc │ │ decides    │ │ generates  │
│chunks  │ │ the route  │ │ AI answer  │
│        │ │   ↓    ↓   │ │ with cited │
│0 LLM   │ │SEARCH CHAT │ │ sources    │
│calls   │ │            │ │            │
└────────┘ └────────────┘ └────────────┘
```

**4 query modes** to fit every use case:

| Mode | Classifier | LLM Calls | Best For |
|---|---|---|---|
| 🔍 **Search Only** | None | 0 | Quick lookups, no API key needed |
| ⚡ **Auto (Smart)** | Heuristic (free) | 0–1 | Balanced cost and quality |
| 🧠 **Auto (LLM)** | LLM classifies | 1–2 | Maximum routing accuracy |
| 💬 **Always Chat** | None | 1 | Always want a full explanation |

> 📖 **[See detailed explanation with examples →](MODES.md)**

### Quick Example

**Question:** *"What documents are required for cooperation with Admitad?"*

| Search Only | Always Chat |
|---|---|
| 📄 Returns the raw excerpt: *"To launch an affiliate program, provide: Supporting documents, Your company's payment details. Send to advsupport@admitad.com"* | 🤖 Returns an interpreted answer: *"To cooperate with Admitad, you need supporting documents (such as a certificate of residence, valid and issued within one year) and your company's payment details. Send everything to advsupport@admitad.com. [Source 1] [Source 2]"* |
| Raw chunks from docs — you read and interpret | AI combines multiple sources into a clear answer |

---

## Features

- **4 query modes** — from zero-cost search to full AI answers ([details](MODES.md))
- **Smart routing** — heuristic or LLM classifier decides between search and chat
- **Multi-provider LLM** — supports Groq, OpenAI, Anthropic, and Google Gemini
- **Bring Your Own Key** — users paste their API key in the sidebar, works instantly
- **No key required** — semantic search works without any API key
- **Multilingual** — embeddings support English, Portuguese, Spanish, and 90+ languages
- **Reranking** — cross-encoder reranks results for higher precision
- **Source attribution** — every answer cites the exact document and section
- **Automatic fallback** — if LLM fails, falls back to semantic search seamlessly

---

## Supported LLM Providers

| Provider | Default Model | Cost | Env Variable |
|---|---|---|---|
| **Groq** | Llama 3.3 70B | Free | `GROQ_API_KEY` |
| **OpenAI** | GPT-4o Mini | Paid | `OPENAI_API_KEY` |
| **Anthropic** | Claude Sonnet | Paid | `ANTHROPIC_API_KEY` |
| **Google Gemini** | Gemini 1.5 Flash | Free tier | `GOOGLE_API_KEY` |

Configure as many as you want — the system auto-detects which are available.
Users can also provide their own key directly in the UI (no server config needed).

**Get a free key:**
- [Groq Console](https://console.groq.com/keys) (recommended — free, fast)
- [Google AI Studio](https://aistudio.google.com/apikey) (free tier)

---

## Quick Start

### Prerequisites

- Python 3.11 or 3.12 (⚠️ Python 3.13 is not yet supported by ML libraries)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/admitad-docs-assistant.git
cd admitad-docs-assistant
```

### 2. Create virtual environment and install dependencies

**Windows:**
```bash
py -3.11 -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Edit `.env` and add at least one API key (or skip this — users can provide their own key in the UI):

```env
GROQ_API_KEY=gsk_your_key_here
# OPENAI_API_KEY=sk-your_key_here
# ANTHROPIC_API_KEY=sk-ant-your_key_here
# GOOGLE_API_KEY=AI_your_key_here
```

### 4. Add documentation

Place your `.md`, `.txt`, or `.html` files in the `docs/` folder.

To scrape the Admitad Advertiser documentation automatically:

```bash
python scraper.py
```

This downloads all articles from the Admitad Advertisers knowledge base and saves them as markdown files in `docs/`.

### 5. Ingest documents into vector store

```bash
python ingest.py
```

This will:
- Load all documents from `docs/`
- Split them into chunks (by sections and paragraphs)
- Generate embeddings using `multilingual-e5-large` (~1.2GB download on first run)
- Store everything in ChromaDB at `chroma_db/`

⏱️ **First run takes ~30 minutes on CPU** (embedding 1200+ chunks). Subsequent runs with the same documents are instant since models are cached.

### 6. Start the backend

```bash
uvicorn api:app --reload --port 8000
```

### 7. Start the frontend (new terminal)

```bash
# Activate the same venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS / Linux

streamlit run app.py
```

### 8. Open in browser

```
http://localhost:8501
```

---

## Adding New Documents (Incremental Update)

To add more documentation to the system:

### Option A: Add files and re-ingest (recommended)

```bash
# 1. Add new .md / .txt / .html files to the docs/ folder
#    You can organize in subfolders — the ingester reads recursively

# 2. Re-run ingestion (this rebuilds the entire vector store)
python ingest.py

# 3. Restart the backend
#    If using --reload, it restarts automatically
```

> **Note:** Currently, `ingest.py` rebuilds the full vector store each time. This ensures consistency but takes ~30 min on CPU. For large-scale use, consider implementing incremental ingestion (see Contributing guide).

### Option B: Re-scrape and ingest

If the Admitad documentation has been updated:

```bash
# 1. Delete old docs (optional — scraper overwrites existing files)
rmdir /s /q docs        # Windows
rm -rf docs             # macOS / Linux

# 2. Re-scrape
python scraper.py

# 3. Re-ingest
python ingest.py
```

### Option C: Add a single document manually

Create a markdown file in `docs/` with this format:

```markdown
---
title: Your Article Title
section: category-name
source: https://example.com/original-article
---

# Your Article Title

Your content here...
```

The frontmatter (`title`, `section`, `source`) is optional but helps with source attribution in answers.

---

## Project Structure

```
admitad-docs-assistant/
├── docs/                  # Documentation files (.md, .txt, .html)
├── chroma_db/             # Vector store (generated by ingest.py)
├── api.py                 # FastAPI backend (routing, search, chat)
├── app.py                 # Streamlit frontend (chat interface)
├── ingest.py              # Document ingestion pipeline
├── llm_providers.py       # Multi-provider LLM abstraction
├── scraper.py             # Admitad documentation scraper
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container config for deployment
├── .env.example           # Environment variables template
├── .gitignore
├── CONTRIBUTING.md         # Contribution guidelines
└── README.md              # This file
```

---

## API Reference

All endpoints are available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | System status, loaded chunks, available providers |
| `/providers` | GET | List available LLM providers |
| `/providers/switch` | POST | Switch the active default provider |
| `/ask` | POST | **Unified endpoint** — classifier + automatic routing |
| `/search` | POST | Pure semantic search (no LLM) |
| `/chat` | POST | Direct RAG chat |

### POST `/ask` — Unified Endpoint

This is the main endpoint. It classifies the question, retrieves relevant chunks, and either returns search results or generates an AI answer.

**Request:**
```json
{
  "query": "What is the difference between tracking code and postback?",
  "history": [],
  "api_key": "gsk_...",
  "provider": "groq"
}
```

- `query` (required): The user's question
- `history` (optional): Previous conversation messages for context
- `api_key` (optional): User-provided API key (overrides server config)
- `provider` (optional): Force a specific provider (`groq`, `openai`, `anthropic`, `google`)

**Response:**
```json
{
  "query": "What is the difference between tracking code and postback?",
  "mode": "chat",
  "reason": "Classifier (groq): needs explanation",
  "answer": "The main difference is... [Source 1] ... [Source 2]",
  "results": [
    {
      "text": "Integration via tracking code...",
      "filename": "integration-via-tracking-code.md",
      "section": "Integration via tracking code",
      "source_url": "https://support.mitgo.com/...",
      "relevance_score": 100.0
    }
  ],
  "total_chunks_searched": 1243,
  "provider_used": "groq",
  "model_used": "llama-3.3-70b-versatile"
}
```

---

## Deployment to HuggingFace Spaces (Free)

### 1. Create a HuggingFace account

Sign up at [huggingface.co/join](https://huggingface.co/join) — free, no credit card.

### 2. Create an Access Token

Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) → New token → **Write** access.

### 3. Create a Space

Go to [huggingface.co/new-space](https://huggingface.co/new-space):
- **Space name:** `admitad-docs-assistant`
- **SDK:** Docker
- **Template:** Blank
- **Hardware:** CPU Basic (Free)
- **Visibility:** Public

### 4. Add secrets (optional)

If you want the server to have a default LLM provider:
- Go to Space **Settings** → **Repository Secrets**
- Add `GROQ_API_KEY` with your key

> This is optional — users can provide their own key in the UI.

### 5. Clone and push

```bash
git lfs install
git clone https://huggingface.co/spaces/YOUR_USERNAME/admitad-docs-assistant
cd admitad-docs-assistant

# Copy all project files here (including docs/ and chroma_db/)
# Make sure the Dockerfile is present

git add .
git commit -m "Initial deploy"
git push
```

> **Important:** When git asks for a password, use your **HuggingFace Access Token**, not your account password.

### 6. Wait for build

The build takes ~15-25 minutes on first deploy (downloading ML models). Monitor progress in the **Logs** tab of your Space.

### 7. Access your app

```
https://YOUR_USERNAME-admitad-docs-assistant.hf.space
```

### Dockerfile for HuggingFace

Make sure this `Dockerfile` is in your project root:

```dockerfile
FROM python:3.11-slim

RUN useradd -m -u 1000 user
WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-download ML models during build
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/multilingual-e5-large')"
RUN python -c "from sentence_transformers import CrossEncoder; CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')"

RUN chown -R user:user /app
USER user

EXPOSE 7860

CMD bash -c "\
    if [ ! -d 'chroma_db' ]; then python ingest.py; fi && \
    uvicorn api:app --host 0.0.0.0 --port 8000 & \
    streamlit run app.py --server.port 7860 --server.address 0.0.0.0 --server.headless true --browser.gatherUsageStats false"
```

> **Tip:** Include the `chroma_db/` folder in your repo to skip the ingestion step on every restart (~30 min saved).

---

## Updating the Deployment

After making changes locally:

```bash
cd admitad-docs-assistant
git add .
git commit -m "Description of changes"
git push
```

HuggingFace automatically rebuilds and redeploys.

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| Embeddings | `multilingual-e5-large` | Multilingual semantic search |
| Vector Store | ChromaDB | Local persistent vector database |
| Reranker | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Rerank results for precision |
| LLM | Groq / OpenAI / Anthropic / Google | Answer generation + classification |
| Backend | FastAPI | REST API with auto docs |
| Frontend | Streamlit | Chat interface with provider selector |

---

## Troubleshooting

### `OSError: O arquivo de paginação é muito pequeno` (Windows)
The embedding model (~2.2GB) is exceeding available RAM. Close other applications (browsers, IDEs) and try again. If it persists, switch to the smaller model in `ingest.py` and `api.py`:
```python
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"  # 500MB instead of 2.2GB
```
Then re-run `python ingest.py`.

### `model has been decommissioned` (Groq)
Groq periodically retires old models. Update the model name in `llm_providers.py` or `.env`:
```
GROQ_MODEL=llama-3.3-70b-versatile
```

### `DuplicateIDError` during ingestion
This was fixed in the latest `ingest.py`. Make sure you're using the version with `_next_chunk_id()` that includes a global counter.

### `Python 3.13` compatibility issues
Python 3.13 is too new for many ML libraries. Use Python 3.11 or 3.12:
```bash
py -3.11 -m venv venv
```

### HuggingFace build fails with out of memory
Switch to the smaller embedding model (`multilingual-e5-base`) or upload `chroma_db/` pre-built to skip ingestion.

---

## License

MIT

---

## Acknowledgments

- [Admitad / Mitgo](https://support.mitgo.com) — Documentation source
- [HuggingFace](https://huggingface.co) — Embedding models and hosting
- [Groq](https://groq.com) — Free LLM inference
- [ChromaDB](https://www.trychroma.com) — Vector database
- [Streamlit](https://streamlit.io) — Frontend framework