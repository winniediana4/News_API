from app import app
import urllib.request,json
from .models import news


News = news.News
api_key = None
base_url = None


def configure__request(app):
  global api_key, base_url
  api_key = app.config['3ce1f65982fd4e27a85eababa5d4e0e8']
  base_url = app.config['NEWS_API_BASE_URL']

  api_key = app.config['NEWS_API_KEY']

  base_url = app.config['NEWS_API_BASE_URL']
  def get_news(category):
    '''
    functions that gets json response to our url request
    '''
    get_news_url = base_url.format(category.api_key)

    with urllib.request.urlopen(get_news_url) as url:
      get_news_data = url.read()
      get_news_response = json.loads(get_news_data)

      news_results = None

      if get_news_response['results']:
        news_results_list = get_news_response['results']
        news_results = (news_results_list)

      return news_results(news):
      '''
      Function that process the news result and transform them to a list of objects

      ARGS:
      news: A list df dictionaries that contain news details
      Returns :
      news_results:A list of news objects
      '''
