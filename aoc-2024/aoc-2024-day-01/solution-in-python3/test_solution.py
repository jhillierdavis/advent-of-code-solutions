import pytest

import solution

input_example = "AOC-2024-Day-01_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-01_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 11),
        pytest.param(input_full, 1882714),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 31),
        pytest.param(input_full, 19437052),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
