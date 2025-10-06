import turtle
from game_logic import roll_dice, update_position, check_win, WINNING_TILE
import board

# Setup the board and get player turtles
bull, cow = board.setup_board()

# Player positions
position1 = 1
position2 = 1
player_turn = 1  # 1 for bull, 2 for cow

# Text turtle for dice/score display
display_turtle = turtle.Turtle()
display_turtle.hideturtle()
display_turtle.penup()
display_turtle.goto(-50, 300)

# Main game loop
while True:
    if player_turn == 1:
        player_name = "Player 1"
        player_turtle = bull
        old_pos = position1
    else:
        player_name = "Player 2"
        player_turtle = cow
        old_pos = position2

    input(f"{player_name}, press Enter to roll the dice...")
    roll = roll_dice()
     # Show initial position before move
    new_pos = update_position(old_pos, roll)

    # Animate player movement
    board.show_dice(roll)
    board.move_player(player_turtle, old_pos, new_pos)

    # Show dice/position feedback
    display_turtle.clear()
    
    display_message = f"{player_name} rolled {roll}:    {old_pos} → {new_pos}"
    display_turtle.write(display_message, font=("Arial", 16, "bold"))

    # Update positions
    if player_turn == 1:
        position1 = new_pos
    else:
        position2 = new_pos

    # Check for win
    if check_win(new_pos):
        board.show_win(player_name)
        break

    # Switch turn
    player_turn = 2 if player_turn == 1 else 1

# Keep the window open after game ends
turtle.done()
