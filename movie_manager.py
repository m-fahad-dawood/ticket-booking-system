from config import MOVIE_FILE

def view_movies():
    try:
        with open(MOVIE_FILE, "r") as f:
            movies = f.readlines()
        if not movies:
            print("No movies available.")
            return []

        print("\n--- AVAILABLE MOVIES ---")
        for i, movie in enumerate(movies, start=1):
            name, category, time, price, seats = movie.strip().split(",")
            print(f"{i}. {name} | {category} | {time} | Rs {price} | Seats: {seats}")
        return movies

    except FileNotFoundError:
        print("Movies file not found.")
        return []


def add_movie():
    name = input("Movie name: ")
    category = input("Category: ")
    time = input("Show time: ")
    price = input("Ticket price: ")
    seats = input("Available seats: ")

    with open(MOVIE_FILE, "a") as f:
        f.write(f"{name},{category},{time},{price},{seats}\n")

    print("✅ Movie added successfully!")


def remove_movie():
    movies = view_movies()
    if not movies:
        return

    try:
        choice = int(input("Enter movie number to remove: "))
        movies.pop(choice - 1)

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        print("✅ Movie removed successfully!")
    except:
        print("❌ Invalid choice!")


def update_seats():
    movies = view_movies()
    if not movies:
        return

    try:
        choice = int(input("Select movie number: "))
        change = int(input("Seats to add/remove: "))

        data = movies[choice - 1].strip().split(",")
        name, category, time, price, seats = data
        seats = int(seats) + change

        if seats < 0:
            print("❌ Seats cannot be negative!")
            return

        movies[choice - 1] = f"{name},{category},{time},{price},{seats}\n"

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        print("✅ Seats updated!")

    except:
        print("❌ Invalid input!")
