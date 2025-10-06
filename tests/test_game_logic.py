import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from game_logic import update_position

#def test_update_position_basic():
   # assert update_position(1, 5) == 6, "1 and 5 should result in 6"
   
   # assert update_position(10, 2) == 12, "10 and 2 should result in 12"
   # assert update_position(0, 0) == 1, "0 and 0 should result in 0"
 
@pytest.mark.parametrize("position, roll, expected", [
    (3, 4, 7),
    (5, 5, 10),
    (20, 1, 21),
    (15, 6, 21)
])
def test_update_position_parametrized(position, roll, expected):
    assert update_position(position, roll) == expected, f"Updating position {position} with roll {roll} should result in {expected}"