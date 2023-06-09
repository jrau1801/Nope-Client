
def print_move_formatted(move):
    for key, value in move.items():
        if isinstance(value, dict):
            value = ' : '.join(str(v) for v in value.values())
        print(f'{key}: {value}')
