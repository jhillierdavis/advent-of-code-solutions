# test_grid_at_count.py
import pytest
from ai_solution_part_1 import count_sparse_at_points, solve_from_text

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

def test_example_count():
    grid = EXAMPLE_GRID.strip().splitlines()
    assert count_sparse_at_points(grid) == 13

def test_example_with_wrapper():
    assert solve_from_text(EXAMPLE_GRID) == 13

def test_single_point():
    grid = ["@"]
    # No neighbours at all, so fewer than 4
    assert count_sparse_at_points(grid) == 1

def test_fully_surrounded_point():
    grid = [
        "@@@",
        "@@@",
        "@@@"
    ]
    # Center has 8 neighbours, excluded
    # Corners have 3 neighbours, edges have 5 neighbours
    # All corners and edges have fewer than 4? No, only corners do.
    # So 4 corners counted.
    assert count_sparse_at_points(grid) == 4
