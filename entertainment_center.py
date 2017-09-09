import media
import fresh_tomatoes

moviesList = []

#data for movies
movie1 = media.Movie(
    "Perfect Blue",
    "https://www.youtube.com/watch?v=cwGMDibs_KY",
    "https://upload.wikimedia.org/wikipedia/en/b/b2/PerfectBlue.jpg")

movie2 = media.Movie(
    "Pirates of the Caribbean",
    "https://www.youtube.com/watch?v=XibzC-e_s5M",
    "http://thumbs1.ebaystatic.com/d/l225/m/mAcgK6wxgKcw1bJ3pGIc6EQ.jpg")

#adding each movie to the list
moviesList.append(movie1)
moviesList.append(movie2)

fresh_tomatoes.open_movies_page(moviesList)
