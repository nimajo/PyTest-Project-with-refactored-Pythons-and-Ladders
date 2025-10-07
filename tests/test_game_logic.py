import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import game_logic as gl


#### Roll dice test ######
def test_roll_dice():
    for x in range(100):  # Testing 100 times to ensure randomness
        roll = gl.roll_dice()
        assert 1 <= roll <= 6, f"Dice roll {roll} is out of bounds (1-6)"
########################


#### Parametrized test for update_position ######
@pytest.mark.parametrize("position, roll, expected", [
    (3, 4, 7), #normal move
    (5, 5, 10), #normal move
    (20, 1, 21), #normal move
    (15, 6, 21), #normal move
    (22, 4, 22),  # Test case where move exceeds winning tile
    (24, 2, 24),   # Test case where move exceeds winning tile
    (21,3,14),  # Test case where player hits a snake
    (4,1,15),   # Test case where player hits a ladder
    (23,2,25), #Test case where player wins
])
def test_update_position(position, roll, expected):
    assert gl.update_position(position, roll) == expected, f"Updating position {position} with roll {roll} should result in {expected}"
###################################################


### Winning Tile Check Test ######
@pytest.mark.parametrize("position, expected", [
    (25, True), #Winning position
    (24, False), #Not a winning position
    (1, False), #Not a winning position
    (0, False), #Not a winning position
])
def test_check_win(position, expected):
    assert gl.check_win(position) == expected, f"Position {position} win check failed"
    
def test_check_win_all_non_winning():    
    for x in range(1, 25):
        assert gl.check_win(x) == False, f"Position {x} should not be a winning position"
#######################################        
        