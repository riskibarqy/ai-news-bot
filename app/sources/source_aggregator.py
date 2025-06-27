from app.sources.global_sources import fetch_global_news
from app.sources.indo_sources import fetch_indo_news

def get_top_news(region=None):
    if region == "indo":
        return fetch_indo_news(1)
    elif region == "global":
        return fetch_global_news(1)
    else:
        return fetch_indo_news(1) + fetch_global_news(1)
