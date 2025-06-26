from config import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

def summarize_news(news_content: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize this article in 1 sentence max 280 char, technical, sarcastic and to the point with sheldon cooper style explain."},
            {"role": "user", "content": news_content}
        ]
    )
    summary = response.choices[0].message.content.strip()
    return summary
