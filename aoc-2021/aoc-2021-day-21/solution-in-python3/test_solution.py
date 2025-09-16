import pytest

import solution

input_example = "AOC-2021-Day-00_Puzzle-Input-Example.txt"
input_full = "AOC-2021-Day-00_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "starting_positions, expected",
    [
        pytest.param([4,8], 739785),
        pytest.param([7,9], 679329),
    ],    
)
def test_solve_part1(starting_positions, expected):
    value = solution.solve_part1(starting_positions)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "starting_positions, expected",
    [
        pytest.param([4,8], 444356092776315),
        pytest.param([7,9], 433315766324816),
    ],    
)
def test_solve_part2(starting_positions, expected):
    value = solution.solve_part2(starting_positions)
    
    assert expected == value
