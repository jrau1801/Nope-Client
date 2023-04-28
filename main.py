from events import *

print("1. Anmelden")
print("2. Registrieren")

while True:
    choice = input("Bitte wählen Sie eine Option (1 oder 2): ")

    if choice == "1":
        print("Geben Sie Ihre Anmeldedaten ein:")
        username = input("Benutzername: ")
        password = input("Passwort: ")

        if login(username, password):
            print("Sie haben sich erfolgreich angemeldet!")
            sio.disconnect()
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
        print("Ungültige Eingabe. Bitte wählen Sie 1 oder 2.")
