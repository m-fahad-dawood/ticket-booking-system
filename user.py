from movie_manager import view_movies
from booking_manager import book_ticket

def user_mode():
    while True:
        print("\n===== USER MODE =====")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            view_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
