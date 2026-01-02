from config import MOVIE_FILE, BOOKING_FILE
from movie import view_movies

def book_ticket():
    try:
        with open(MOVIE_FILE, "r") as f:
            movies = f.readlines()

        if not movies:
            print("No movies available.")
            return

        view_movies()
        choice = int(input("Select movie number: "))
        tickets = int(input("Number of tickets: "))
        customer = input("Customer name: ")

        data = movies[choice - 1].strip().split(",")
        name, category, time, price, seats = data

        seats = int(seats)
        price = int(price)

        if tickets > seats:
            print("❌ Not enough seats!")
            return

        total = tickets * price
        data[4] = str(seats - tickets)
        movies[choice - 1] = ",".join(data) + "\n"

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        with open(BOOKING_FILE, "a") as f:
            f.write(f"{customer},{name},{tickets},{total}\n")

        print("✅ Booking successful! Bill: Rs", total)

    except:
        print("Invalid input!")


def view_bookings():
    try:
        with open(BOOKING_FILE, "r") as f:
            for b in f:
                c, m, t, total = b.strip().split(",")
                print(f"{c} | {m} | {t} tickets | Rs {total}")
    except:
        print("No bookings found.")


def total_revenue():
    total = 0
    try:
        with open(BOOKING_FILE, "r") as f:
            for b in f:
                total += int(b.strip().split(",")[3])
        print("💰 TOTAL REVENUE: Rs", total)
    except:
        print("No revenue data.")
