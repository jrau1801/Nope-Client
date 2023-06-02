from logger import logger


def ai_player_move(hand, top_card, last_move, currentPlayer):
    move = {
        "type": None,
        "card1": None,
        "card2": None,
        "card3": None,
        "reason": "A"
    }

    if top_card['type'] == 'number':
        required_colors = top_card['color'].split('-')  # Splitting the color string by '-' to get individual colors
        required_count = top_card['value']

        matching_cards = []
        # Searching for matching cards in hand
        for i in range(len(required_colors)):
            for card in hand:
                if card['type'] == 'number':
                    color = card['color'].split("-")
                    for j in range(len(color)):
                        if color[j] in required_colors[i]:
                            matching_cards.append(card)

                    if len(matching_cards) >= required_count:
                        move['type'] = 'put'
                        for j in range(required_count):
                            move[f'card{j + 1}'] = matching_cards[j]


    if move['type'] is None:
        if last_move['type'] == 'take':
            move['type'] = 'nope'
        else:
            move['type'] = 'take'

    logger.info(f"{currentPlayer['username']}: {move}")
    print(f"{currentPlayer['username']}: {move}")
    return move

# Example hand
# hand = [
#     {"type": "number", "color": "yellow", "value": 1},
#     {"type": "number", "color": "red", "value": 3},
#     {"type": "number", "color": "blue", "value": 2},
#     {"type": "number", "color": "yellow-green", "value": 1},
#     {"type": "number", "color": "blue", "value": 1},
#     {"type": "number", "color": "yellow", "value": 3},
#     {"type": "number", "color": "green", "value": 2},
#     {"type": "number", "color": "yellow-red", "value": 1},
#     # Additional cards in hand
# ]

# top_card = {"type": "number", "color": "red", "value": 3}
# move = ai_player_move(hand, top_card)
#
# print(move)
