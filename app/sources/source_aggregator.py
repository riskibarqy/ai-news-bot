from app.sources.indonesia.dailysocial import fetch_dailysocial
from app.sources.indonesia.techinasia import fetch_techinasia_rss
from app.sources.global_sources import fetch_global_news

def get_top_news(region=None):
    if region == "indo":
        return fetch_dailysocial(1) + fetch_techinasia_rss(1)
    elif region == "global":
        return fetch_global_news(3)
    else:
        return fetch_dailysocial(1) + fetch_techinasia_rss(1) + fetch_global_news(1)
