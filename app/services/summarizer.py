from app.services.openai import client

def summarize_news(news_content: str) -> str:
    messages = [
        {"role": "system", "content": "Summarize this article into 280 characters. Use technical language, sarcasm, memes, and the speaking style of Sheldon Cooper. Be clear and snappy."},
        {"role": "user", "content": news_content}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=120,
            temperature=0.85,
            top_p=0.95,
        )
        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        print(f"[OpenAI Error] {e}")
