import pytest

import solution

input_example = "AOC-2020-Day-16_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-16_Puzzle-Input-Full.txt"



@pytest.mark.parametrize(
    "value, min, max, expected",
    [
        pytest.param(5, 1, 10, True),
        pytest.param(0, 1, 10, False),
        pytest.param(10, 1, 10, True),
    ],    
)
def test_is_within_range(value, min, max, expected):
    value = solution.is_within_range(value, min, max)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 71),
        pytest.param(input_full, 25059),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
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
