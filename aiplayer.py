def aiplayer_move(hand, top_card):

    move = {
        "type": None,
        "card1": None,
        "card2": None,
        "card3": None,
        "reason": "Because I can!"
    }

    if top_card['type'] == 'number':
        required_color = top_card['color']
        required_count = top_card['value']

        print(required_color)
        required_color = required_color.split("-")
        print(required_color[1])

        # Suchen nach passenden Karten in der Hand
        matching_cards = [card for card in hand if card['type'] == 'number' and card['color'] == required_color]

        if len(matching_cards) >= required_count:

            move['type'] = 'put'
            for i in range(required_count):
                move[f'card{i + 1}'] = matching_cards[i]

    return move


# Beispielhand
hand = [
    {"type": "number", "color": "red", "value": 2},
    {"type": "number", "color": "blue", "value": 3},
    {"type": "number", "color": "red", "value": 6},
    # Weitere Karten in der Hand
]

top_card = {"type": "number", "color": "red-green", "value": 3}

move = aiplayer_move(hand, top_card)
print(move)
