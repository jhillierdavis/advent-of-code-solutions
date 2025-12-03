import pytest

import solution

input_example = "AOC-2025-Day-03_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-03_Puzzle-Input-Full.txt"

"""
@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param('987654321111111', 98),
        pytest.param('811111111111119', 89),
        pytest.param('234234234234278', 78),
        pytest.param('818181911112111', 92),
    ],    
)
def test_get_max_joltage(value, expected):
    value = solution.get_largest_joltage(value, 2)
    assert expected == value
"""

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 357),
        pytest.param(input_full, 17445),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "value, size, expected",
    [
        pytest.param('987654321111111', 2, 98),
        pytest.param('811111111111119', 2, 89),
        pytest.param('234234234234278', 2, 78),
        pytest.param('818181911112111', 2, 92),
        pytest.param('987654321111111', 12, 987654321111),
        pytest.param('811111111111119', 12, 811111111119),
        pytest.param('234234234234278', 12, 434234234278),
        pytest.param('818181911112111', 12, 888911112111),
    ],    
)
def test_get_largest_joltage(value, size, expected):
    value = solution.get_largest_joltage(value, size)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3121910778619),
        pytest.param(input_full, 173229689350551),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
