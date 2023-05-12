import requests
import socketio
import json

loginurl = 'https://nope-server.azurewebsites.net/api/auth/login'
registerurl = 'https://nope-server.azurewebsites.net/api/auth/register'
sio = socketio.Client()


def login(name, password):
    data = {"username": name, "password": password}
    response = requests.post(loginurl, json=data)

    try:
        print(response.json()['accessToken'])
    except KeyError:
        return False

    accessToken = response.json()['accessToken']

    sio.connect("https://nope-server.azurewebsites.net", namespaces='/', auth={'token': accessToken})

    return True


def registration(name, password, firstname, lastname):
    data = {"username": name, "password": password, "firstname": firstname, "lastname": lastname}
    response = requests.post(registerurl, json=data)

    print(response)


# Server -> Client

@sio.event
def connect():
    # Connect to the server
    print("Connected to server.")


@sio.event
def disconnect():
    print("Disconnected from server.")


@sio.event
def callback(data):
    print(data)


@sio.on("list:tournaments")
def list_tournaments(data, data1):
    # Eine Liste von Turnier-IDs erstellen
    tournament_ids = [tournament['id'] for tournament in data]

    # Die Turnier-IDs ausgeben
    print("\n", tournament_ids)


# Client -> Server

# tournament:create
def create_tournament(num_best_of_matches):
    response = sio.call("tournament:create", num_best_of_matches)
    print(response)


# tournament:join
def join_tournament(tournament_id):
    response = sio.call("tournament:join", tournament_id)
    print(response)


# tournament:leave
def leave_tournament():
    response = sio.call("tournament:leave")
    print(response)


# tournament:start
def start_tournament():
    response = sio.call("tournament:start")
    print(response)
