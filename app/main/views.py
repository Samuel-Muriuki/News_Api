from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Sources

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting the page sources
    sources=get_sources('business')
    sports_sources=get_sources('sports')
    technology_sources=get_sources('technology')
    entertainment_sources=get_sources('entertainment')
    title="News Highlighter"

    return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@main.route('/sources/<int:id>')
def articles(id):
	'''
    View articles page function that returns the news details page and its data
	'''
	articles = get_articles(id)
	title = f' | {id}'

	return render_template('articles.html',title= title,articles = articles)