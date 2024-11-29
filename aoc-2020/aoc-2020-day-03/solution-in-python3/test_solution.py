import pytest

import solution

input_example = "AOC-2020-Day-03_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-03_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7),
        pytest.param(input_full, 228),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 336),
        pytest.param(input_full, 6818112000),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value   