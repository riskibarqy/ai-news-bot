import feedparser
import requests

def fetch_hackernews(n=1):
    url = "https://hn.algolia.com/api/v1/search?tags=front_page"
    res = requests.get(url).json()
    articles = []

    for hit in res["hits"]:
        title = hit.get("title", "").strip()
        link = hit.get("url", "")
        if title and link:
            articles.append(f"{title} - {link}")
        if len(articles) >= n:
            break
    return articles


def fetch_devto(n=1):
    feed = feedparser.parse("https://dev.to/feed")
    articles = []
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link.strip()
        if any(kw in title.lower() for kw in ["startup", "programming", "ai", "dev", "corporate"]):
            articles.append(f"{title} - {link}")
        if len(articles) >= n:
            break
    return articles


def fetch_techcrunch(n=1):
    feed = feedparser.parse("https://techcrunch.com/feed/")
    articles = []
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link.strip()
        if any(kw in title.lower() for kw in ["startup", "ai", "corporate", "programmer", "developer"]):
            articles.append(f"{title} - {link}")
        if len(articles) >= n:
            break
    return articles


def fetch_global_news(n=1):
    # Pull 1 from each (or tweak later to get top 3 regardless of source)
    return fetch_hackernews(n) + fetch_devto(n) + fetch_techcrunch(n)
