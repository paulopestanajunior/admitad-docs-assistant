"""
Scraper para documentação Admitad Advertisers.
Baixa APENAS os artigos da seção "Admitad Advertisers" e salva como markdown.
"""

import os
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from markdownify import markdownify as md


DOCS_DIR = "docs"
DELAY_BETWEEN_REQUESTS = 1

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# URLs das sub-seções de Admitad Advertisers
SECTION_URLS = [
    "https://support.mitgo.com/knowledge-base/articles/general-information",
    "https://support.mitgo.com/knowledge-base/articles/affiliate-program-settings",
    "https://support.mitgo.com/knowledge-base/articles/technical-integration",
    "https://support.mitgo.com/knowledge-base/articles/tools_1",
    "https://support.mitgo.com/knowledge-base/articles/working-with-publishers",
    "https://support.mitgo.com/knowledge-base/articles/finances",
    "https://support.mitgo.com/knowledge-base/articles/faq",
]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:80]


def get_article_links_from_section(section_url: str) -> list[dict]:
    """Extrai links de artigos individuais de uma página de seção."""
    print(f"  Buscando em: {section_url}")
    try:
        response = requests.get(section_url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"  Erro: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    articles = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        full_url = urljoin(section_url, href)

        # Filtra apenas links de artigos individuais (não seções)
        # Artigos individuais usam /knowledge-base/article/ (singular)
        # Seções usam /knowledge-base/articles/ (plural)
        if "/knowledge-base/article/" in full_url:
            title = link.get_text(strip=True)
            if title and len(title) > 3:
                articles.append({"url": full_url, "title": title})

    # Remove duplicatas
    seen = set()
    unique = []
    for a in articles:
        if a["url"] not in seen:
            seen.add(a["url"])
            unique.append(a)

    return unique


def scrape_article(url: str) -> dict | None:
    """Faz scraping de um artigo individual."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"    Erro ao acessar {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "lxml")

    # Tenta encontrar o conteúdo principal
    content_selectors = [
        ".article-content",
        ".article-body",
        "article",
        ".knowledge-base-article",
        ".content-body",
        "main",
    ]

    content_element = None
    for selector in content_selectors:
        content_element = soup.select_one(selector)
        if content_element:
            break

    if not content_element:
        content_element = soup.find("body")
        if content_element:
            for tag in content_element.find_all(["nav", "footer", "header", "script", "style", "aside"]):
                tag.decompose()

    if not content_element:
        return None

    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(strip=True) if title_el else "sem-titulo"

    markdown_content = md(
        str(content_element),
        heading_style="ATX",
        bullets="-",
        strip=["img", "script", "style"]
    )

    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content).strip()

    if len(markdown_content) < 50:
        return None

    return {"title": title, "content": markdown_content, "url": url}


def save_article(article: dict, section_name: str) -> str:
    filename = slugify(article["title"]) + ".md"
    filepath = os.path.join(DOCS_DIR, filename)

    content = f"""---
title: {article['title']}
section: {section_name}
source: {article['url']}
---

# {article['title']}

{article['content']}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)

    # 1. Coleta links de todas as sub-seções
    all_articles = []
    seen_urls = set()

    print("=== Coletando artigos de Admitad Advertisers ===\n")

    for section_url in SECTION_URLS:
        section_name = section_url.split("/")[-1]
        articles = get_article_links_from_section(section_url)

        for a in articles:
            if a["url"] not in seen_urls:
                seen_urls.add(a["url"])
                a["section"] = section_name
                all_articles.append(a)

        print(f"  → {len(articles)} artigos encontrados\n")
        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"Total de artigos únicos: {len(all_articles)}\n")

    if not all_articles:
        print("Nenhum artigo encontrado. Verifique as URLs das seções.")
        return

    # 2. Faz scraping de cada artigo
    saved = 0
    for i, article_info in enumerate(all_articles, 1):
        print(f"[{i}/{len(all_articles)}] {article_info['title'][:60]}...")

        article = scrape_article(article_info["url"])
        if article:
            filepath = save_article(article, article_info["section"])
            print(f"    Salvo: {filepath}")
            saved += 1

        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\nConcluído! {saved} artigos salvos em '{DOCS_DIR}/'")


if __name__ == "__main__":
    main()