import feedparser

def fetch_techinasia_rss(n=2):
    feed = feedparser.parse("https://id.techinasia.com/feed")
    articles = []
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link.strip()
        if any(kw in title.lower() for kw in ["startup", "program", "korporat", "investasi", "teknologi"]):
            articles.append(f"{title} - {link}")
        if len(articles) >= n:
            break
    return articles