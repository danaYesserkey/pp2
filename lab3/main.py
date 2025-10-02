from classes import Square, Rectangle, Point, Account, filter_primes
from functions import grams_to_ounces, reverse_sentence, filter_prime, has_33, spy_game
from movies import movies, good_movies, avg_imdb_category

if __name__ == "__main__":
    print("Square area:", Square(5).area())
    print("Rectangle area:", Rectangle(4, 6).area())

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print("Distance:", p1.dist(p2))

    acc = Account("Ivan", 100)
    acc.deposit(50)
    acc.withdraw(200)
    acc.withdraw(50)

    print("Primes:", filter_primes([2, 3, 4, 5, 10, 11]))

    print("100 grams in ounces:", grams_to_ounces(100))
    print(reverse_sentence("We are ready"))
    print(filter_prime([2, 3, 4, 5, 10, 11]))
    print("has_33:", has_33([1, 3, 3]))
    print("spy_game:", spy_game([1, 2, 4, 0, 0, 7, 5]))

    print("Good movies:", good_movies(movies))
    print("Avg IMDB Romance:", avg_imdb_category(movies, "Romance"))