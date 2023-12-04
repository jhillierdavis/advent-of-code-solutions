import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 13),
        pytest.param('puzzle-input-full.txt', 26914), # Not 1538
    ],    
)
def test_solution_part1(input, expected):
    assert solution.solve_part1(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 30),
        pytest.param('puzzle-input-full.txt', 13080971),
    ],    
)
def test_solution_part2(input, expected):
    assert solution.solve_part2(input) == expected    