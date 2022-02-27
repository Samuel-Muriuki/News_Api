import urllib.request,json
from .models import Sources,Articles


def configure_request(app):
    global source_url,articles_url, api_key
    source_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
    api_key = app.config['NEWS_API_KEY']
