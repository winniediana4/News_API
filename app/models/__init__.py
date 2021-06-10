class News:
  '''
  News class to define movie object
  '''

  def __init__(self, id, title, overview, vote_average, vote_count):
    self.id = id
    self.title = title
    self.vote_average = vote_average
    self.vote_counrt = vote_count