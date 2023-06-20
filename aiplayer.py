from format import *


def ai_player_build_move(hand, top_card, last_topCard, last_move):
    """
    AI-Player builds a move
    :param last_topCard: card under see-through
    :param hand: Current hand
    :param top_card: card last played by other player
    :param last_move: last move you made
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
        print_top_card_formatted(last_topCard, prefix="LAST-")
        move = handle_see_through(move, last_topCard, hand)

    if top_card['type'] == 'number':
        move = build(move, top_card, hand, last_topCard)

    if top_card['type'] == 'joker' or top_card['type'] == 'reboot':
        move = handle_reboot_and_joker(move, hand)

    if check_for_action(hand) and not check_same_color_hand_field(hand, top_card):
        move = handle_only_action_left(move, hand, top_card, last_topCard)

    if check_for_only_action(hand):
        move = handle_only_action_left(move, hand, top_card, last_topCard)

    if move['type'] is None:
        if last_move is not None and last_move['type'] == 'take':
            move['type'] = 'nope'
            move.update({'reason': 'No Set with Number-Cards and Joker possible and already Take -> Nope.'})
        else:
            move['type'] = 'take'
            move.update({'reason': 'No Set with Number-Cards and Joker possible -> Take.'})

    # logger.info(f"{currentPlayer['username']}: {move}")
    print_move_formatted(move)

    return move


def build(move, topCard, hand, last_top_card):
    """
    Builds a move if the top card is a number card
    :param last_top_card: top-card under see-through
    :param move: empty move
    :param topCard: current top card
    :param hand: current player hand
    :return: built move
    """
    required_colors = topCard['color'].split('-')
    required_count = topCard['value']
    matching_cards = []
    all_matching_cards = []

    if check_for_action(hand) and not check_same_color_hand_field(hand, topCard):
        move = handle_only_action_left(move, hand, topCard, last_top_card)
        return move

    if check_for_only_action(hand):
        move = handle_only_action_left(move, hand, topCard, last_top_card)
        return move

    # Searching for matching cards in hand
    for required_color in required_colors:
        for card in hand:
            if card['type'] == 'number' and any(color in card['color'] for color in required_color.split("-")):
                if len(matching_cards) < required_count:
                    matching_cards.append(card)

        if len(matching_cards) != 0:
            all_matching_cards.append(matching_cards)

        matching_cards = []

    if check_for_reboot(hand) and topCard['value'] == 3 and move['type'] == 'put':
        move = play_reboot_first(move, hand)
        return move

    return move


def filter_and_weigh(all_matching_cards, hand, required_count, move):
    """
    Starts filtering possible card sets and weigh cards to find best set
    :param all_matching_cards: cards with same color or joker
    :param hand: player hand
    :param required_count: number of cards needed
    :param move: empty move
    :return: built move
    """
    num_joker_cards = count_joker_cards(hand)

    for card_set in all_matching_cards:
        if can_joker_fill_set(card_set, num_joker_cards, required_count):
            index = all_matching_cards.index(card_set)
            all_matching_cards[index] = joker_fill_set(card_set, required_count)

    all_matching_cards = filter_all_matching(all_matching_cards, required_count)

    full_set = weigh_sets(all_matching_cards)

    if len(full_set) >= required_count:
        move['type'] = 'put'
        move.update({f'card{i + 1}': full_set[i] for i in range(required_count)})
        move.update({'reason': 'Set was completed -> Set with highest value'})
        return move

    return move


def weigh_sets(all_matching_cards):
    """
    Weighs all available card sets based on their card type and color
    :param all_matching_cards: available sets
    :return: best set
    """
    best_set = []

    weighed_sets = []

    for card_set in all_matching_cards:
        weigh_value = 0
        for card in card_set:

            if card['type'] == 'joker':
                weigh_value += 50

            if card['type'] == 'number' and len(card['color'].split("-")) == 2:
                weigh_value += 30

            if card['type'] == 'number' and len(card['color'].split("-")) == 1:
                weigh_value += 20

        weighed_sets.append({weigh_value: card_set})

    if not weighed_sets:
        return best_set

    max_value = max(weighed_sets, key=lambda x: max(x.keys()))
    best_set = max_value[max(max_value.keys())]
    return best_set


def filter_all_matching(all_matching_cards, required_count):
    """
    Removes card sets where the length is less than the required card count
    :param all_matching_cards: array with card sets
    :param required_count: number of cards needed
    :return: filtered card sets
    """
    all_matching_cards = [card_set for card_set in all_matching_cards if len(card_set) >= required_count]
    return all_matching_cards


def get_joker(hand):
    """
    Gets a joker from hand
    :param hand: player hand
    :return: joker card
    """
    for card in hand:
        if card['type'] == 'joker':
            return card


def get_reboot(hand):
    """
    Gets a reboot card from hand
    :param hand: player hand
    :return: a reboot card
    """
    for card in hand:
        if card['type'] == 'reboot':
            return card


def play_reboot_first(move, hand):
    """
    Play a reboot card
    :param move: empty move
    :param hand: player hand
    :return: built move
    """
    move.update({"card1": get_reboot(hand)})
    move.update({"card2": None})
    move.update({"card3": None})
    move.update({'reason': 'Reboot on hand and Top-Card has value of 3 and other set of 3 available -> Reboot'})

    return move


def check_for_reboot(hand):
    """
    Checks if the hand has a reboot card
    :param hand: player hand
    :return: True if reboot is in hand, False if not
    """
    for card in hand:
        if card['type'] == 'reboot':
            return True

    return False


def check_for_action(hand):
    """
    Checks if the hand has action cards
    :param hand: player hand
    :return: True, if only action cards in hand, False if not
    """
    for card in hand:
        if card['type'] == 'reboot' or card['type'] == 'see-through' or card['type'] == 'joker':
            return True

    return False


def check_for_only_action(hand):
    """
    Checks if the hand ONLY has action cards
    :param hand: player hand
    :return: True if player only has action cards, False otherwise
    """
    for card in hand:
        if card['type'] == 'number':
            return False

    return True


def check_same_color_hand_field(hand, top_card):
    """
    check if player has card with same color as top-card
    :param hand: player hand
    :param top_card: current top-card
    :return: if color is same return True, otherwise False
    """
    same_color = False

    for card in hand:

        if card['type'] == 'number':
            have_colors = card['color'].split("-")
            need_colors = top_card['color'].split("-")

            for color in have_colors:
                if color in need_colors or 'multi' in need_colors:
                    same_color = True
                    break

    return same_color


def handle_only_action_left(move, hand, top_card, last_top_card):
    """
    Plays the action cards if they're the only ones left
    :param last_top_card: top-card under see-through
    :param move: empty move
    :param hand: player hand
    :param top_card: current card at the top
    :return: built move
    """

    if top_card['type'] == 'see-through':
        top_card = last_top_card

    for card in hand:

        if card['type'] == 'see-through':

            if card['color'] in top_card['color'].split("-") or top_card['color'] == 'multi':
                move['type'] = 'put'
                move.update({'card1': card})
                move.update({'reason': 'Only Action cards left -> See-Through same color as Top-Card.'})
                return move

        if card['type'] == 'reboot':
            move['type'] = 'put'
            move.update({'card1': card})
            move.update({'reason': 'Only Action cards left and no See-Through on hand -> Reboot.'})
            return move

        if card['type'] == 'joker' and top_card['value'] is not None and top_card['value'] <= count_joker_cards(hand):
            move['type'] = 'put'
            move.update({f'card{i + 1}': get_joker(hand) for i in range(top_card['value'])})
            move.update({'reason': 'Only Action cards left and no See-Through or Reboot on hand -> Joker.'})
            return move

        if card['type'] == 'joker' and top_card['value'] is None and not check_same_color_hand_field(hand, top_card):
            move['type'] = 'put'
            move.update({f'card1': get_joker(hand)})

    return move


def sort_card_set_asc(card_set):
    """
    sorts the playable card-set by value ascending -> 1, 2, 3
    :param card_set: playable set
    :return: asc-sorted set
    """
    temp = card_set
    n = len(temp)
    sort = False
    if n >= 2:
        while not sort:
            sort = True
            for i in range(n - 1):
                current_card = temp[i]
                next_card = temp[i + 1]

                if current_card["value"] > next_card["value"]:
                    # Swap card contents
                    temp[i], temp[i + 1] = next_card, current_card
                    sort = False

    print(temp)


def sort_card_set_desc(card_set):
    """
    sorts the playable card-set by value descending -> 3, 2, 1
    :param card_set: playable set
    :return: desc-sorted set
    """
    temp = card_set
    n = len(temp)
    sort = False
    if n >= 2:
        while not sort:
            sort = True
            for i in range(n - 1):
                current_card = temp[i]
                next_card = temp[i + 1]

                if current_card["value"] < next_card["value"]:
                    # Swap card contents
                    temp[i], temp[i + 1] = next_card, current_card
                    sort = False

    print(temp)


def can_joker_fill_set(card_set, num_joker_cards, required_count):
    """
    Checks if joker cards in hand can fill up a set
    :param card_set: card-set to check
    :param num_joker_cards: number of joker cards in hand
    :param required_count: number of cards needed for a complete set
    :return: True if set can be filled, False if not
    """
    if len(card_set) < required_count <= len(card_set) + num_joker_cards:
        return True

    return False


def joker_fill_set(card_set, required_count):
    """
    Fills the uncompleted set with joker cards
    :param card_set: card-set to fill
    :param required_count: number of cards needed for a complete set
    :return: filled card-set
    """
    while len(card_set) < required_count:
        card_set.append({"type": "joker", "color": "multi", "value": 1})

    return card_set


def count_joker_cards(hand):
    """
    Counts the joker cards in your hand
    :param hand: player hand
    :return: number of joker cards
    """
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
        move = build(move, last_topCard, hand, last_topCard)

    if last_topCard['type'] == 'reboot' or last_topCard['type'] == 'joker':
        move = handle_reboot_and_joker(move, hand)

    if last_topCard['type'] == 'see-through':
        move = handle_see_under_see(move, last_topCard, hand)

    return move


def handle_see_under_see(move, last_topCard, hand):
    """
    If top card and last top card are both see-through
    :param move: empty move
    :param last_topCard: a see-through card
    :param hand: player hand
    :return: built move
    """
    for card in hand:
        if last_topCard['color'] in card['color'].split("-"):
            move.update({'card1': card})
            move.update({'type': 'put'})
            move.update({'reason': 'See-Through under See-Through -> Same colored card as See-Through.'})
            return move

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
            move.update({'reason': 'Top-Card either reboot or joker -> Double-Colored.'})
            return move

    for card in hand:
        if card['type'] == 'number' and len(card['color'].split('-')) == 1:
            move.update({'card1': card})
            move.update({'type': 'put'})
            move.update({'reason': 'Top-Card either reboot or joker -> No 2 colored on hand -> Single colored.'})
            return move

    for card in hand:
        if not card['value'] or card['type'] == 'joker':
            move.update({'card1': card})
            move.update({'type': 'put'})
            move.update({'reason': 'Top-Card either reboot or joker -> No color on hand -> Joker.'})
            return move

    return move


# Example hand
# handTest = [
#     {"type": "number", "color": "red-green", "value": 2},
#     {"type": "number", "color": "green", "value": 1},
#     {"type": "reboot", "color": "multi", "value": None},
#     {"type": "joker", "color": "multi", "value": 1},
#     {"type": "number", "color": "blue-green", "value": 1},
#     {"type": "number", "color": "yellow", "value": 3},
#     {"type": "number", "color": "red", "value": 3},
#     {"type": "reboot", "color": "multi", "value": None},
#     {"type": "see-through", "color": "red", "value": None},
# ]
#
# top_cardTest = {"type": "number", "color": "green-red", "value": 2}
# last_topCardTest = {"type": "see-through", "color": "blue", "value": None}
# print_top_card_formatted(top_cardTest)
# moveTest = ai_player_build_move(handTest, top_cardTest, last_topCardTest, None)
# print_hand_formatted(handTest, 5)
