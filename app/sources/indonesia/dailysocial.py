import feedparser

def fetch_dailysocial(n=2):
    rss_url = "https://news.dailysocial.id/"
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link.strip()

        # Filter only relevant topics (can be adjusted)
        if any(kw in title.lower() for kw in ["startup", "teknologi", "investasi", "programmer", "fintech", "korporasi"]):
            articles.append(f"{title} - {link}")
        if len(articles) >= n:
            break
    return articles
