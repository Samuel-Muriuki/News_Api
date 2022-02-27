import urllib.request,json
from .models import Sources,Articles


def configure_request(app):
    global source_url,articles_url, api_key
    source_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
    api_key = app.config['NEWS_API_KEY']


def get_sources(category):
    '''
    Function to get json response for our url request
    '''
    get_sources_url = source_url.format(category,api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results