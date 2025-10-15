from classes import Account
from functions import avg_imdb_category, is_good_movie,avg_imdb_category
from movies import movies

if __name__ == "__main__":
    acc = Account("Ivan", 100)
    acc.deposit(50)
    acc.withdraw(200)
    acc.withdraw(50)

    print(is_good_movie(movies[0]))


    print(avg_imdb_category(movies, "Romance"))