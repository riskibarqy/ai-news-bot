import requests
import time
from app.services.summarizer import summarize_news
from app.services.twitter import post_to_twitter
from app.sources.source_aggregator import get_top_news

SHORTENER_API = "https://snax-url-shortener.fly.dev/public/shorten"
SHORTENER_REDIRECT_BASE = "https://snax-url-shortener.fly.dev/public/r/"

def shorten_url(long_url: str) -> str:
    try:
        res = requests.post(
            SHORTENER_API,
            json={"url": long_url},
            timeout=5
        )
        res.raise_for_status()
        data = res.json()
        short_code = data.get("data", {}).get("shortCode")
        if short_code:
            return f"{SHORTENER_REDIRECT_BASE}{short_code}"
        else:
            print("[Shortener] No shortCode found, using original URL.")
            return long_url
    except Exception as e:
        print(f"[Shortener Error] {e}")
        return long_url

def run_daily_post(limit=3, region=None):
    articles = get_top_news(region=region)[:limit]

    for raw in articles:
        title, url = raw.split(" - ", 1)
        summary = summarize_news(f"{title} {url}")
        short_url = shorten_url(url)
        tweet_text = f"{summary}\n{short_url}"

        # Retry logic
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                post_to_twitter(tweet_text)
                break  # ✅ Success, exit retry loop
            except Exception as e:
                print(f"❌ Attempt {attempt} failed: {e}")
                if attempt < max_retries:
                    time.sleep(2 ** attempt)  # ⏳ Exponential backoff: 2s, 4s, 8s
                else:
                    print("❌ All retry attempts failed. Skipping tweet.")