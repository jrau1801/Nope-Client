def aiplayer_move(hand, top_card):
    can_put = False
    global take_counter

    move = {
        "type": None,
        "card1": None,
        "card2": None,
        "card3": None,
        "reason": "Because I can!"
    }

    if top_card['type'] == 'number':
        required_colors = top_card['color'].split('-')  # Splitting the color string by '-' to get individual colors
        required_count = top_card['value']

        # Searching for matching cards in hand
        for i in range(len(required_colors)):

            matching_cards = [card for card in hand if card['type'] == 'number' and card['color'] in required_colors[i]]

            if len(matching_cards) >= required_count:
                move['type'] = 'put'
                can_put = True
                for j in range(required_count):
                    move[f'card{j + 1}'] = matching_cards[j]

    if take_counter >= 1:
        move['type'] = 'nope'
        take_counter = 0
        return move

    if not can_put:
        move['type'] = 'take'
        take_counter += 1

    return move


# Example hand
hand = [
    {"type": "number", "color": "red", "value": 2},
    {"type": "number", "color": "red", "value": 3},
    {"type": "number", "color": "red", "value": 4},
    {"type": "number", "color": "green", "value": 5},
    # Additional cards in hand
]

top_card = {"type": "number", "color": "red-yellow", "value": 3}
take_counter = 0
move = aiplayer_move(hand, top_card)
print(move)
