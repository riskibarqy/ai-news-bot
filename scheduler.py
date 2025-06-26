import schedule
import time
from app.delivery.cli import run_bot

def post_indo_morning():
    print("🤖 Morning Indo News")
    run_bot(limit=1, region="indo")

def post_indo_afternoon():
    print("🤖 Afternoon Indo News")
    run_bot(limit=1, region="indo")

def post_global_evening():
    print("🤖 Evening Global News")
    run_bot(limit=1, region="global")

# Schedule jobs (adjust for your timezone)
schedule.every().day.at("09:00").do(post_indo_morning)     # 9 AM
schedule.every().day.at("14:00").do(post_indo_afternoon)   # 2 PM
schedule.every().day.at("21:00").do(post_global_evening)   # 9 PM

print("⏳ AI News Bot Scheduler running...")
while True:
    schedule.run_pending()
    time.sleep(30)
