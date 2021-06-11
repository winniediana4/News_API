import unittest 
from .models import news

News = news.News

class NewsTest(unittest.TestCase):
  '''
  Test class to test behaviour of the News class
  '''

  def setUp(self):
    '''
    set up methods that run before every test
    '''
    self.latest_news = News("More Vaccine-Hesitant Hongkongers Are Finally Signing Up for COVID-19 Shots. Is It the Give-Aways, or the Outbreak Next Door That’s Driving Interest?",
"A Tesla, a free apartment and gold bars are all up for grabs in COVID-19 vaccine lotteries in Hong Kong. They may not be enough to overcome hesitancy.",
"https://time.com/6071742/hong-kong-vaccine-incentives/",
"https://api.time.com/wp-content/uploads/2021/06/hong-kong-covid-19-vaccine.jpg?quality=85&w=1024&h=628&crop=1")


  def test_instance(self):
    self.assertTrue(isinstance(self.latest_news.News))



    if  __name__ == '__main__':
      unittest.main()