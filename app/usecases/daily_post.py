import requests
from app.domain.entities import NewsPost
from app.services.summarizer import summarize_news
from app.services.twitter import post_to_twitter

def fetch_top_hn_story():
    ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()
    for id in ids:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json").json()
        if 'url' in story:
            return story['title'], story['url']
    raise Exception("No story with a URL found.")

def run_daily_post():
    title, url = fetch_top_hn_story()
    summary = summarize_news(title, url)
    post = NewsPost(title=title, url=url, summary=summary)

    tweet = f"📰 {post.summary}\n🔗 {post.url}"
    post_to_twitter(tweet)
