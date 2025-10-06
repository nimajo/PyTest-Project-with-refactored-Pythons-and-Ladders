import random



#Rolling a six-sided dice
def roll_dice():
    return random.randint(1, 6)


#Position of snakes and ladders on the board
SNAKES = {8:3, 20:1, 24:14}
LADDERS = {5:15, 9:12, 18:23}



#Updating player position based on dice roll
def update_position(current_position, roll_value):  
    new_position = current_position + roll_value
    if new_position in SNAKES:
        new_position = SNAKES[new_position]
    elif new_position in LADDERS:
        new_position = LADDERS[new_position]
    return new_position
