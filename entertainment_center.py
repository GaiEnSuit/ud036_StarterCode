import media
import fresh_tomatoes

moviesList = []

#data for movies
perfect_blue = media.Movie(
    "Perfect Blue",
    "https://www.youtube.com/watch?v=cwGMDibs_KY",
    "https://upload.wikimedia.org/wikipedia/en/b/b2/PerfectBlue.jpg")

pirates_of_the_caribbean = media.Movie(
    "Pirates of the Caribbean",
    "https://www.youtube.com/watch?v=a5V5C8mEVzY",
    "http://thumbs1.ebaystatic.com/d/l225/m/mAcgK6wxgKcw1bJ3pGIc6EQ.jpg")

#adding each movie to the list
moviesList.append(perfect_blue)
moviesList.append(pirates_of_the_caribbean)

fresh_tomatoes.open_movies_page(moviesList)
