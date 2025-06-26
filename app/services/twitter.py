import tweepy
from config import settings

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
        if response.errors:
            print("❌ Tweet failed:", response.errors)
        else:
            print(f"✅ Tweet posted with id: {response.data['id']}")
    except Exception as e:
        print("❌ Exception while tweeting:", e)
