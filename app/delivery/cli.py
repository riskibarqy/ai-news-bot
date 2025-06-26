from app.usecases.daily_post import run_daily_post

def run_bot(limit=3, region=None):
    print("🤖 Running AI News Bot...")
    run_daily_post(limit=limit, region=region)
