import schedule
import time
from datetime import datetime, timedelta
from app.delivery.cli import run_bot

def log(msg):
    print(f"[{datetime.utcnow().isoformat()} UTC] {msg}", flush=True)

def job_wrapper(name, region):
    def job():
        log(f"🤖 Starting {name} News for region: {region}")
        try:
            run_bot(limit=1, region=region)
            log(f"✅ Finished {name} News job.")
        except Exception as e:
            log(f"❌ Error in {name} News job: {e}")
    return job

# Indo time (UTC+7) → Convert to UTC
schedule.every().day.at("02:00").do(job_wrapper("Morning Indo", "indo"))     # 09:00 WIB
schedule.every().day.at("07:00").do(job_wrapper("Afternoon Indo", "indo"))   # 14:00 WIB
schedule.every().day.at("14:00").do(job_wrapper("Evening Global", "global")) # 21:00 WIB

def get_next_run_eta():
    next_run = schedule.idle_seconds()
    if next_run is None or next_run < 0:
        return "Unknown"
    return str(timedelta(seconds=int(next_run)))

log("⏳ AI News Bot Scheduler started...")

while True:
    schedule.run_pending()
    eta = get_next_run_eta()
    log(f"⏱ Waiting... next post in: {eta}")
    time.sleep(60)
