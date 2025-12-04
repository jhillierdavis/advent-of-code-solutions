import pytest

import solution

input_example = "AOC-2025-Day-04_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-04_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 13),
        pytest.param(input_full, 1551),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 43),
        pytest.param(input_full, 9784),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
