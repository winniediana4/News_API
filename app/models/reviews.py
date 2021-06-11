class Reviews:

  all_reviews = []

  def __init__(self, news_id, title,imageurl, reviews, cls):
    self.news_id = news_id
    self.title = title
    self.imageurl = imageurl
    self.reviews = reviews


    def save_reviews(self):
      Reviews.all_reviews.append(self)

      @classmethod
      def clear_reviews(cls):
        Reviews.all_reviews.clear()

      @classmethod
      def get_reviews(cld, id):

        response = []

        for reviews in cls.all_reviews:
          if reviews.news_id == id:
            response.append(reviews)

            return response  