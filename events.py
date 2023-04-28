import requests
import socketio
import json

url = 'https://nope-server.azurewebsites.net/api/auth/login'
sio = socketio.Client()


def login(name, password):
    data = {"username": name, "password": password}
    response = requests.post(url, json=data)

    try:
        print(response.json()['accessToken'])
    except KeyError:
        return False

    accessToken = response.json()['accessToken']

    sio.connect("https://nope-server.azurewebsites.net", namespaces='/', auth={'token': accessToken})

    return True


def registration(name, password, firstname, lastname):
    data = {"username": name, "password": password, "firstname": firstname, "lastname": lastname}
    response = requests.post(url, json=data)

    print(response)


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


# Client -> Server

# tournament:create
def create_tournament(num_best_of_matches):
    response = sio.call("tournament:create", num_best_of_matches)
    print(response)


# tournament:join
def join_tournament(tournament_id):
    sio.emit("tournament:join", json.dumps({"tournamentId": tournament_id}))


# tournament:leave
def leave_tournament():
    sio.emit("tournament:leave")


# tournament:start
def start_tournament():
    response = sio.call("tournament:start")
    print(response)


