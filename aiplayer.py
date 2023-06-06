from logger import logger


def ai_player_move(hand, top_card, last_move, currentPlayer):
    """
    AI-Player builds a move
    :param hand: Current hand
    :param top_card: card last played by other player
    :param last_move: last move you made
    :param currentPlayer: player whose turn it is
    :return: built move
    """
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
        for required_color in required_colors:
            for card in hand:
                if card['type'] == 'number' and any(color in card['color'] for color in required_color.split('-')):
                    matching_cards.append(card)

            if len(matching_cards) >= required_count:
                move['type'] = 'put'
                move.update({f'card{i + 1}': matching_cards[i] for i in range(required_count)})
                break

    if move['type'] is None:
        if last_move['type'] == 'take':
            move['type'] = 'nope'
        else:
            move['type'] = 'take'

    # logger.info(f"{currentPlayer['username']}: {move}")
    print(f"{top_card}")
    print(f"{currentPlayer['username']}: {move}")

    return move

# Example hand
# hand = [
#     {"type": "number", "color": "red-blue", "value": 1},
#     {"type": "number", "color": "yellow", "value": 3},
#     {"type": "number", "color": "blue", "value": 2},
#     {"type": "number", "color": "green", "value": 1},
#     {"type": "number", "color": "blue", "value": 1},
#     {"type": "number", "color": "green", "value": 3},
#     {"type": "number", "color": "green", "value": 2},
#     {"type": "number", "color": "red", "value": 1},
#     # Additional cards in hand
# ]
#
# top_card = {"type": "number", "color": "red-yellow", "value": 3}
# move = ai_player_move(hand, top_card, {"type" : "put"})
#
# print(move)
