import time

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
last_topCard = None
last_move = None
current_player = None
tournament_started = False

lock = threading.Lock()


def login(name, password):
    """
    Handles Client-Login
    :param name: Name of client-player
    :param password: password of client-player
    :return: true if successful, false otherwise
    """
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
    """
    Handles Client-Registration
    :param name: Username of new user
    :param password: Password of new user
    :param firstname: Real firstname of User
    :param lastname: Real lastname of user
    :return: true if successful, false otherwise
    """
    data = {"username": name, "password": password, "firstname": firstname, "lastname": lastname}

    # Register on server
    response = requests.post(register_url, json=data)

    print(response)


# Server -> Client

@sio.event
def connect():
    """
    Connect to server
    :return: nothing
    """
    print("Connected to server.")


@sio.event
def disconnect():
    """
    Disconnect from server
    :return: nothing
    """
    print("Disconnected from server")


@sio.event
def callback(data):
    """
    Prints data on acknowledgment
    :param data: data received from server
    :return: nothing
    """
    print(data)


@sio.on("tournament:playerInfo")
def player_info(data, _):
    """
    Prints player-info
    :param data: player-info-data received from server
    :param _: placeholder
    :return: nothing
    """
    with lock:
        print("\n")
        print("PLAYER INFO: ")
        print(data['message'])
        print("-" * 20)


@sio.on("tournament:info")
def tournament_info(data, _):
    """
    Prints tournament-info
    :param data: tournament-info-data received from server
    :param _: placeholder
    :return: nothing
    """
    with lock:
        global tournament_started
        print("\n")
        print("TOURNAMENT INFO: ")
        print(data['message'])
        print(data['status'])

        if(data['status']) == "FINISHED":
            tournament_started = False

        print("-" * 20)


@sio.on("match:info")
def match_info(data, _):
    """
    Prints match-info
    :param data: match-info-data received from server
    :param _: placeholder
    :return: nothing
    """
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
    """
    Prints list of tournaments
    :param data: tournament-list data received from server
    :param _: placeholder
    :return: nothing
    """
    with lock:

        if not tournament_started:

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
    """
    Initializes ai-player move
    :param data: turn-data received from server
    :return: move to make
    """
    with lock:
        global topCard, hand
        print("\n")
        print(data['message'])
        move = ai.ai_player_build_move(hand, topCard, last_topCard, last_move, current_player)
        time.sleep(0.5)
        return move


@sio.on("game:state")
def game_state(data, _):
    """
    Prints the current game-state
    :param data: game-state-data received from server
    :param _: placeholder
    :return: nothing
    """
    with lock:
        global topCard, hand, last_move, current_player, last_topCard, player_id
        topCard = data['topCard']
        last_topCard = data['lastTopCard']
        hand = data['hand']
        last_move = data['lastMove']
        current_player = data['currentPlayer']

        if player_id == current_player['id']:
            print(f"Top-Card: \n{topCard['type']} \n{topCard['color']} \n{topCard['value']}\n")
            print("YOUR HAND: ")
            for card in data['hand']:
                print(card['type'], card['color'], card['value'])


@sio.on("game:status")
def game_status(data, _):
    """
    Prints message and winner
    :param data: status-data received from server
    :param _: placeholder
    :return: nothing
    """
    time.sleep(0.5)
    print(data['message'])
    print(data['winner'])


# Client -> Server

# tournament:create
def create_tournament(num_best_of_matches):
    """
    Creates a tournament with an emit to the server
    :param num_best_of_matches: number of max matches
    :return: nothing
    """
    response = sio.call("tournament:create", num_best_of_matches)
    print(response)


# tournament:join
def join_tournament(tournament_id):
    """
    Join a tournament with an id
    :param tournament_id: tournament you want to join
    :return: nothing
    """
    response = sio.call("tournament:join", tournament_id)
    print(response)


# tournament:leave
def leave_tournament():
    """
    Leave a tournament
    :return: nothing
    """
    response = sio.call("tournament:leave")
    print("TOURNAMENT LEAVE: ", response)


# tournament:start
def start_tournament():
    """
    Start a tournament
    :return: true if successful, false otherwise
    """
    response = sio.call("tournament:start")
    print(response)

    global tournament_started

    if response['success']:
        tournament_started = True
        return True
