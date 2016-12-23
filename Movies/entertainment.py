import fresh_tomatoes
import Movie

3-idiots = Movie.Movie("3 idiots",   "The engineering college", "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg", "https://www.youtube.com/watch?v=eY2Da8o_9XI")

ms-dhoni = Movie.Movie("MS Dhoni",
                       "The untold story",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BOTY5ODQxMTY3M15BMl5BanBnXkFtZTgwOTA3NTA4OTE@._V1_UY268_CR2,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=0mQLTWvXbXM")

fnf8 = Movie.Movie("Fast & Furious 8",
                   "Life is a race",
                   "http://digitalspyuk.cdnds.net/16/16/480x678/gallery-1461099449-fast-furious-8-poster.jpg",
                   "https://www.youtube.com/watch?v=uisBaTkQAEs")

befikre = Movie.Movie("Befikre",
                       "Love Story",
                       "http://www.songspk.guru/mp3/images/cover/58084ecac78a4nashe-ki-chadh-gayi.jpg",
                       "https://www.youtube.com/watch?v=Wd2B8OAotU8")


movies = [3-idiots, ms-dhoni, fnf8, befikre]
fresh_tomatoes.open_movies_page(movies)
