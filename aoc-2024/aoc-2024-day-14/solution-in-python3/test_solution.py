import pytest

import solution

input_example = "AOC-2024-Day-14_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-14_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, width, height, expected",
    [
        pytest.param(input_example, 11, 7, 12),
        pytest.param(input_full, 101, 103, 229980828), # 500 too low
    ],    
)
def test_solve_part1(filename, width, height, expected):
    value = solution.solve_part1(filename,  width, height)
    
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
