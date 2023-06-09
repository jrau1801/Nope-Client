from events import *
import time


def tournament_menu():
    """
    Main menu for the game
    :return: nothing
    """
    while True:
        # Wait for server
        time.sleep(0.5)
        print("[1] Create Tournament\n"
              "[2] Join Tournament\n"
              "[3] Leave Tournament\n"
              "[4] Start Tournament\n"
              "[5] Disconnect: ")

        choice = input("Choose: ")

        # Create a tournament
        if choice == "1":
            num_matches = int(input("Number of matches: "))
            create_tournament(num_matches)

        # Join a tournament
        elif choice == "2":
            tournament_id = input("Tournament-ID: ")
            join_tournament(tournament_id)

        # Leave a tournament
        elif choice == "3":
            leave_tournament()

        # Start a tournament
        elif choice == "4":
            if start_tournament():
                break

        elif choice == "5":
            sio.disconnect()
            break
        else:
            print("Invalid input.")


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
            print("Login credentials:")
            username = input("Benutzername: ")
            password = input("Passwort: ")

            if login(username, password):
                print("Login successful!")
                tournament_menu()
                break

        # Register a new user
        elif choice == "2":
            print("Bitte geben Sie Ihre Registrierungsdaten ein:")
            username = input("Benutzername: ")
            password = input("Passwort: ")
            firstname = input("Firstname: ")
            lastname = input("Lastname: ")

            registration(username, password, firstname, lastname)

            print("Sie haben sich erfolgreich registriert!")

        else:
            print("Invalid input.")


if __name__ == "__main__":
    login_menu()
