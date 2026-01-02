from config import MOVIE_FILE

def view_movies():
    try:
        with open(MOVIE_FILE, "r") as f:
            movies = f.readlines()

        if not movies:
            print("No movies available.")
            return

        print("\n--- AVAILABLE MOVIES ---")
        for i, movie in enumerate(movies, start=1):
            name, category, time, price, seats = movie.strip().split(",")
            print(f"{i}. {name} | {category} | {time} | Rs {price} | Seats: {seats}")

    except FileNotFoundError:
        print("No movies file found.")


def add_movie():
    name = input("Enter movie name: ")
    category = input("Enter category: ")
    time = input("Enter show time: ")
    price = input("Enter ticket price: ")
    seats = input("Enter available seats: ")

    with open(MOVIE_FILE, "a") as f:
        f.write(f"{name},{category},{time},{price},{seats}\n")

    print("✅ Movie added successfully!")


def remove_movie():
    try:
        with open(MOVIE_FILE, "r") as f:
            movies = f.readlines()

        view_movies()
        choice = int(input("Enter movie number to remove: "))
        movies.pop(choice - 1)

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        print("✅ Movie removed successfully!")
    except:
        print("Invalid input!")


def update_seats():
    try:
        with open(MOVIE_FILE, "r") as f:
            movies = f.readlines()

        view_movies()
        choice = int(input("Select movie number: "))
        change = int(input("Enter seats to add/remove: "))

        data = movies[choice - 1].strip().split(",")
        seats = int(data[4]) + change

        if seats < 0:
            print("❌ Seats cannot be negative!")
            return

        data[4] = str(seats)
        movies[choice - 1] = ",".join(data) + "\n"

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        print("✅ Seats updated!")
    except:
        print("Invalid input!")
