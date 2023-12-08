import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("puzzle-input-example.txt", 6),
        pytest.param("puzzle-input-full.txt", 11567),
    ],    
)
def test_solution_part1(input, expected):
    assert solution.solve_part1(input) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("puzzle-input-example-part2.txt", 6),
        pytest.param("puzzle-input-full.txt", 9858474970153),
    ],    
)
def test_solution_part2(input, expected):
    assert solution.solve_part2(input) == expected    