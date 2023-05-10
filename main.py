from events import *

print("1. Anmelden")
print("2. Registrieren")

while True:
    choice = input("[1] Login, [2] Registration: ")

    if choice == "1":
        print("Login credentials:")
        # username = input("Benutzername: ")
        # password = input("Passwort: ")

        if login("Jan", "123456"):
            print("Login successful!")
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

# create_tournament(3)
