import turtle

# Constants
TILE_SIZE = 125
BOARD_ROWS = 5
BOARD_COLS = 5
BOARD_START_X = -350
BOARD_START_Y = -350

# You can keep the same ladder/snake positions as game_logic.py
LADDERS = {5: 15, 9: 12, 18: 23}
SNAKES = {8: 3, 20: 1, 24: 14}


def get_tile_coords(tile):
    """Return the (x, y) coordinates of a tile center based on tile number (1-25)."""
    row = (tile - 1) // BOARD_COLS
    col = (tile - 1) % BOARD_COLS

    # Reverse direction every other row (snake pattern)
    if row % 2 == 1:
        col = BOARD_COLS - 1 - col

    x = BOARD_START_X + col * TILE_SIZE + TILE_SIZE / 2
    y = BOARD_START_Y + row * TILE_SIZE + TILE_SIZE / 2
    return x, y


def grid():
    """Draw the 5x5 board."""
    gridt1 = turtle.Turtle()
    gridt1.speed(0)
    gridt1.hideturtle()
    gridt1.penup()
    gridt1.goto(BOARD_START_X, BOARD_START_Y)
    gridt1.pendown()
    gridt1.pensize(5)

    def box(size):
        for _ in range(4):
            gridt1.forward(size)
            gridt1.left(90)

    def row(nos, size):
        for _ in range(nos):
            box(size)
            gridt1.forward(size)
        gridt1.penup()
        gridt1.left(180)
        gridt1.forward(nos * size)
        gridt1.left(180)
        gridt1.pendown()

    def draw_rows(aor, nos, size):
        for _ in range(aor):
            row(nos, size)
            gridt1.penup()
            gridt1.left(90)
            gridt1.forward(size)
            gridt1.right(90)
            gridt1.pendown()

    draw_rows(BOARD_ROWS, BOARD_COLS, TILE_SIZE)

        
def label_tiles():
    numbers = turtle.Turtle()
    numbers.hideturtle()
    numbers.speed(0)
    numbers.penup()
    
    start_x = -340
    start_y = -255
    tile_size = 125
    count = 1
    
    for row in range(5):
        for col in range(5):
            x = start_x + col * tile_size + 10
            y = start_y + row * tile_size + 10
            numbers.goto(x, y)
            numbers.write(str(count), font=("Arial", 12, "normal"))
            count += 1

    
def draw_snakes_and_ladders():
    """Draw ladder and snake images on the board."""
    screen = turtle.Screen()

    # Add shapes
    screen.addshape("assets/ladder.gif")
    screen.addshape("assets/snake.gif")

    # Draw ladders
    for start, end in LADDERS.items():
        ladder = turtle.Turtle()
        ladder.shape("assets/ladder.gif")
        ladder.penup()
        x1, y1 = get_tile_coords(start)
        x2, y2 = get_tile_coords(end)
        ladder.goto((x1 + x2) / 2, (y1 + y2) / 2)

    # Draw snakes
    for head, tail in SNAKES.items():
        snake = turtle.Turtle()
        snake.shape("assets/snake.gif")
        snake.penup()
        x1, y1 = get_tile_coords(head)
        x2, y2 = get_tile_coords(tail)
        snake.goto((x1 + x2) / 2, (y1 + y2) / 2)


def setup_players():
    """Initialize bull and cow player pieces."""
    screen = turtle.Screen()
    screen.addshape("assets/bull.gif")
    screen.addshape("assets/cow.gif")

    bull = turtle.Turtle()
    bull.shape("assets/bull.gif")
    bull.penup()
    bull.goto(*get_tile_coords(1))

    cow = turtle.Turtle()
    cow.shape("assets/cow.gif")
    cow.penup()
    x, y = get_tile_coords(1)
    cow.goto(x, y - 40)  # offset to avoid overlap

    return bull, cow


def setup_board():
    """Call all setup functions to draw the board and players."""
    turtle.setup(width=0.4, height=0.666, startx=1110, starty=0)
    turtle.title("Snakes & Ladders Game")
    turtle.bgcolor("#FFCC99")

    grid()
    label_tiles()
    draw_snakes_and_ladders()
    return setup_players()

def show_dice(roll_value):
    """Display dice image corresponding to roll_value at top of screen."""
    screen = turtle.Screen()
    
    # Add shapes only once (you can move this outside the function if you want)
    for i in range(1, 7):
        screen.addshape(f"assets/dice{i}.gif")

    # Create dice turtle
    dice_turtle = turtle.Turtle()
    dice_turtle.hideturtle()
    dice_turtle.penup()
    dice_turtle.goto(250, 250)  # top-right corner
    dice_turtle.shape(f"assets/dice{roll_value}.gif")
    dice_turtle.showturtle()
    
def show_win(player_name):
    screen = turtle.Screen()
    screen.addshape("assets/win.gif")
    win_turtle = turtle.Turtle()
    win_turtle.shape("assets/win.gif")
    win_turtle.penup()
    win_turtle.goto(0, 0)  # center of the screen
    win_turtle.st()
    print(f"{player_name} wins!")
    
def move_player(player_turtle, start, end, delay=0.2):
    """Animate player moving from start tile to end tile."""
    for tile in range(start + 1, end + 1):
        x, y = get_tile_coords(tile)
        player_turtle.goto(x, y)
        turtle.update()
        turtle.time.sleep(delay)
