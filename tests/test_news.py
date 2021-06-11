import unittest
from app.models import News

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News class
  '''

  def setUp(self):
    '''
    set up method that will run before every Test
    '''
    self.latest_news = News("More Vaccine-Hesitant Hongkongers Are Finally Signing Up for COVID-19 Shots. Is It the Give-Aways, or the Outbreak Next Door That’s Driving Interest?",
 "A Tesla, a free apartment and gold bars are all up for grabs in COVID-19 vaccine lotteries in Hong Kong. They may not be enough to overcome hesitancy.")

def test_instance(self):
  self.assertTrue(isinstance(self.latest_news, News))
