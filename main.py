from events import *


def in_tournament_menu():
    leave = input("Leave Tournament?: ")

    if leave == "y":
        leave_tournament()


def tournament_menu():
    while True:
        print("[1] Create Tournament\n[2] Join Tournament")
        choice = input("Choose: ")

        if choice == "1":
            num_matches = int(input("Number of matches: "))
            create_tournament(num_matches)

        elif choice == "2":
            tournament_id = input("Tournament-ID: ")
            join_tournament(tournament_id)
            break

    in_tournament_menu()


def login_menu():
    print("1. Login")
    print("2. Register")

    while True:
        choice = input("[1] Login, [2] Register: ")

        if choice == "1":
            print("Login credentials:")
            # username = input("Benutzername: ")
            # password = input("Passwort: ")

            if login("Jan", "123456"):
                print("Login successful!")
                tournament_menu()
                break

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


login_menu()
