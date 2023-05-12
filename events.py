import requests
import socketio

login_url = 'https://nope-server.azurewebsites.net/api/auth/login'
register_url = 'https://nope-server.azurewebsites.net/api/auth/register'
sio = socketio.Client()


def login(name, password):
    data = {"username": name, "password": password}
    response = requests.post(login_url, json=data)

    try:
        print(response.json()['accessToken'])
    except KeyError:
        return False

    accessToken = response.json()['accessToken']

    sio.connect("https://nope-server.azurewebsites.net", namespaces='/', auth={'token': accessToken})

    return True


def registration(name, password, firstname, lastname):
    data = {"username": name, "password": password, "firstname": firstname, "lastname": lastname}
    response = requests.post(register_url, json=data)

    print(response)


# Server -> Client

@sio.event
def connect():
    # Connect to the server
    print("Connected to server.")


@sio.event
def disconnect():
    # Disconnect from the server
    print("Disconnected from server.")


@sio.event
def callback(data):
    # Prints data on acknowledgement
    print(data)


@sio.on("list:tournaments")
def list_tournaments(data, data1):
    # Lists tournament info for all tournaments
    content = []
    row_content = []

    for tournament in data:
        
        row_content.append(tournament['id'])
        row_content.append(tournament['status'])
        
        for player in tournament["players"]:
            row_content.append(player["username"])

        content.append(row_content)
        row_content = []
        
    for entry in content:
        print(entry)


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
    print("TOURNAMENT LEAVE: ", response)


# tournament:start
def start_tournament():
    response = sio.call("tournament:start")
    print(response)
