def ai_player_build_move(hand, top_card, last_topCard, last_move, currentPlayer):
    """
    AI-Player builds a move
    :param last_topCard: card under see-through
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

    if top_card['type'] == 'see-through':
        move = handle_see_through(move, last_topCard, hand)

    if top_card['type'] == 'number':
        move = build(move, top_card, hand)

    if top_card['type'] == 'joker':
        move = handle_reboot_and_joker(move, hand)

    if move['type'] is None:
        if last_move['type'] == 'take':
            move['type'] = 'nope'
        else:
            move['type'] = 'take'

    # logger.info(f"{currentPlayer['username']}: {move}")
    print(f"TOP-CARD: {top_card}")
    # print(f"{currentPlayer['username']}: {move}")

    return move


def build(move, topCard, hand):
    """
    Builds a move if the top card is a number card
    :param move: empty move
    :param topCard: current top card
    :param hand: current player hand
    :return: built move
    """
    required_colors = topCard['color'].split('-')
    required_count = topCard['value']
    matching_cards = []
    all_matching_cards = []
    num_joker_cards = 0

    # Searching for matching cards in hand
    for required_color in required_colors:
        for card in hand:
            if card['type'] == 'number' and any(color in card['color'] for color in required_color.split('-')):
                matching_cards.append(card)

        all_matching_cards.append(matching_cards)

        matching_cards = []

    for card_set in all_matching_cards:

        if can_joker_fill_set(card_set, num_joker_cards, required_count):
            index = all_matching_cards.index(card_set)
            all_matching_cards[index] = joker_fill_set(card_set, required_count)

        print(card_set)

        # if len(card_set) >= required_count:
        #     move['type'] = 'put'
        #     move.update({f'card{i + 1}': card_set[i] for i in range(required_count)})
        #     return move

    return move


def can_joker_fill_set(card_set, num_joker_cards, required_count):
    if len(card_set) < required_count <= len(card_set) + num_joker_cards:
        return True

    return False


def joker_fill_set(card_set, required_count):
    while len(card_set) < required_count:
        card_set.append({"type": "joker", "color": "multi", "value": None})

    return card_set


def count_joker_cards(hand):
    joker_counter = 0

    for card in hand:
        if card['type'] == 'joker':
            joker_counter += 1

    return joker_counter


def handle_see_through(move, last_topCard, hand):
    """
    Handles see-through top-card
    :param move: empty move
    :param last_topCard: top-card under see-through
    :param hand:
    :return: built move
    """
    if last_topCard['type'] == 'number':
        move = build(move, last_topCard, hand)

    if last_topCard['type'] == 'reboot' or last_topCard['type'] == 'joker':
        move = handle_reboot_and_joker(move, hand)

    return move


def handle_reboot_and_joker(move, hand):
    """
    Handles the move if the top-card or last-top-card is a joker or a reboot card
    :param move: empty move
    :param hand: current player-hand
    :return: built move
    """
    for card in hand:
        if card['type'] == 'number' and len(card['color'].split('-')) == 2:
            move.update({'card1': card})
            move.update({'type': 'put'})
            return move

    for card in hand:
        if card['type'] == 'number' and len(card['color'].split('-')) == 1:
            move.update({'card1': card})
            move.update({'type': 'put'})
            return move

    for card in hand:
        if not card['value']:
            move.update({'card1': card})
            move.update({'type': 'put'})
            return move

    return move


# Example hand
handTest = [
    {"type": "number", "color": "yellow", "value": 1},
    {"type": "number", "color": "yellow", "value": 3},
    {"type": "number", "color": "yellow", "value": 2},
    {"type": "number", "color": "red", "value": 1},
    {"type": "number", "color": "blue", "value": 1},
    # {"type": "number", "color": "yellow", "value": 3},
    # {"type": "number", "color": "green", "value": 2},
    # {"type": "number", "color": "red", "value": 1},
    # {"type": "see-through", "color": "red", "value": None},
    # Additional cards in hand
]

top_cardTest = {"type": "number", "color": "yellow-red", "value": 3}
last_topCardTest = {"type": "joker", "color": "multi", "value": None}
moveTest = ai_player_build_move(handTest, top_cardTest, last_topCardTest, {"type": "put"}, None)

print(moveTest)
