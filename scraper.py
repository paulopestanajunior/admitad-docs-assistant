"""
Scraper for the Mitgo/Admitad Knowledge Base.
Downloads articles from ALL products (EN + RU) and saves as markdown.
"""

import os
import re
import sys
import time
import requests

# Force UTF-8 output to handle Cyrillic and other non-ASCII characters
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from markdownify import markdownify as md


DOCS_DIR = "docs"
DELAY_BETWEEN_REQUESTS = 1

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

EN_BASE = "https://support.mitgo.com"
RU_BASE = "https://support.admitad.ru"

# Each entry: section URL (H2 level), category (H1 product), language
SECTION_URLS = [
    # ── EN: Admitad Advertisers ───────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/general-information",           "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/affiliate-program-settings",    "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/technical-integration",         "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/tools_1",                       "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/working-with-publishers",       "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/finances",                      "category": "admitad-advertisers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/faq",                           "category": "admitad-advertisers", "language": "en"},

    # ── EN: Admitad Publishers ────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/getting-started",               "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/account-and-settings",          "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/ad-spaces",                     "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/affiliate-programs",            "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/CPC+pricing+model",             "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/affiliate-links-and-creatives", "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/tools",                         "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/admitad-extension",             "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/aliexpress",                    "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/reports-and-target-actions",    "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/finance-balance-payment-terms-and-methods", "category": "admitad-publishers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/tech-support",                  "category": "admitad-publishers",  "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/admitad-partner-network-glossary", "category": "admitad-publishers", "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/gdpr",                          "category": "admitad-publishers",  "language": "en"},

    # ── EN: TakeDeals ─────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/Getting+started.",              "category": "takedeals",           "language": "en"},

    # ── EN: Takeads ───────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/getting-started_1",             "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/account-and-settings_2",        "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/platforms",                     "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/take-link",                     "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/reports_1",                     "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/finance-and-payment-methods",   "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/Merchants",                     "category": "takeads",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/tech-support_1",                "category": "takeads",             "language": "en"},

    # ── EN: Mitgo ID ──────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/mitgo-id",                      "category": "mitgo-id",            "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/how-to-manage-mitgo-id-account","category": "mitgo-id",            "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/Ad+spaces",                     "category": "mitgo-id",            "language": "en"},

    # ── EN: Mobmio ────────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/getting-started_2",             "category": "mobmio",              "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/finance",                       "category": "mobmio",              "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/caps-and-mmp-links",            "category": "mobmio",              "language": "en"},

    # ── EN: Takefluence ───────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/creators",                      "category": "takefluence",         "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/advertisers",                   "category": "takefluence",         "language": "en"},

    # ── EN: Wallet ────────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/wallet",                        "category": "wallet",              "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/how-to-work-with-wallet",       "category": "wallet",              "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/tax-information-and-billing-details", "category": "wallet",        "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/how-to-withdraw-money-from-wallet", "category": "wallet",          "language": "en"},

    # ── EN: Mitgame ───────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/affiliates",                    "category": "mitgame",             "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/advertisers_1",                 "category": "mitgame",             "language": "en"},

    # ── EN: ConvertSocial ─────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/whats-first",                   "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/account-and-settings_1",        "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/working-with-social-media",     "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/working-with-brands",           "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/referral-links",                "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/reports",                       "category": "convertsocial",       "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/finance-balance-and-funds-withdrawal", "category": "convertsocial","language": "en"},

    # ── EN: TrendWeave ────────────────────────────────────────────────────────
    {"url": f"{EN_BASE}/knowledge-base/articles/getting_started",               "category": "trendweave",          "language": "en"},
    {"url": f"{EN_BASE}/knowledge-base/articles/Finance+TW",                    "category": "trendweave",          "language": "en"},

    # ── RU: Admitad Advertisers ───────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/general-information",           "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/affiliate-program-settings",    "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/technical-integration",         "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/tools_1",                       "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/working-with-publishers",       "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/finances",                      "category": "admitad-advertisers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/faq",                           "category": "admitad-advertisers", "language": "ru"},

    # ── RU: Admitad Publishers ────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/getting-started",               "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/account-and-settings",          "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/ad-spaces",                     "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/affiliate-programs",            "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C+%D0%BE%D0%BF%D0%BB%D0%B0%D1%82%D1%8B+CPC", "category": "admitad-publishers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/affiliate-links-and-creatives", "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/tools",                         "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/admitad-extension",             "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/aliexpress",                    "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/reports-and-target-actions",    "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/finance-balance-payment-terms-and-methods", "category": "admitad-publishers", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/tech-support",                  "category": "admitad-publishers",  "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/admitad-partner-network-glossary", "category": "admitad-publishers", "language": "ru"},

    # ── RU: Mitgo ID ──────────────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/mitgo-id",                      "category": "mitgo-id",            "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/how-to-manage-mitgo-id-account","category": "mitgo-id",            "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/Ad+spaces",                     "category": "mitgo-id",            "language": "ru"},

    # ── RU: Wallet ────────────────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/wallet",                        "category": "wallet",              "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/how-to-work-with-wallet",       "category": "wallet",              "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/tax-information-and-billing-details", "category": "wallet",        "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/how-to-withdraw-money-from-wallet", "category": "wallet",          "language": "ru"},

    # ── RU: Affilead ──────────────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BE+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B", "category": "affilead", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/%D0%A4%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D1%8B",                                   "category": "affilead", "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B",          "category": "affilead", "language": "ru"},

    # ── RU: Telerev ───────────────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BE+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B+%D0%B2+Telerev", "category": "telerev", "language": "ru"},

    # ── RU: Takprodam ─────────────────────────────────────────────────────────
    {"url": f"{RU_BASE}/knowledge-base/articles/takprodam-for-publisher",       "category": "takprodam",           "language": "ru"},
    {"url": f"{RU_BASE}/knowledge-base/articles/takprodam-for-seller",          "category": "takprodam",           "language": "ru"},
]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text[:80]


def get_article_links_from_section(section_url: str) -> list[dict]:
    """Extract individual article links from a section page."""
    print(f"  Fetching: {section_url}")
    try:
        response = requests.get(section_url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"  Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")
    articles = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        full_url = urljoin(section_url, href)

        # Individual articles use /knowledge-base/article/ (singular)
        # Sections use /knowledge-base/articles/ (plural)
        if "/knowledge-base/article/" in full_url:
            title = link.get_text(strip=True)
            if title and len(title) > 3:
                articles.append({"url": full_url, "title": title})

    # Remove duplicates
    seen = set()
    unique = []
    for a in articles:
        if a["url"] not in seen:
            seen.add(a["url"])
            unique.append(a)

    return unique


def scrape_article(url: str) -> dict | None:
    """Scrape an individual article page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"    Error accessing {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, "lxml")

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
    title = title_el.get_text(strip=True) if title_el else "untitled"

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


def save_article(article: dict, section_name: str, category: str, language: str) -> str:
    filename = f"{language}_{slugify(article['title'])}.md"
    filepath = os.path.join(DOCS_DIR, filename)

    content = f"""---
title: {article['title']}
category: {category}
section: {section_name}
language: {language}
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

    # Remove old docs without language prefix to avoid duplicates in the index
    removed = 0
    for fname in os.listdir(DOCS_DIR):
        if fname.endswith(".md") and not fname.startswith(("en_", "ru_")):
            os.remove(os.path.join(DOCS_DIR, fname))
            removed += 1
    if removed:
        print(f"Removed {removed} old unprefixed docs\n")

    # 1. Collect links from all sections
    all_articles = []
    seen_urls = set()

    print("=== Collecting articles from the full Knowledge Base ===\n")

    for section_entry in SECTION_URLS:
        section_url = section_entry["url"]
        category = section_entry["category"]
        language = section_entry["language"]
        section_name = section_url.split("/")[-1]

        articles = get_article_links_from_section(section_url)

        for a in articles:
            if a["url"] not in seen_urls:
                seen_urls.add(a["url"])
                a["section"] = section_name
                a["category"] = category
                a["language"] = language
                all_articles.append(a)

        print(f"  [{language.upper()}] [{category}] {section_name} -> {len(articles)} articles\n")
        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"Total unique articles: {len(all_articles)}\n")

    if not all_articles:
        print("No articles found. Check the section URLs.")
        return

    # 2. Scrape and save each article
    saved = 0
    for i, article_info in enumerate(all_articles, 1):
        print(f"[{i}/{len(all_articles)}] {article_info['title'][:60]}...")

        article = scrape_article(article_info["url"])
        if article:
            filepath = save_article(
                article,
                article_info["section"],
                article_info["category"],
                article_info["language"],
            )
            print(f"    Saved: {filepath}")
            saved += 1

        time.sleep(DELAY_BETWEEN_REQUESTS)

    print(f"\nDone! {saved} articles saved to '{DOCS_DIR}/'")


if __name__ == "__main__":
    main()
