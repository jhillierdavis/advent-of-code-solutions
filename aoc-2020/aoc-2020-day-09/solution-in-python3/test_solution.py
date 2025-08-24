import pytest

import solution

input_example = "AOC-2020-Day-09_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-09_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, preamble, expected",
    [
        pytest.param(input_example, 5, 127),
        pytest.param(input_full, 25, 144381670),
    ],    
)
def test_solve_part1(filename, preamble, expected):
    value = solution.solve_part1(filename, preamble)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, -1),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
