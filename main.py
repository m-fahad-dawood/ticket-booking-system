from admin import admin_mode
from user import user_mode

while True:
    print("\n===== CINEMA MANAGEMENT SYSTEM =====")
    print("1. Admin Mode")
    print("2. User Mode")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        admin_mode()
    elif choice == "2":
        user_mode()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
