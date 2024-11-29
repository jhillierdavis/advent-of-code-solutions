import pytest

import solution

input_example = "AOC-2020-Day-04_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-04_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2),
        pytest.param(input_full, 245),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value

@pytest.mark.parametrize(
    "filename, expected",
    [
        #pytest.param(input_example, 2),
        pytest.param(input_full, "TODO"),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value   
