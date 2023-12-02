import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 8),
        pytest.param('puzzle-input-full.txt', 2162),
    ],    
)
def test_solution(input, expected):

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    assert solution.solve(input) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 2286),
        pytest.param('puzzle-input-full.txt', 72513),
    ],    
)
def test_solution_part2(input, expected):

    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    assert solution.solve_part2(input) == expected    