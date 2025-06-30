import feedparser
import numpy as np
import random
from app.utils.news_keywords import NEWS_KEYWORDS
from app.services.openai import client

# In-memory storage (consider persisting this)
previous_embeddings = []

def embed_text(text: str) -> np.ndarray:
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return np.array(response.data[0].embedding)

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def is_duplicate(new_embedding: np.ndarray, threshold=0.85) -> bool:
    for prev_emb in previous_embeddings:
        if cosine_similarity(new_embedding, prev_emb) > threshold:
            return True
    return False

def from_feedparser(url: str, n: int) -> list[str]:
    articles = []
    feed = feedparser.parse(url)
    for entry in feed.entries:
        title = entry.title.strip()
        link = entry.link.strip()
        if any(kw in title.lower() for kw in NEWS_KEYWORDS):
            combined_text = f"{title} - {link}"
            emb = embed_text(combined_text)
            if not is_duplicate(emb):
                articles.append(combined_text)
                previous_embeddings.append(emb)
            if len(articles) >= n:
                break
    return articles

# Expanded + shuffled RSS sources
RSS_SOURCES = [
    "https://www.cnbcindonesia.com/tech/rss",
    "https://feed.liputan6.com/rss/tekno",
    "https://inet.detik.com/rss",                
    "https://www.merdeka.com/feed/teknologi",
]

def fetch_indo_news(n=1) -> list[str]:
    articles = []
    shuffled_sources = RSS_SOURCES[:]
    random.shuffle(shuffled_sources)

    for rss_url in shuffled_sources:
        articles.extend(from_feedparser(rss_url, n))

    return articles[:n * len(RSS_SOURCES)]
