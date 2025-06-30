import traceback
import tweepy
from config import settings
from app.usecases.daily_post import run_daily_post  # make sure this doesn't create circular import

MAX_TWEET_RETRY = 1
tweet_retry_counter = {"count": 0}

client = tweepy.Client(
    bearer_token=settings.TWITTER_BEARER_TOKEN,
    consumer_key=settings.TWITTER_API_KEY,
    consumer_secret=settings.TWITTER_API_SECRET,
    access_token=settings.TWITTER_ACCESS_TOKEN,
    access_token_secret=settings.TWITTER_ACCESS_SECRET,
    wait_on_rate_limit=True,
)

def post_to_twitter(text: str):
    try:
        response = client.create_tweet(text=text)
        
        if hasattr(response, 'errors') and response.errors:
            print("❌ Tweet failed with API error(s):")
            for err in response.errors:
                print(f"  - {err}")
        else:
            tweet_id = response.data.get("id")
            print(f"✅ Tweet posted successfully! ID: {tweet_id}")
    
    except tweepy.TweepyException as e:
        print("❌ Tweepy error while tweeting:")
        print(f"  Type    : {type(e).__name__}")
        print(f"  Message : {e}")
        print("  Traceback:")
        traceback.print_exc()

        # Retry logic
        if tweet_retry_counter["count"] < MAX_TWEET_RETRY:
            tweet_retry_counter["count"] += 1
            print("🔁 Retrying post via run_daily_post() due to Tweepy failure...")
            run_daily_post(limit=1)

    except Exception as e:
        print("❌ Unexpected error occurred:")
        print(f"  Type    : {type(e).__name__}")
        print(f"  Message : {e}")
        print("  Traceback:")
        traceback.print_exc()

        # Retry logic
        if tweet_retry_counter["count"] < MAX_TWEET_RETRY:
            tweet_retry_counter["count"] += 1
            print("🔁 Retrying post via run_daily_post() due to", e)
            run_daily_post(limit=1)
