"""
Camada de abstração multi-provider para LLMs.
Suporta: Groq, OpenAI, Anthropic, Google Gemini, Ollama (local).

Detecta automaticamente quais providers estão disponíveis
com base nas API keys configuradas no .env
"""

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from dotenv import load_dotenv

load_dotenv()


# ── Tipos ──────────────────────────────────────────────────────

@dataclass
class LLMResponse:
    """Resposta padronizada de qualquer provider."""
    text: str
    model: str
    provider: str
    usage: dict = field(default_factory=dict)  # tokens usados (se disponível)


class LLMProvider(ABC):
    """Interface base para todos os providers."""
    
    name: str
    model: str
    
    @abstractmethod
    def complete(
        self,
        messages: list[dict],
        temperature: float = 0.1,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        """Gera uma completion a partir de mensagens."""
        pass
    
    @abstractmethod
    def classify(self, system_prompt: str, query: str) -> str:
        """Classificação rápida (poucas tokens). Retorna texto curto."""
        pass
    
    def __repr__(self):
        return f"{self.name} ({self.model})"


# ── Groq ───────────────────────────────────────────────────────

class GroqProvider(LLMProvider):
    name = "Groq"
    
    def __init__(self, api_key: str, model: str = "llama-3.3-70b-versatile"):
        from groq import Groq
        self.model = model
        self.client = Groq(api_key=api_key)
    
    def complete(self, messages, temperature=0.1, max_tokens=1024) -> LLMResponse:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return LLMResponse(
            text=completion.choices[0].message.content,
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": getattr(completion.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(completion.usage, "completion_tokens", 0),
            }
        )
    
    def classify(self, system_prompt: str, query: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0,
            max_tokens=10,
        )
        return completion.choices[0].message.content.strip()


# ── OpenAI ─────────────────────────────────────────────────────

class OpenAIProvider(LLMProvider):
    name = "OpenAI"
    
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        from openai import OpenAI
        self.model = model
        self.client = OpenAI(api_key=api_key)
    
    def complete(self, messages, temperature=0.1, max_tokens=1024) -> LLMResponse:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return LLMResponse(
            text=completion.choices[0].message.content,
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": getattr(completion.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(completion.usage, "completion_tokens", 0),
            }
        )
    
    def classify(self, system_prompt: str, query: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0,
            max_tokens=10,
        )
        return completion.choices[0].message.content.strip()


# ── Anthropic ──────────────────────────────────────────────────

class AnthropicProvider(LLMProvider):
    name = "Anthropic"
    
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        from anthropic import Anthropic
        self.model = model
        self.client = Anthropic(api_key=api_key)
    
    def complete(self, messages, temperature=0.1, max_tokens=1024) -> LLMResponse:
        # Anthropic usa system separado das messages
        system_msg = ""
        filtered_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_msg = msg["content"]
            else:
                filtered_messages.append(msg)
        
        response = self.client.messages.create(
            model=self.model,
            system=system_msg,
            messages=filtered_messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return LLMResponse(
            text=response.content[0].text,
            model=self.model,
            provider=self.name,
            usage={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            }
        )
    
    def classify(self, system_prompt: str, query: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=[{"role": "user", "content": query}],
            temperature=0,
            max_tokens=10,
        )
        return response.content[0].text.strip()


# ── Google Gemini ──────────────────────────────────────────────

class GeminiProvider(LLMProvider):
    name = "Google"
    
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        from google import genai
        self.model = model
        self.client = genai.Client(api_key=api_key)
    
    def complete(self, messages, temperature=0.1, max_tokens=1024) -> LLMResponse:
        # Converte formato OpenAI → Gemini
        system_instruction = ""
        contents = []
        for msg in messages:
            if msg["role"] == "system":
                system_instruction = msg["content"]
            elif msg["role"] == "user":
                contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
            elif msg["role"] == "assistant":
                contents.append({"role": "model", "parts": [{"text": msg["content"]}]})
        
        from google.genai import types
        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=temperature,
                max_output_tokens=max_tokens,
            ),
        )
        return LLMResponse(
            text=response.text,
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": getattr(response.usage_metadata, "prompt_token_count", 0),
                "completion_tokens": getattr(response.usage_metadata, "candidates_token_count", 0),
            }
        )
    
    def classify(self, system_prompt: str, query: str) -> str:
        from google.genai import types
        response = self.client.models.generate_content(
            model=self.model,
            contents=[{"role": "user", "parts": [{"text": query}]}],
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0,
                max_output_tokens=10,
            ),
        )
        return response.text.strip()


# ── Ollama (local) ─────────────────────────────────────────────

class OllamaProvider(LLMProvider):
    name = "Ollama"
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.1"):
        import httpx
        self.model = model
        self.base_url = base_url
        self.http = httpx
        # Testa se Ollama está rodando
        try:
            resp = httpx.get(f"{base_url}/api/tags", timeout=5)
            resp.raise_for_status()
        except Exception:
            raise ConnectionError(f"Ollama não encontrado em {base_url}")
    
    def complete(self, messages, temperature=0.1, max_tokens=1024) -> LLMResponse:
        response = self.http.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                }
            },
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        return LLMResponse(
            text=data["message"]["content"],
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": data.get("prompt_eval_count", 0),
                "completion_tokens": data.get("eval_count", 0),
            }
        )
    
    def classify(self, system_prompt: str, query: str) -> str:
        response = self.http.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                "stream": False,
                "options": {"temperature": 0, "num_predict": 10}
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()["message"]["content"].strip()


# ── Registry: detecta providers disponíveis ────────────────────

@dataclass
class ProviderRegistry:
    """Gerencia todos os providers disponíveis."""
    providers: dict[str, LLMProvider] = field(default_factory=dict)
    default: str | None = None
    
    def add(self, provider: LLMProvider):
        self.providers[provider.name] = provider
        if self.default is None:
            self.default = provider.name
    
    def get(self, name: str | None = None) -> LLMProvider | None:
        if name:
            return self.providers.get(name)
        if self.default:
            return self.providers.get(self.default)
        return None
    
    def list_available(self) -> list[dict]:
        return [
            {"name": p.name, "model": p.model}
            for p in self.providers.values()
        ]
    
    def is_available(self) -> bool:
        return len(self.providers) > 0


def discover_providers() -> ProviderRegistry:
    """
    Detecta automaticamente quais providers estão disponíveis
    com base nas API keys no .env e serviços locais rodando.
    
    Ordem de prioridade: Groq > OpenAI > Anthropic > Google > Ollama
    (Groq primeiro porque é gratuito e rápido)
    """
    registry = ProviderRegistry()
    
    # Groq (gratuito, prioridade máxima)
    groq_key = os.getenv("GROQ_API_KEY", "")
    if groq_key and groq_key != "your_groq_api_key_here":
        try:
            provider = GroqProvider(api_key=groq_key)
            registry.add(provider)
            print(f"  ✓ Groq: {provider.model}")
        except Exception as e:
            print(f"  ✗ Groq: erro ao inicializar — {e}")
    
    # OpenAI
    openai_key = os.getenv("OPENAI_API_KEY", "")
    if openai_key and openai_key != "your_openai_api_key_here":
        try:
            model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
            provider = OpenAIProvider(api_key=openai_key, model=model)
            registry.add(provider)
            print(f"  ✓ OpenAI: {provider.model}")
        except Exception as e:
            print(f"  ✗ OpenAI: erro ao inicializar — {e}")
    
    # Anthropic
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
    if anthropic_key and anthropic_key != "your_anthropic_api_key_here":
        try:
            model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
            provider = AnthropicProvider(api_key=anthropic_key, model=model)
            registry.add(provider)
            print(f"  ✓ Anthropic: {provider.model}")
        except Exception as e:
            print(f"  ✗ Anthropic: erro ao inicializar — {e}")
    
    # Google Gemini
    google_key = os.getenv("GOOGLE_API_KEY", "")
    if google_key and google_key != "your_google_api_key_here":
        try:
            model = os.getenv("GOOGLE_MODEL", "gemini-2.0-flash")
            provider = GeminiProvider(api_key=google_key, model=model)
            registry.add(provider)
            print(f"  ✓ Google: {provider.model}")
        except Exception as e:
            print(f"  ✗ Google: erro ao inicializar — {e}")
    
    # Ollama (local — tenta conectar)
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.1")
    if os.getenv("OLLAMA_ENABLED", "false").lower() == "true":
        try:
            provider = OllamaProvider(base_url=ollama_url, model=ollama_model)
            registry.add(provider)
            print(f"  ✓ Ollama: {provider.model} (local)")
        except Exception as e:
            print(f"  ✗ Ollama: não disponível — {e}")
    
    if not registry.is_available():
        print("  ⚠ Nenhum provider LLM disponível — modo chat desabilitado")
    
    return registry
