from config import ADMIN_PASSWORD
from movie import add_movie, view_movies, remove_movie, update_seats
from booking import view_bookings, total_revenue

def admin_mode():
    pwd = input("Enter admin password: ")
    if pwd != ADMIN_PASSWORD:
        print("❌ Wrong password!")
        return

    while True:
        print("\n===== ADMIN MODE =====")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Remove Movie")
        print("4. Update Seats")
        print("5. View Bookings")
        print("6. Total Revenue")
        print("7. Logout")

        choice = input("Choice: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            remove_movie()
        elif choice == "4":
            update_seats()
        elif choice == "5":
            view_bookings()
        elif choice == "6":
            total_revenue()
        elif choice == "7":
            break
