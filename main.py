from events import *
import time
from format import *


def tournament_menu():
    """
    Main menu for the game
    :return: nothing
    """
    while True:
        # Wait for server
        time.sleep(0.5)

        print_menu()

        choice = input(f"{Color.BLUE_BACKGROUND_BRIGHT} - {Color.BLACK_BOLD}Choose:{Color.RESET} ")

        # Create a tournament
        if choice == "1":
            try:
                num_matches = int(input("Number of matches: "))
                create_tournament(num_matches)
            except ValueError:
                print("Has to be a number!")

        # Join a tournament
        elif choice == "2":
            tournament_idx = int(input("Tournament-Index: "))
            join_tournament(format.formatted_data[tournament_idx][0])

        # Leave a tournament
        elif choice == "3":
            leave_tournament()

        # Start a tournament
        elif choice == "4":
            start_tournament()

        elif choice == "5":
            sio.disconnect()
            break

        else:
            print("Invalid input.\n")


def login_menu():
    """
    Login and Registration menu
    :return: nothing
    """
    print("1. Login")
    print("2. Register")

    while True:
        choice = input("[1] Login, [2] Register: ")

        # Login to the server
        if choice == "1":
            print("\nLogin credentials:")
            username = input("Benutzername: ")
            password = input("Passwort: ")

            if login(username, password):
                print("Login successful!")
                tournament_menu()
                break
            else:
                print("Login failed")

        # Register a new user
        elif choice == "2":
            print("Bitte geben Sie Ihre Registrierungsdaten ein:")
            username = input("Benutzername: ")
            password = input("Passwort: ")
            firstname = input("Firstname: ")
            lastname = input("Lastname: ")

            if registration(username, password, firstname, lastname):
                print("Registration Successful")
            else:
                print("Registration Failed")

        else:
            print("Invalid input.")


if __name__ == "__main__":
    login_menu()
