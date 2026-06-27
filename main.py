# MAIN PROGRAM MODULE

from generator import generate_password
from hasher import hash_password_with_salt

# show_menu()
def show_menu():
    print("\n=== PYTHON SECURITY TOOLS ===")
    print("1. Generate a secure password")
    print("2. Hash a password with salt")
    print("3. Exit")

# get_user_choice()
def get_user_choice():
    choice = input("Choose an option (1-3): ")
    return choice

# main_loop()
def main_loop():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            password = generate_password()
            if password is not None:
                print("\nGenerated Password:")
                print(password)

        elif choice == "2":
            salt, hashed = hash_password_with_salt()
            print("\nSalt (Base64):")
            print(salt)
            print("\nSHA-256 Hash:")
            print(hashed)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main_loop()