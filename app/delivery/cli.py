from app.usecases.daily_post import run_daily_post

def run_bot():
    print("🤖 Running AI News Bot (Twitter only)...")
    run_daily_post()
