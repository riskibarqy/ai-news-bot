import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

def summarize_news(title: str, url: str) -> str:
    prompt = f"Summarize this news article for developers in 1 sentence:\nTitle: {title}\nURL: {url}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
