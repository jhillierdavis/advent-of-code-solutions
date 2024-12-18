import pytest

import solution

input_example = "AOC-2024-Day-18_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-18_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, size, fallen, expected",
    [
        pytest.param(input_example, 7, 12, 22),
        pytest.param(input_full, 71, 1024, 252),
    ],    
)
def test_solve_part1(filename, size, fallen, expected):
    value = solution.solve_part1(filename, fallen, size)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, size, expected",
    [
        pytest.param(input_example, 7, (6,1)),
        pytest.param(input_full, 71, (5,60)),
    ],    
)
def test_solve_part2(filename, size, expected):
    value = solution.solve_part2(filename, size)    
    assert expected == value