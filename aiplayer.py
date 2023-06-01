def ai_player_move(hand, top_card):

    global take_counter

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

        # Searching for matching cards in hand
        for i in range(len(required_colors)):
            matching_cards = [card for card in hand if card['type'] == 'number' and card['color'] in required_colors[i]]

            if len(matching_cards) >= required_count:
                move['type'] = 'put'

                for j in range(required_count):
                    move[f'card{j + 1}'] = matching_cards[j]

                return move

    if take_counter >= 1:
        move['type'] = 'nope'
        take_counter = 0
        return move

    if take_counter == 0:
        move['type'] = 'take'
        take_counter += 1

    return move


# Example hand
hand = [
    {"type": "number", "color": "red", "value": 2},
    {"type": "number", "color": "red", "value": 3},
    {"type": "number", "color": "yellow", "value": 4},
    {"type": "number", "color": "yellow", "value": 5},
    # Additional cards in hand
]

top_card = {"type": "number", "color": "red-yellow", "value": 2}
take_counter = 0
move = ai_player_move(hand, top_card)
print(move)
