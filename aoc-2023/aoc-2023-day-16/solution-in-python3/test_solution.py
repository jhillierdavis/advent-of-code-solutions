import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 46),
        pytest.param("puzzle-input-full.txt", 6605),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    