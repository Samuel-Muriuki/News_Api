import os

class Config:
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY ='53ffdeb94a4d451e9f763453ed4c7665'

   
    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}