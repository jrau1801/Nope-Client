import requests
import socketio
import threading
import aiplayer as ai

login_url = 'https://nope-server.azurewebsites.net/api/auth/login'
register_url = 'https://nope-server.azurewebsites.net/api/auth/register'
sio = socketio.Client()

player_id = None
hand = None
topCard = None
last_move = None
current_player = None

lock = threading.Lock()


def login(name, password):
    # Login logic
    data = {"username": name, "password": password}
    response = requests.post(login_url, json=data)

    # Try to get Access-Token
    try:
        print(response.json()['accessToken'])
        player = response.json()['user']
        global player_id
        player_id = (player['id'])
    except KeyError or requests.exceptions.JSONDecodeError:
        return False

    # Save Access-Token
    accessToken = response.json()['accessToken']

    # Connect to server
    sio.connect("https://nope-server.azurewebsites.net", namespaces='/', auth={'token': accessToken})

    return True


def registration(name, password, firstname, lastname):
    # Register Logic
    data = {"username": name, "password": password, "firstname": firstname, "lastname": lastname}

    # Register on server
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
    print("Disconnected from server")


@sio.event
def callback(data):
    # Prints data on acknowledgement
    print(data)


@sio.on("tournament:playerInfo")
def player_info(data, _):
    with lock:
        print("\n")
        print("PLAYER INFO: ")
        print(data['message'])
        print("-" * 20)


@sio.on("tournament:info")
def tournament_info(data, _):
    with lock:
        print("\n")
        print("TOURNAMENT INFO: ")
        print(data['message'])
        print(data['status'])
        print("-" * 20)


@sio.on("match:info")
def match_info(data, _):
    with lock:
        print("\n")
        print("MATCH INFO: ")
        print(data['message'])

        opponents = data['match']['opponents']

        # Print the usernames
        for opponent in opponents:
            pass
            # print(opponent['username'])

        print("-" * 20)


@sio.on("list:tournaments")
def list_tournaments(data, _):
    with lock:
        print("\n")
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
        print("\n")


@sio.on("game:makeMove")
def make_move(data):
    with lock:
        global topCard, hand
        print("\n")
        print(data['message'])
        return ai.ai_player_move(hand, topCard, last_move, current_player)


@sio.on("game:state")
def game_state(data, _):
    with lock:
        print("\n")
        global topCard, hand, last_move, current_player
        topCard = data['topCard']
        hand = data['hand']
        last_move = data['lastMove']
        current_player = data['currentPlayer']

        print("TOP-CARD: ", data['topCard'])

        for card in data['hand']:
            print(card['type'], card['color'], card['value'])


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

    if response['success']:
        return True
