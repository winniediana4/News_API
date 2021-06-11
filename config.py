from app.requests import configure_request
import os

class config:
 '''
 General configuration parent class
 '''

 NEWS_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category=business&apikey={}'
 NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
 SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(config):
   '''
   Production configuration child class
   
   Args:
   Config: The parent configuration class with General configuration settings
   '''
   pass

class DEvConfig(configure_request):
     '''
     Production configuration child class

     Args:
     config:The parent configuration child class with General configuration settings
     '''
     pass
     class DevConfig(config):
       '''
       Developement configuration child class

       Args:
       config:The parent configuration class with General configuration class with General configuration settings
       '''

       DEBUG = True

       config_options = {
      'developement':'DevConfig',
       }
       { 
       'developement':ProdConfig  
       }