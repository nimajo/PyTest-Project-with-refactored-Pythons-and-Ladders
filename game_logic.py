import random

def roll_dice():
    return random.randint(1, 6)


def update_position(position, roll_value):  
    return position + roll_value