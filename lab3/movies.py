movies = [
    {"name": "Usual Suspects", "imdb": 3.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 3.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"}
]

def good_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

def avg_imdb_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    if not category_movies:
        return 0
    return sum(movie["imdb"] for movie in category_movies) / len(category_movies)