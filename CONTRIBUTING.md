# Contributing to Admitad Docs Assistant

Thank you for your interest in contributing! This guide covers how to add documentation, improve the codebase, and deploy your changes.

---

## Table of Contents

- [Adding New Documentation](#adding-new-documentation)
- [Development Setup](#development-setup)
- [Project Architecture](#project-architecture)
- [Making Code Changes](#making-code-changes)
- [Testing Your Changes](#testing-your-changes)
- [Deploying Updates](#deploying-updates)
- [Code Style](#code-style)
- [Pull Request Guidelines](#pull-request-guidelines)

---

## Adding New Documentation

This is the most common contribution — adding or updating articles in the knowledge base.

### Adding a single article

1. Create a `.md` file in the `docs/` folder:

```markdown
---
title: Your Article Title
section: general-information
source: https://support.mitgo.com/knowledge-base/article/your-article
---

# Your Article Title

Article content goes here.
Use markdown formatting — headers, lists, code blocks, etc.
```

2. Re-run ingestion:

```bash
python ingest.py
```

3. Restart the backend (or let `--reload` pick it up).

### Adding multiple articles at once

1. Place all `.md` / `.txt` / `.html` files in `docs/` (subfolders are supported).
2. Run `python ingest.py` — it processes everything in `docs/` recursively.

### Re-scraping from the Admitad website

If the official documentation has been updated:

```bash
# Optional: clear old docs
rm -rf docs/        # macOS/Linux
rmdir /s /q docs    # Windows

# Scrape fresh articles
python scraper.py

# Re-ingest
python ingest.py
```

### Frontmatter format

The frontmatter block at the top of each `.md` file is optional but recommended:

```yaml
---
title: Article Title          # Used in source citations
section: technical-integration # Category for organization
source: https://...           # Link to original article
---
```

If omitted, the system will use the filename as the title.

### Supported file formats

| Format | Notes |
|---|---|
| `.md` | Recommended — best chunking by headers |
| `.txt` | Plain text, chunked by paragraphs |
| `.html` | HTML content, converted during ingestion |

### Important: Re-ingestion is required

After adding or modifying documents, you **must** run `python ingest.py` to rebuild the vector store. The system does not auto-detect new files at runtime.

> **Future improvement:** Incremental ingestion that only processes new/changed files. See [Roadmap](#roadmap).

---

## Development Setup

### Prerequisites

- Python 3.11 or 3.12
- Git
- At least one LLM API key (or users provide their own)

### First-time setup

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/admitad-docs-assistant.git
cd admitad-docs-assistant

# Virtual environment
py -3.11 -m venv venv          # Windows
python3.11 -m venv venv        # macOS/Linux

# Activate
venv\Scripts\activate           # Windows
source venv/bin/activate        # macOS/Linux

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Environment
cp .env.example .env
# Edit .env with your API key(s)

# Ingest docs (if chroma_db/ doesn't exist)
python ingest.py

# Run
uvicorn api:app --reload --port 8000    # Terminal 1
streamlit run app.py                     # Terminal 2
```

---

## Project Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  Streamlit   │────▶│   FastAPI     │────▶│  ChromaDB    │
│  (app.py)    │     │   (api.py)    │     │  (vectors)   │
│              │     │               │     └──────────────┘
│  - Chat UI   │     │  - /ask       │
│  - API key   │     │  - /search    │     ┌──────────────┐
│    input     │     │  - /chat      │────▶│  LLM Provider│
│  - Provider  │     │  - classifier │     │  (Groq/OAI/  │
│    selector  │     │  - reranker   │     │   Anthropic/ │
└─────────────┘     └──────────────┘     │   Google)    │
                                          └──────────────┘
```

### Key files

| File | Responsibility |
|---|---|
| `api.py` | FastAPI backend — routing, search, RAG chat, classifier |
| `app.py` | Streamlit frontend — chat UI, API key input, provider selector |
| `llm_providers.py` | Multi-provider abstraction (Groq, OpenAI, Anthropic, Google) |
| `ingest.py` | Document processing — chunking, embeddings, ChromaDB storage |
| `scraper.py` | Scrapes Admitad documentation into markdown files |

### Data flow

1. `scraper.py` → downloads articles → saves as `.md` in `docs/`
2. `ingest.py` → reads `docs/` → chunks → embeddings → stores in `chroma_db/`
3. `api.py` → loads `chroma_db/` → serves search and RAG endpoints
4. `app.py` → calls `api.py` → renders results in chat interface

---

## Making Code Changes

### Branching strategy

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Commit
git add .
git commit -m "feat: description of your change"

# Push
git push origin feature/your-feature-name

# Open a Pull Request on GitHub
```

### Commit message format

Use conventional commits:

```
feat: add support for PDF documents
fix: resolve duplicate chunk IDs in ingestion
docs: update README with deployment instructions
refactor: extract classifier into separate module
chore: update dependencies
```

### Common changes

#### Adding a new LLM provider

1. Edit `llm_providers.py` — add a new provider class
2. Edit `api.py` → `_create_provider_from_key()` — add the key prefix detection
3. Edit `app.py` → `detect_provider()` — add the key prefix mapping
4. Update `requirements.txt` with the provider's SDK
5. Update `.env.example` with the new env variable
6. Update `README.md` with the provider info

#### Changing the embedding model

1. Edit `EMBEDDING_MODEL` in both `ingest.py` and `api.py` (must match!)
2. Re-run `python ingest.py` (full re-ingestion required)
3. Update `Dockerfile` if deploying to HuggingFace

#### Modifying the classifier prompt

Edit `CLASSIFIER_PROMPT` in `api.py`. The classifier should return exactly `SEARCH` or `CHAT`. Test with various question types before committing.

#### Modifying the RAG system prompt

Edit `build_rag_messages()` in `api.py`. This controls how the LLM generates answers from the retrieved context.

---

## Testing Your Changes

### Manual testing checklist

After any change, test these scenarios:

```
1. Simple factual question (should route to SEARCH):
   "What documents are required for cooperation with Admitad?"

2. Complex comparison question (should route to CHAT):
   "What is the difference between tracking code and postback integration?"

3. Question with no answer in docs (should say it doesn't know):
   "What is the CEO's email address?"

4. Question in another language (should respond in same language):
   "Quais documentos são necessários para cooperar com a Admitad?"

5. Without API key (should fall back to semantic search):
   Clear the API key field and ask any question.

6. With invalid API key (should fall back gracefully):
   Enter "invalid_key_12345" and ask a question.
```

### API testing

FastAPI auto-generates interactive docs:

```
http://localhost:8000/docs     # Swagger UI
http://localhost:8000/redoc    # ReDoc
```

### Health check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "ok",
  "chunks_loaded": 1243,
  "llm_available": true,
  "providers": [...],
  "default_provider": "groq"
}
```

---

## Deploying Updates

### To HuggingFace Spaces

```bash
# Make sure you're in the HuggingFace repo directory
cd admitad-docs-assistant

# Add changes
git add .
git commit -m "feat: your change description"
git push
```

HuggingFace automatically rebuilds and redeploys. Monitor the **Logs** tab.

### If you added new documents

After adding docs and re-running `python ingest.py` locally:

**Option A (faster startup):** Include `chroma_db/` in the push
```bash
# Remove chroma_db from .gitignore temporarily
git add chroma_db/
git commit -m "docs: update vector store with new articles"
git push
```

**Option B (smaller repo):** Let HuggingFace re-ingest on startup
```bash
# Make sure chroma_db/ is in .gitignore
# Push only the new docs/ files
git add docs/
git commit -m "docs: add new articles"
git push
# HuggingFace will run ingest.py on startup (~15-30 min)
```

### If you changed dependencies

```bash
# Update requirements.txt
pip freeze > requirements.txt  # or edit manually

# Push — HuggingFace will rebuild the Docker image
git add requirements.txt
git commit -m "chore: update dependencies"
git push
```

---

## Code Style

- **Language:** All code, comments, prompts, and UI text in **English**
- **Python:** Follow PEP 8, use type hints where practical
- **Docstrings:** Use Google-style docstrings for functions
- **Formatting:** 4 spaces indentation, max line length ~100 chars
- **Naming:**
  - Functions: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
  - Files: `kebab-case.py` or `snake_case.py`

---

## Pull Request Guidelines

1. **One PR per feature/fix** — keep changes focused
2. **Describe what and why** — not just what you changed, but why
3. **Test before submitting** — run the manual testing checklist above
4. **Update docs** — if your change affects the README, update it
5. **Don't commit secrets** — never commit `.env`, API keys, or tokens
6. **Don't commit `chroma_db/`** — unless intentionally updating the vector store

### PR template

```markdown
## What does this PR do?

Brief description of the change.

## Why?

Context and motivation.

## Testing

- [ ] Tested semantic search mode
- [ ] Tested RAG chat mode
- [ ] Tested without API key (fallback)
- [ ] Tested with invalid API key
- [ ] Updated README if needed
```

---

## Roadmap

Potential improvements for contributors:

- [ ] **Incremental ingestion** — only process new/changed documents instead of full rebuild
- [ ] **PDF support** — extract text from PDF documents in `docs/`
- [ ] **Streaming responses** — stream LLM responses token by token
- [ ] **Conversation memory** — persist chat history across sessions
- [ ] **Admin panel** — web UI for managing documents without terminal
- [ ] **Analytics** — track most asked questions, search quality metrics
- [ ] **Authentication** — optional login for team deployments
- [ ] **Ollama support** — local LLM option for fully offline usage
- [ ] **Evaluation suite** — automated tests comparing answer quality across providers

---

## Questions?

Open an issue on GitHub or reach out to the maintainers.