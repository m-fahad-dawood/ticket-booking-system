from config import MOVIE_FILE, BOOKING_FILE
from movie_manager import view_movies

def book_ticket():
    movies = view_movies()
    if not movies:
        return

    try:
        choice = int(input("Select movie: "))
        tickets = int(input("Number of tickets: "))
        customer = input("Customer name: ")

        name, category, time, price, seats = movies[choice - 1].strip().split(",")
        seats = int(seats)

        if tickets > seats:
            print("❌ Not enough seats!")
            return

        total = tickets * int(price)
        remaining = seats - tickets

        movies[choice - 1] = f"{name},{category},{time},{price},{remaining}\n"

        with open(MOVIE_FILE, "w") as f:
            f.writelines(movies)

        with open(BOOKING_FILE, "a") as f:
            f.write(f"{customer},{name},{tickets},{total}\n")

        print("✅ Booking successful!")
        print("Total Bill: Rs", total)

    except:
        print("❌ Invalid input!")


def view_bookings():
    try:
        with open(BOOKING_FILE, "r") as f:
            bookings = f.readlines()

        if not bookings:
            print("No bookings found.")
            return

        print("\n--- BOOKING HISTORY ---")
        for b in bookings:
            customer, movie, tickets, total = b.strip().split(",")
            print(f"{customer} | {movie} | {tickets} tickets | Rs {total}")

    except FileNotFoundError:
        print("No booking file found.")


def total_revenue():
    total = 0
    try:
        with open(BOOKING_FILE, "r") as f:
            for b in f:
                total += int(b.strip().split(",")[3])

        print("💰 TOTAL REVENUE: Rs", total)

    except FileNotFoundError:
        print("No revenue data found.")
