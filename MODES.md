# 🔍 Query Modes — How They Work

Admitad Docs Assistant offers **4 query modes** that control how your question is processed. Choose the mode that best fits your needs.

---

## Overview

| Mode | Classifier | Response Type | LLM Calls | Best For |
|---|---|---|---|---|
| 🔍 **Search Only** | None | Raw document excerpts | 0 | Quick lookups, no API key needed |
| ⚡ **Auto (Smart)** | Heuristic (free) | Search or AI answer | 0–1 | Balanced cost and quality |
| 🧠 **Auto (LLM)** | LLM classifies | Search or AI answer | 1–2 | Maximum routing accuracy |
| 💬 **Always Chat** | None | AI-generated answer | 1 | Always want a full explanation |

---

## Detailed Comparison

### Same question, 4 different modes

**Question:** *"What documents are required for cooperation with Admitad?"*

---

### 🔍 Search Only

**What happens:** The system finds the most relevant document chunks using semantic similarity and returns them directly. No LLM is involved at any point.

**Response:**

```
📄 documents-required-for-cooperation-with-admitad.md · Section: main
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
To launch an affiliate program, you need to establish a partnership
with Admitad. This is necessary to comply with the tax laws of your
country.

For that, provide the following to Admitad:
* Supporting documents
* Your company's payment details

Send all information to advsupport@admitad.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
relevance: 100%

📄 admitad-for-advertisers-the-basics.md · Section: Procedure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Documents required for cooperation with Admitad
- How to sign up for Admitad as an advertiser
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
relevance: 95%
```

**LLM calls:** 0
**Speed:** ~200ms
**When to use:** You just want to find where the information is. You're comfortable reading the raw documentation.

---

### ⚡ Auto (Smart)

**What happens:** A free heuristic analyzes your question using keyword patterns and question length. For this simple factual question, it routes to **Search**. For a question like *"What is the difference between..."*, it would route to **Chat**.

**Heuristic rules:**
- Contains "why", "explain", "difference", "compare", "how does" → **Chat**
- Question has 15+ words → **Chat**
- Has conversation history → **Chat**
- Otherwise → **Search**

**Response for this question:** Same as Search Only (heuristic detected it's a simple factual question).

**Response for** *"Explain the difference between tracking code and postback integration"***:**

```
Chat RAG · groq (llama-3.3-70b-versatile)
Route: Pattern 'explain' detected → needs explanation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The main difference between tracking code integration and postback
integration lies in how target action data is transmitted to Admitad:

**Tracking code** places a JavaScript snippet on your website that
sends data from the user's browser to Admitad. [Source 1]

**Postback integration** sends data directly from your server to
Admitad's server, making it more secure and unaffected by ad blockers
or browser privacy settings. [Source 2]

Postback is generally recommended as the more reliable method, though
it requires server-side access. [Source 3]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📎 Sources: 3 documents cited
```

**LLM calls:** 0 for search, 1 for chat
**Speed:** ~200ms (search) or ~2-3s (chat)
**When to use:** You want the system to be smart about when to use the LLM. Best balance between cost and quality.

---

### 🧠 Auto (LLM)

**What happens:** The LLM itself reads your question and decides whether it needs a simple search or a full AI-generated answer. More accurate routing than heuristics, but costs an extra LLM call.

**Response for this question:** The LLM classifier returns `SEARCH` (it recognizes this is a factual lookup), so the response is the same as Search Only.

**When the LLM classifier shines:**

Questions like *"Can I use postback if my website runs on Shopify?"* — the heuristic would route to Search (no trigger words), but the LLM classifier correctly identifies this needs interpretation from multiple sources and routes to Chat.

**LLM calls:** 1 (classifier) + 0 or 1 (answer) = 1–2 total
**Speed:** ~1s (classifier) + ~200ms or ~2-3s (answer)
**When to use:** You want maximum accuracy in routing and don't mind the extra LLM call.

---

### 💬 Always Chat

**What happens:** Every question goes through the full RAG pipeline. The system retrieves relevant chunks, sends them to the LLM, and generates a natural language answer with citations. No classification step.

**Response:**

```
Chat RAG · groq (llama-3.3-70b-versatile)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
To cooperate with Admitad, you need to provide two things:

1. **Supporting documents** — such as a certificate of residence,
   which must be valid at the time of accepting the Admitad offer
   and issued no earlier than one year before. If the certificate
   only contains a registration number, you'll also need a document
   verifying your company name. [Source 1]

2. **Your company's payment details** [Source 1]

Send all required information to advsupport@admitad.com. [Source 1]

Note: The specific documents may vary depending on the country
where your company is registered. [Source 2]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📎 Sources: 2 documents cited
```

**LLM calls:** 1 (always)
**Speed:** ~2-3s
**When to use:** You always want a polished, interpreted answer. You don't mind using an LLM call for every question, even simple ones.

---

## Choosing the Right Mode

```
Do you have an API key?
├── No  → 🔍 Search Only (only option)
│
├── Yes → Do you want to minimize LLM usage?
│         ├── Yes → ⚡ Auto (Smart)
│         │         Free classification, LLM only when needed
│         │
│         └── No  → Do you want maximum routing accuracy?
│                   ├── Yes → 🧠 Auto (LLM)
│                   │         LLM classifies + LLM answers
│                   │
│                   └── No  → 💬 Always Chat
│                             Every question gets an AI answer
```

---

## Cost Comparison (per 100 questions)

Assuming 60% of questions are simple (search) and 40% are complex (chat):

| Mode | LLM Calls | Estimated Cost (Groq free tier) |
|---|---|---|
| 🔍 Search Only | 0 | Free |
| ⚡ Auto (Smart) | ~40 | Free (well within limits) |
| 🧠 Auto (LLM) | ~140 | Free (may hit rate limits) |
| 💬 Always Chat | 100 | Free (may hit rate limits) |

> Groq's free tier allows ~30 requests/minute. For personal or small team use, all modes are effectively free.

---

## How to Change Modes

In the Streamlit interface, look for the **Query Mode** selector in the sidebar. You can switch modes at any time — it takes effect on the next question.

The mode selection is per-session and does not affect other users.