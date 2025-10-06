import turtle

def show_dice(roll_value):
    """Show a dice GIF matching the roll."""
    screen = turtle.Screen()
    dice = turtle.Turtle()
    dice.penup()
    dice.goto(325, 240)
    screen.addshape(f"dice{roll_value}.gif")
    dice.shape(f"dice{roll_value}.gif")
    dice.st()
    
def create_player(image_path, start_x, start_y):
    screen = turtle.Screen()
    screen.addshape(image_path)
    t = turtle.Turtle()
    t.shape(image_path)
    t.penup()
    t.goto(start_x, start_y)
    return t