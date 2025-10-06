# debug_ladders.py
from game_logic import update_position

# quick checks for ladder tiles
tests = [
    (1, 4),   # 1 + 4 = 5 -> ladder 5 -> 15
    (3, 6),   # 3 + 6 = 9 -> ladder 9 -> 12
    (12, 6),  # 12 + 6 = 18 -> ladder 18 -> 23
]

for start, roll in tests:
    newpos = update_position(start, roll)
    print(f"start={start}, roll={roll} -> newpos={newpos}")
