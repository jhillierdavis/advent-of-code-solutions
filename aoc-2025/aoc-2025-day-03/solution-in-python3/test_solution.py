import pytest

import solution

input_example = "AOC-2025-Day-03_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-03_Puzzle-Input-Full.txt"


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
    value = solution.get_max_joltage(value)    
    assert expected == value


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
    "value, expected",
    [
        pytest.param('987654321111111', 987654321111),
        pytest.param('811111111111119', 811111111119),
        pytest.param('234234234234278', 434234234278),
        pytest.param('818181911112111', 888911112111),
    ],    
)
def test_get_largest_joltage(value, expected):
    value = solution.get_largest_joltage(value)    
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
