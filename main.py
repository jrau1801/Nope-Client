import requests
import socketio
import json

data = {"username": "Jan", "password": "123456"}

url = 'https://nope-server.azurewebsites.net/api/auth/login'

response = requests.post(url, json=data)

print(response.json()['accessToken'])

accessToken = response.json()['accessToken']

sio = socketio.Client()


@sio.event
def connect():
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


# Connect to the server
sio.connect("https://nope-server.azurewebsites.net", namespaces='/', auth={'token': accessToken})

# Example usage
create_tournament(5)
# join_tournament(1)
# leave_tournament()
# start_tournament()

# Disconnect from the server
sio.disconnect()
