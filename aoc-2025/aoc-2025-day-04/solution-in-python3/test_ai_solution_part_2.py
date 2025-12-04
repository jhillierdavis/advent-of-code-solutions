# test_grid_replace.py
import pytest
from ai_solution_part_2 import iterative_replace

EXAMPLE_GRID = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def test_example_iterative_replace():
    assert iterative_replace(EXAMPLE_GRID) == 43

def test_single_point():
    grid = "@"
    # Single '@' has 0 neighbours, replaced in one iteration
    assert iterative_replace(grid) == 1

def test_fully_surrounded_point():
    grid = "\n".join([
        "@@@",
        "@@@",
        "@@@"
    ])
    # Corners have 3 neighbours, replaced first
    # Then edges become sparse, replaced next
    # Finally center becomes sparse, replaced last
    # All 9 replaced in total
    assert iterative_replace(grid) == 9
