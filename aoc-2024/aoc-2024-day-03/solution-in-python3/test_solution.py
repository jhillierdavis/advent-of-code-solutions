import pytest

import solution

input_example_part1 = "AOC-2024-Day-03_Puzzle-Input-Example-Part1.txt"
input_full = "AOC-2024-Day-03_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part1, 161),
        pytest.param(input_full, 173419328), # not 31748124!
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


input_example_part2 = "AOC-2024-Day-03_Puzzle-Input-Example-Part2.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, 48),
        pytest.param(input_full, 90669332),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
