from app.domain.entities import NewsPost
from app.services.summarizer import summarize_news
from app.services.twitter import post_to_twitter
from app.sources.source_aggregator import get_top_news

def run_daily_post(limit=3, region=None):
    articles = get_top_news(region=region)[:limit]

    for raw in articles:
        title, url = raw.split(" - ", 1)
        summary = summarize_news(f"{title} {url}")
        post_to_twitter(f"📰 {summary}\n🔗 {url}")
