#A class for a movie object
class Movie:
    #constructor that instantiates the title, trailer url, and poster image url
    def __init__(self, movie_title, url, img):
        self.title = movie_title
        self.trailer_youtube_url = url
        self.poster_image_url = img
