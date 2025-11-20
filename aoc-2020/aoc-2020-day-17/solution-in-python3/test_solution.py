import pytest

import solution

input_example = "AOC-2020-Day-17_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-17_Puzzle-Input-Full.txt"

from helpers import point


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, cycles, expected",
    [
        pytest.param(input_example, 0, 5),
        pytest.param(input_example, 1, 11),
        pytest.param(input_example, 2, 21),
        pytest.param(input_example, 3, 38),
        pytest.param(input_example, 6, 112),
        pytest.param(input_full, 6, 448),
    ],    
)
def test_solve_part1(filename, cycles, expected):
    value = solution.solve_part1(filename, cycles)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, cycles, expected",
    [
        pytest.param(input_example, 0, 5),
        pytest.param(input_example, 1, 29),
        pytest.param(input_example, 6, 848),
        pytest.param(input_full, 6, 2400),
    ],    
)
def test_solve_part2(filename, cycles, expected):
    value = solution.solve_part2(filename, cycles)    
    assert expected == value
