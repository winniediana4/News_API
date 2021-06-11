# from app import app
# import urllib.request,json
# from .models import news


# News = news.News
# api_key = None
# base_url = None


# def configure__request(app):
#   global api_key, base_url
#   api_key = app.config['']
#   base_url = app.config['NEWS_API_BASE_URL']

#   api_key = app.config['NEWS_API_KEY']

#   base_url = app.config['NEWS_API_BASE_URL']
#   def get_news(category):
#     '''
#     functions that gets json response to our url request
#     '''
#     get_news_url = base_url.format(category.api_key)

#     with urllib.request.urlopen(get_news_url) as url:
#       get_news_data = url.read()
#       get_news_response = json.loads(get_news_data)

#       news_results = None

#       if get_news_response['results']:
#         news_results_list = get_news_response['results']
#         news_results = (news_results_list)

#       return news_results(news)
#       '''
#       Function that process the news result and transform them to a list of objects

#       ARGS:
#       news: A list df dictionaries that contain news details
#       Returns :
#       news_results:A list of news objects
#       '''
#       news_results = []
#       for news_items in news:
#         id = news_items.get('id')
#         title = news_items.get('original_title')
#         overview = news_items.get('overview')
#         poster = news_items.get('poster_path')
#         vote_average = news_items.get('vote_average')
#         vote_count = news_item.get('vote_count')

#         if poster:
#           news_object = News(id, title,overview, poster, vote_average, vote_count)
#           news_results.append(news_object)

#           return news_results

#         def get_news(id):
#           get_news_details_url = base_url.format(id, api_key)

#           with urllib.resquest.urlopen(get_news_details_url)  as url:  
#             news_details_data = url.read()
#             news_details_response = json.loads(news_details_data)

#             news_object = None
#             if news_details_response:
#               id = news_details_response.get('id')
#               title = news_details_response.get('original_title')
#               overview = news_details_response.get('overview')
#               poster = news_details_response.get('poster_path')
#               vote_count = news_details_response.get('vote_count')
#               news_object = News(id, title,overview,poster, poster, vote_average,vote_count)

#               return news_object 

#               def search_news(news_name):
#                 search_news_url = "http://newsapi.org/v2/top_headlines?country=us&category=business&apikey={}&query={}'.format(api_key, news_name"
#                 withurllib.request.urlopen(search_news_data)

#                 search_news_results = None

#                 if search_news_response['results']:
#                   search_news = search_news_response['results']
#                   search_news_results = process_results()

#                   return search_news_results

import urllib.request,json
from .models import Article, Category, Source , Headlines

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
cat_url= None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']


def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results

def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = cat_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results
