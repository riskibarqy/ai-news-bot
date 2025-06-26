# 🧠 AI News Bot — Powered by Python, Posting Like Sheldon Cooper

An automated AI-powered news bot that posts hot programming, startup, and tech-related news on Twitter — with a distinct Sheldon Cooper personality. It posts 3 times daily:
- 2x from **Indonesian tech/startup news**
- 1x from **global programming/startup/corporate news**

Built with clean architecture principles, deployed for free using Fly.io, and infused with wit and sarcasm like your favorite physicist.

---

## ✨ Features

- 🔍 Scrapes news from multiple sources (e.g. Tech in Asia, DailySocial, HackerNews)
- 🧠 Summarizes using OpenAI's GPT models
- 🐦 Tweets with a custom tone/personality (like Sheldon Cooper)
- ⏰ Scheduled 3x per day automatically
- ☁️ Runs on Fly.io (on free tier)
- 🧼 Clean codebase with domain-driven design

---

## 📦 Project Structure

├── app
│ ├── delivery # CLI / entry points
│ ├── domain # Entities and interfaces
│ ├── services # Integrations: summarizer, twitter, news sources
│ ├── usecases # Business logic / orchestration
├── scheduler.py # Main scheduled runner
├── config.py # Environment variables (using Pydantic Settings)
├── Dockerfile # Container definition
├── fly.toml # Fly.io deployment config
├── requirements.txt # Python dependencies
└── README.md # This file

---

## ⚙️ Setup

### 1. Clone & Install

```bash
git clone https://github.com/riskibarqy/ai-news-bot.git
cd ai-news-bot
pip install -r requirements.txt
```

### 2. Set up .env (or OS env vars)

OPENAI_API_KEY=your_openai_key
TWITTER_BEARER_TOKEN=...
TWITTER_CONSUMER_KEY=...
TWITTER_CONSUMER_SECRET=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_SECRET=...

## 🚀 Run Locally

```bash
python scheduler.py
```

## Or manually:

```bash
python main.py
```

## 🕒 Scheduling Tweets (3x/day)
Already handled using schedule library inside scheduler.py:

9:00 WIB: Indonesian news

13:00 WIB: Indonesian news

18:00 WIB: Global tech news

## ☁️ Deployment on Fly.io (Free Tier)

# Requirements
- Fly CLI: https://fly.io/docs/hands-on/install-flyctl/
- Docker installed

# Deploy
```bash
fly auth login
fly launch  # (once)
fly deploy
```
You’ll stay on free tier by default (256MB shared VM, no web service, auto shutdown).

## 🧠 Personality Mode: Sheldon Cooper
Yes, the bot’s summaries and tweets follow a tone inspired by Dr. Sheldon Cooper:

- Sarcastic
- Highly articulate
- Occasionally passive-aggressive
- Always informative

Example tweet:

"Oh, look, another Indonesian startup raised 2 million dollars to solve a problem no one knew existed. Fascinating. Read on."

# ✅ Sources
- TechInAsia
- HackerNews
- [Global RSS feeds]
- DailySocial (if available)

# 📜 License
MIT — use, fork, tweak, or criticize.

# 👤 Author
Riski Ramdan
GitHub: @riskibarqy

# 🙋‍♂️ Contributing
PRs are welcome if:
- The code is clean
- The humor is smarter than average
- The news sources are useful