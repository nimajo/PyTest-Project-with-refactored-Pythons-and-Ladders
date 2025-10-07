import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import dice_visual as dv

def get_dice_image(roll_value):
    return f"dice{roll_value}.gif"

@pytest.mark.parametrize("roll_value, expected_image", [
    (1, "assets/dice1.gif"),
    (2, "assets/dice2.gif"),
    (3, "assets/dice3.gif"),
    (4, "assets/dice4.gif"),
    (5, "assets/dice5.gif"),
    (6, "assets/dice6.gif"),
    (7, None),  # Invalid case
    (0, None),  # Invalid case
])
def test_get_dice_image(roll_value, expected_image):
    assert get_dice_image(roll_value) == expected_image