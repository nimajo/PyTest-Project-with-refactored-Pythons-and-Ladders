import random



#Rolling a six-sided dice
def roll_dice():
    return random.randint(1, 6)


#Position of snakes and ladders on the board and winning tile
SNAKES = {8:3, 20:1, 24:14}
LADDERS = {5:15, 9:12, 18:23}
WINNING_TILE = 25



def update_position(current_position, roll_value):
    """Return new position after applying snakes/ladders."""
    new_position = current_position + roll_value

    if new_position > WINNING_TILE:
        return current_position  # must roll exact number to win

    # apply snakes/ladders
    if new_position in SNAKES:
        new_position = SNAKES[new_position]
    elif new_position in LADDERS:
        new_position = LADDERS[new_position]

    return new_position


def check_win(position):
    """Return True if player has won."""
    return position == WINNING_TILE

