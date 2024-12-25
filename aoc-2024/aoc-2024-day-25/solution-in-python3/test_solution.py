import pytest

import solution

input_example = "AOC-2024-Day-25_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-25_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3),
        pytest.param(input_full, 2586),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


# NB: Part 2 is completion (both parts 1 & 2) of all prior 2024 puzzle days