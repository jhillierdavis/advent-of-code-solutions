import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 94),
        pytest.param("puzzle-input-full.txt", 2250),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 154),
        #pythopytest.param("puzzle-input-full.txt", 6470), # Too slow! # TODO: Improve performance!
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    