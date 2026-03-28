"""
Streamlit Frontend — Unified smart interface with 4 query modes.
Users can provide their own API key and choose the query mode.
"""

import streamlit as st
import requests

API_URL = "http://localhost:8000"

# Mode definitions
MODES = {
    "search_only": {
        "label": "🔍 Search Only",
        "description": "Returns raw document excerpts. No LLM, no cost.",
        "needs_key": False,
    },
    "auto_smart": {
        "label": "⚡ Auto (Smart)",
        "description": "Free heuristic decides: simple → search, complex → AI answer.",
        "needs_key": True,
    },
    "auto_llm": {
        "label": "🧠 Auto (LLM)",
        "description": "LLM classifies your question first, then routes. Most accurate.",
        "needs_key": True,
    },
    "always_chat": {
        "label": "💬 Always Chat",
        "description": "Every question gets a full AI-generated answer with citations.",
        "needs_key": True,
    },
}


# ── Config ─────────────────────────────────────────────────────

st.set_page_config(
    page_title="Admitad Docs Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .result-card {
        background: #111118;
        border: 1px solid #1e1e2e;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .result-source {
        font-family: 'Courier New', monospace;
        font-size: 0.75rem;
        color: #818cf8;
        margin-bottom: 0.5rem;
    }
    .result-text {
        color: #c4c4d0;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    .result-score {
        color: #34d399;
        font-size: 0.75rem;
        font-family: 'Courier New', monospace;
        margin-top: 0.5rem;
    }
    .chat-answer {
        background: #111118;
        border: 1px solid #1e1e2e;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        color: #e0e0e8;
        line-height: 1.7;
    }
    .mode-badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .mode-search {
        background: rgba(99, 102, 241, 0.15);
        color: #818cf8;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    .mode-chat {
        background: rgba(52, 211, 153, 0.15);
        color: #34d399;
        border: 1px solid rgba(52, 211, 153, 0.3);
    }
    .route-info {
        font-size: 0.72rem;
        color: #4b5563;
        font-family: 'Courier New', monospace;
        font-style: italic;
    }
    .key-ok { color: #34d399; font-size: 0.8rem; }
    .key-none { color: #f59e0b; font-size: 0.8rem; }
    .mode-cost {
        font-size: 0.7rem;
        color: #6b7280;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)


# ── API helpers ────────────────────────────────────────────────

def check_api() -> dict | None:
    try:
        return requests.get(f"{API_URL}/health", timeout=5).json()
    except requests.ConnectionError:
        return None


def do_ask(query: str, history: list, api_key: str = "", provider: str = "", mode: str = "auto_smart") -> dict | None:
    try:
        payload = {
            "query": query,
            "history": history,
            "mode": mode,
        }
        if api_key:
            payload["api_key"] = api_key
        if provider:
            payload["provider"] = provider

        response = requests.post(f"{API_URL}/ask", json=payload, timeout=60)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def render_result(result: dict):
    source = result.get("filename", "")
    section = result.get("section", "")
    label = f"{source} · {section}" if section else source
    score = result.get("relevance_score", 0)
    text = result.get("text", "")

    st.markdown(f"""
    <div class="result-card">
        <div class="result-source">📄 {label}</div>
        <div class="result-text">{text[:500]}{'...' if len(text) > 500 else ''}</div>
        <div class="result-score">relevance: {score:.0f}%</div>
    </div>
    """, unsafe_allow_html=True)

    url = result.get("source_url", "")
    if url:
        st.caption(f"[View original article]({url})")


def detect_provider(api_key: str) -> str:
    key = api_key.strip()
    if key.startswith("gsk_"):
        return "groq"
    elif key.startswith("sk-ant-"):
        return "anthropic"
    elif key.startswith("sk-"):
        return "openai"
    elif key.startswith("AI"):
        return "google"
    return "groq"


# ── Session state ──────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []
if "user_api_key" not in st.session_state:
    st.session_state.user_api_key = ""
if "query_mode" not in st.session_state:
    st.session_state.query_mode = "auto_smart"


# ── Backend check ──────────────────────────────────────────────

health = check_api()

if not health:
    st.error(
        "⚠️ Backend is not running. "
        "Run `uvicorn api:app --reload --port 8000` in another terminal."
    )
    st.stop()


# ── Sidebar ────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("### ⚙️ Settings")

    # ── Query Mode ─────────────────────────────────────────────
    st.divider()
    st.markdown("**📋 Query Mode**")

    mode_keys = list(MODES.keys())
    mode_labels = [MODES[k]["label"] for k in mode_keys]
    current_mode_idx = mode_keys.index(st.session_state.query_mode) if st.session_state.query_mode in mode_keys else 1

    selected_mode_label = st.radio(
        "How should questions be processed?",
        mode_labels,
        index=current_mode_idx,
        label_visibility="collapsed",
    )
    selected_mode = mode_keys[mode_labels.index(selected_mode_label)]
    st.session_state.query_mode = selected_mode

    # Show description and cost
    mode_info = MODES[selected_mode]
    st.caption(mode_info["description"])

    cost_map = {
        "search_only": "0 LLM calls per question",
        "auto_smart": "0–1 LLM calls per question",
        "auto_llm": "1–2 LLM calls per question",
        "always_chat": "1 LLM call per question",
    }
    st.markdown(f'<p class="mode-cost">Cost: {cost_map[selected_mode]}</p>', unsafe_allow_html=True)

    # ── API Key ────────────────────────────────────────────────
    st.divider()
    st.markdown("**🔑 API Key**")

    needs_key = mode_info["needs_key"]

    if needs_key:
        st.caption("Required for this mode. Paste your key below.")
    else:
        st.caption("Not required for Search Only mode.")

    user_key = st.text_input(
        "API Key",
        value=st.session_state.user_api_key,
        type="password",
        placeholder="gsk_... or sk-... or sk-ant-...",
        label_visibility="collapsed",
    )

    if user_key != st.session_state.user_api_key:
        st.session_state.user_api_key = user_key

    if user_key:
        provider = detect_provider(user_key)
        st.markdown(f'<p class="key-ok">✅ Detected: <strong>{provider}</strong></p>', unsafe_allow_html=True)
    elif needs_key:
        st.markdown('<p class="key-none">⚠️ No key — will fall back to Search Only</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="key-ok">✅ No key needed for this mode</p>', unsafe_allow_html=True)

    # ── Provider links ─────────────────────────────────────────
    st.divider()
    st.markdown("**Get a free API key:**")
    st.caption("[→ Groq — free, recommended](https://console.groq.com/keys)")
    st.caption("[→ Google AI Studio — free tier](https://aistudio.google.com/apikey)")

    st.divider()
    st.markdown("**Supported providers:**")
    st.caption("🟢 **Groq** — `gsk_...`")
    st.caption("🔵 **OpenAI** — `sk-...`")
    st.caption("🟠 **Anthropic** — `sk-ant-...`")
    st.caption("🔴 **Google** — `AI...`")

    # ── System info ────────────────────────────────────────────
    st.divider()
    st.caption(f"📦 {health.get('chunks_loaded', 0)} chunks indexed")
    st.caption(f"📋 Mode: {MODES[selected_mode]['label']}")

    st.divider()
    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()


# ── Main ───────────────────────────────────────────────────────

st.markdown("## 🔍 Admitad Docs Assistant")

# Subtitle based on mode
mode_subtitle = {
    "search_only": "Mode: **Search Only** — returns document excerpts, no AI generation.",
    "auto_smart": "Mode: **Auto (Smart)** — heuristic decides between search and AI answer.",
    "auto_llm": "Mode: **Auto (LLM)** — LLM classifier picks the best route for each question.",
    "always_chat": "Mode: **Always Chat** — every question gets a full AI-generated answer.",
}
st.caption(mode_subtitle[selected_mode])

if needs_key and not user_key:
    st.info("💡 This mode requires an API key. Add one in the sidebar, or switch to **Search Only** mode.")

st.write("")

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            mode = msg.get("mode", "search")
            if mode == "chat":
                provider_info = ""
                if msg.get("provider_used"):
                    provider_info = f" · {msg['provider_used']} ({msg.get('model_used', '')})"
                st.markdown(
                    f'<span class="mode-badge mode-chat">Chat RAG{provider_info}</span>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<span class="mode-badge mode-search">Semantic Search</span>',
                    unsafe_allow_html=True
                )

            if msg.get("reason"):
                st.markdown(f'<p class="route-info">{msg["reason"]}</p>', unsafe_allow_html=True)

            if msg.get("answer"):
                st.markdown(
                    f'<div class="chat-answer">{msg["answer"]}</div>',
                    unsafe_allow_html=True
                )

            results = msg.get("results", [])
            if results:
                label = "📎 Sources" if msg.get("answer") else "📎 Results"
                with st.expander(label, expanded=not msg.get("answer")):
                    for r in results:
                        render_result(r)
        else:
            st.write(msg["content"])


# Input
if query := st.chat_input("Ask a question about Admitad documentation..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing your question..."):
            provider = detect_provider(user_key) if user_key else ""
            result = do_ask(
                query,
                st.session_state.history,
                user_key,
                provider,
                selected_mode
            )

        if result:
            mode = result.get("mode", "search")
            reason = result.get("reason", "")
            answer = result.get("answer")
            results = result.get("results", [])
            provider_used = result.get("provider_used", "")
            model_used = result.get("model_used", "")

            if mode == "chat":
                provider_info = f" · {provider_used} ({model_used})" if provider_used else ""
                st.markdown(
                    f'<span class="mode-badge mode-chat">Chat RAG{provider_info}</span>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    '<span class="mode-badge mode-search">Semantic Search</span>',
                    unsafe_allow_html=True
                )

            st.markdown(f'<p class="route-info">{reason}</p>', unsafe_allow_html=True)

            if answer:
                st.markdown(
                    f'<div class="chat-answer">{answer}</div>',
                    unsafe_allow_html=True
                )

            if results:
                label = "📎 Sources" if answer else "📎 Results"
                with st.expander(label, expanded=not answer):
                    for r in results:
                        render_result(r)

            st.session_state.messages.append({
                "role": "assistant",
                "mode": mode,
                "reason": reason,
                "answer": answer,
                "results": results,
                "provider_used": provider_used,
                "model_used": model_used,
            })
            st.session_state.history.append({"role": "user", "content": query})
            if answer:
                st.session_state.history.append({"role": "assistant", "content": answer})