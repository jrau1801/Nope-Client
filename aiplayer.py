def aiplayer_move(hand, top_card):
    move = {
        "type": "nope",
        "reason": "Because I can!"
    }

    if top_card['type'] == 'number':
        required_color = top_card['color']
        required_count = top_card['value']

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

top_card = {"type": "number", "color": "red", "value": 1}

move = aiplayer_move(hand, top_card)
print(move)
