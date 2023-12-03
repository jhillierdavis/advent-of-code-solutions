import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 4361),
        pytest.param('puzzle-input-full.txt', 530495),
    ],    
)
def test_solution_part1(input, expected):
    assert solution.solve_part1(input) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 467835), 
        pytest.param('puzzle-input-full.txt', 80253814),        
    ],    
)
def test_solution_part2(input, expected):
    assert solution.solve_part2(input) == expected    