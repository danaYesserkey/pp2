def is_good_movie(movie):
    return movie["imdb"] > 5.5

def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

def avg_imdb_category(movies, category):
    cat_movies = movies_by_category(movies, category)
    return avg_imdb(cat_movies) if cat_movies else 0