---
title: Admitad Docs Assistant
emoji: 🔍
colorFrom: indigo
colorTo: green
sdk: docker
app_port: 7860
pinned: false
license: mit
---

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
| 🔍 **Search Only — Free, no AI** | None | 0 | Quick lookups, no API key needed |
| ⚡ **Smart Auto — Best balance** | Heuristic (free) | 0–1 | Balanced cost and quality |
| 🧠 **AI Auto — Most accurate routing** | LLM classifies | 1–2 | Maximum routing accuracy |
| 💬 **Always AI Answer** | None | 1 | Always want a full explanation |

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

## Troubleshooting & FAQ

### Setup & Installation

<details>
<summary><b>❌ Python 3.13: <code>numpy</code> fails to build / <code>metadata-generation-failed</code></b></summary>

Python 3.13 is too new — many ML libraries (numpy, sentence-transformers, chromadb) don't have pre-built wheels for it yet, so pip tries to compile from source and fails on Windows.

**Solution:** Use Python 3.11 or 3.12:
```bash
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Check available versions with `py --list`.
</details>

<details>
<summary><b>❌ Windows: <code>OSError: O arquivo de paginação é muito pequeno</code> (OS error 1455)</b></summary>

The embedding model (`multilingual-e5-large`, ~2.2GB) is exceeding available RAM when loading.

**Solutions (try in order):**
1. Close other applications (browser tabs, IDEs, AnythingLLM, etc.) and try again
2. If it still fails, switch to the smaller model in both `ingest.py` and `api.py`:
```python
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"  # 500MB instead of 2.2GB
```
Then re-run `python ingest.py` (re-ingestion required when changing model).
</details>

<details>
<summary><b>❌ <code>DuplicateIDError: Expected IDs to be unique</code> during ingestion</b></summary>

Some document chunks produce identical MD5 hashes, causing ChromaDB to reject them.

**Solution:** Make sure you're using the latest `ingest.py` with the `_next_chunk_id()` function that includes a global counter. The fix generates unique IDs by combining filename + counter + text prefix.
</details>

<details>
<summary><b>❌ <code>ModuleNotFoundError: No module named 'requests'</code></b></summary>

Your virtual environment is not activated, or dependencies aren't installed.

**Solution:**
```bash
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```
</details>

### LLM & Providers

<details>
<summary><b>❌ <code>model 'llama-3.1-70b-versatile' has been decommissioned</code></b></summary>

Groq periodically retires old models.

**Solution:** Update the model name in `llm_providers.py` or your `.env`:
```
GROQ_MODEL=llama-3.3-70b-versatile
```
Check available models at [console.groq.com/docs/models](https://console.groq.com/docs/models).
</details>

<details>
<summary><b>❌ Classifier falls back to heuristic / <code>Error code: 400</code></b></summary>

Usually caused by an expired/invalid API key or a decommissioned model.

**Diagnosis:**
```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GROQ_API_KEY')[:10])"
```
If this prints the first 10 characters, the key is loaded. Test it directly:
```bash
python -c "
from groq import Groq
client = Groq(api_key='YOUR_FULL_KEY')
r = client.chat.completions.create(model='llama-3.3-70b-versatile', messages=[{'role':'user','content':'Hello'}], max_tokens=10)
print(r.choices[0].message.content)
"
```
</details>

<details>
<summary><b>⚠️ <code>Failed to send telemetry event</code> warnings from ChromaDB</b></summary>

These are harmless ChromaDB telemetry warnings — they do not affect functionality. ChromaDB tries to send anonymous usage analytics and fails. You can safely ignore them.
</details>

<details>
<summary><b>⚠️ <code>Field "model_used" has conflict with protected namespace "model_"</code></b></summary>

Pydantic warning about a field name conflicting with its internal namespace. Does not affect functionality. Can be suppressed by adding to the Pydantic models:
```python
model_config = {"protected_namespaces": ()}
```
</details>

### HuggingFace Deployment

<details>
<summary><b>❌ HF push rejected: <code>files larger than 10 MiB</code></b></summary>

The `chroma_db/chroma.sqlite3` file exceeds HuggingFace's regular file size limit.

**Solution:** Use Git LFS to track large files:
```bash
git lfs install
git lfs track "chroma_db/chroma.sqlite3"
git add .gitattributes
git add chroma_db/chroma.sqlite3 --force
git commit --amend --no-edit
git push
```
</details>

<details>
<summary><b>❌ HF push: <code>read access but not the required permissions</code></b></summary>

Your HuggingFace token only has Read access.

**Solution:** Create a new token with **Write** permissions:
1. Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Create token with Write access
3. Clear cached credentials and re-push:
```bash
cmdkey /delete:git:https://huggingface.co     # Windows
git push
```
</details>

<details>
<summary><b>❌ HF build: out of memory</b></summary>

The embedding model download (~2.2GB) + ingestion can exceed the free tier memory.

**Solutions:**
1. Include `chroma_db/` pre-built in your repo (skips ingestion on startup)
2. Switch to the smaller model `intfloat/multilingual-e5-base` in the Dockerfile
</details>

<details>
<summary><b>❌ HF Space shows "Building" forever</b></summary>

First build takes 15-25 minutes (downloading ML models). Check the **Build** tab for progress. If it stalls for more than 30 minutes, check for errors in the build logs.
</details>

### GitHub Actions (Auto-Sync)

<details>
<summary><b>❌ GitHub push rejected: <code>refusing to allow a Personal Access Token to create or update workflow</code></b></summary>

Your GitHub Personal Access Token doesn't have the `workflow` scope.

**Solution:**
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Edit your token → enable ✅ **workflow** scope
3. Save, then clear cached credentials and retry:
```bash
cmdkey /delete:git:https://github.com     # Windows
git push
```
</details>

<details>
<summary><b>❌ GitHub Action fails: <code>chroma.sqlite3 larger than 10 MiB</code></b></summary>

The auto-sync workflow pushes the full repo to HuggingFace, including the large `chroma_db/` folder.

**Solution:** The workflow is configured to exclude `chroma_db/` from the sync. The HuggingFace Space keeps its own copy from the initial manual push. If you need to update the vector store on HuggingFace, push directly:
```bash
cd hf-space
git add chroma_db/
git commit -m "docs: update vector store"
git push
```
</details>

<details>
<summary><b>ℹ️ How does GitHub → HuggingFace sync work?</b></summary>

A GitHub Actions workflow (`.github/workflows/sync-to-hf.yml`) runs on every push to `main`. It:

1. Checks out the code
2. Removes `chroma_db/` from tracking (to avoid LFS issues)
3. Force-pushes to HuggingFace Spaces

**Important notes:**
- Code changes sync automatically
- `chroma_db/` does NOT sync automatically (too large). Update it manually via `hf-space/` repo
- Secrets (`GROQ_API_KEY`) must be configured separately on both platforms
- The `HF_TOKEN` secret must be set in GitHub repo Settings → Secrets → Actions
</details>

### Updating Documents

<details>
<summary><b>ℹ️ How do I add new documents?</b></summary>

1. Add `.md` / `.txt` / `.html` files to the `docs/` folder
2. Re-run ingestion: `python ingest.py` (~30 min on CPU)
3. Push code changes: `git push` (auto-syncs to HuggingFace)
4. To update `chroma_db/` on HuggingFace, push manually to `hf-space/` repo

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.
</details>

<details>
<summary><b>ℹ️ How do I update the vector store on HuggingFace after adding new docs?</b></summary>

The auto-sync workflow does NOT sync `chroma_db/` (file too large for regular git). After re-running `python ingest.py` locally:

```bash
# Option A: Push chroma_db directly to HuggingFace
cd hf-space
xcopy /E /I /Y C:\Users\paulo\admitad-rag-chat-project\chroma_db\* chroma_db\
git add chroma_db/
git commit -m "docs: update vector store with new articles"
git push

# Option B: Let HuggingFace re-ingest on restart
# Remove chroma_db/ from HuggingFace and it will run ingest.py on next boot (~30 min)
```
</details>

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