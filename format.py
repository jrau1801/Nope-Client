def print_move_formatted(move):
    """
    Prints a formatted move for clearer output
    :param move: move to print
    :return: returns nothing
    """
    print(f"\n{Color.GREEN_BACKGROUND} - {Color.BLACK_BOLD} MOVE: {Color.RESET}")
    for key, value in move.items():
        if isinstance(value, dict):
            value = ' : '.join(str(v) for v in value.values())
        print(f'{Color.GREEN_BACKGROUND} + {Color.BLACK_BOLD} {key}: {value} {Color.RESET}')


def print_hand_formatted(hand, opp_hand_size):
    """
    Prints a formatted hand for clearer output
    :param opp_hand_size: number of cards opponent has
    :param hand: hand to print
    :return: returns nothing
    """
    print(f"\n{Color.BLUE_BACKGROUND_BRIGHT} - {Color.BLACK_BOLD} YOUR HAND: {Color.RESET}\t\t\t\t\t\t"
          f"{Color.BLUE_BACKGROUND_BRIGHT} - {Color.BLACK_BOLD} Opponent Cards: {opp_hand_size} {Color.RESET}")
    for card in hand:
        print(f"{Color.BLUE_BACKGROUND_BRIGHT} + {Color.BLACK_BOLD} {card['type']} : {card['color']} : {card['value']} "
              f"{Color.RESET}")


def print_top_card_formatted(top_card, prefix=""):
    """
    Prints a formatted top-card for clearer output
    :param prefix: add before top-card print
    :param top_card: top-card to print
    :return: returns nothing
    """
    print(f"\n{Color.CYAN_BACKGROUND} - {Color.BLACK_BOLD} {prefix}TOP-CARD: {Color.RESET}")
    print(
        f"{Color.CYAN_BACKGROUND} + {Color.BLACK_BOLD} {top_card['type']} : {top_card['color']} : {top_card['value']} "
        f"{Color.RESET}")


def print_menu():
    print(f"{Color.BLUE_BOLD}[1] Create Tournament\n"
          "[2] Join Tournament\n"
          "[3] Leave Tournament\n"
          "[4] Start Tournament\n"
          f"[5] Disconnect: {Color.RESET}")


# ANSI escape codes for text colors and formatting
class Color:
    """
    Colors and Background-Colors in many different variations
    """
    RESET = "\033[0m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PINK = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"

    # Bold
    BLACK_BOLD = "\033[1;30m"
    RED_BOLD = "\033[1;31m"
    GREEN_BOLD = "\033[1;32m"
    YELLOW_BOLD = "\033[1;33m"
    BLUE_BOLD = "\033[1;34m"
    PINK_BOLD = "\033[1;35m"
    CYAN_BOLD = "\033[1;36m"
    WHITE_BOLD = "\033[1;37m"

    # Underline
    BLACK_UNDERLINED = "\033[4;30m"
    RED_UNDERLINED = "\033[4;31m"
    GREEN_UNDERLINED = "\033[4;32m"
    YELLOW_UNDERLINED = "\033[4;33m"
    BLUE_UNDERLINED = "\033[4;34m"
    PINK_UNDERLINED = "\033[4;35m"
    CYAN_UNDERLINED = "\033[4;36m"
    WHITE_UNDERLINED = "\033[4;37m"

    # Background
    BLACK_BACKGROUND = "\033[40m"
    RED_BACKGROUND = "\033[41m"
    GREEN_BACKGROUND = "\033[42m"
    YELLOW_BACKGROUND = "\033[43m"
    BLUE_BACKGROUND = "\033[44m"
    PINK_BACKGROUND = "\033[45m"
    CYAN_BACKGROUND = "\033[46m"
    WHITE_BACKGROUND = "\033[47m"

    # High Intensity
    BLACK_BRIGHT = "\033[0;90m"
    RED_BRIGHT = "\033[0;91m"
    GREEN_BRIGHT = "\033[0;92m"
    YELLOW_BRIGHT = "\033[0;93m"
    BLUE_BRIGHT = "\033[0;94m"
    PINK_BRIGHT = "\033[0;95m"
    CYAN_BRIGHT = "\033[0;96m"
    WHITE_BRIGHT = "\033[0;97m"

    # Bold High Intensity
    BLACK_BOLD_BRIGHT = "\033[1;90m"
    RED_BOLD_BRIGHT = "\033[1;91m"
    GREEN_BOLD_BRIGHT = "\033[1;92m"
    YELLOW_BOLD_BRIGHT = "\033[1;93m"
    BLUE_BOLD_BRIGHT = "\033[1;94m"
    PINK_BOLD_BRIGHT = "\033[1;95m"
    CYAN_BOLD_BRIGHT = "\033[1;96m"
    WHITE_BOLD_BRIGHT = "\033[1;97m"

    # High Intensity backgrounds
    BLACK_BACKGROUND_BRIGHT = "\033[0;100m"
    RED_BACKGROUND_BRIGHT = "\033[0;101m"
    GREEN_BACKGROUND_BRIGHT = "\033[0;102m"
    YELLOW_BACKGROUND_BRIGHT = "\033[0;103m"
    BLUE_BACKGROUND_BRIGHT = "\033[0;104m"
    PINK_BACKGROUND_BRIGHT = "\033[0;105m"
    CYAN_BACKGROUND_BRIGHT = "\033[0;106m"
    WHITE_BACKGROUND_BRIGHT = "\033[0;107m"
