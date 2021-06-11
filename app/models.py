class news:
  '''
  news classto define news objects
  '''

  def __init__(self, id, title, overview, poster, vote_average, vote_count):
    self.id = id
    self.title = title
    self.overview = overview
    self.poster = "https:/images.wsj.net/im-247417/social" + poster
    self.vote_average = vote_average
    self.vote_count = vote_count 

    class Review:
      all_reviews = []

      def __init__(self, news_id, title,imageurl, review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.reviews = review

      def save_review(self):
          Review.all_reviews.append(self) 


      @classmethod
      def get_reviews(cls,id):

        response = []


      @classmethod
      def get_reviews(cls,id):

        response = []
        
         
