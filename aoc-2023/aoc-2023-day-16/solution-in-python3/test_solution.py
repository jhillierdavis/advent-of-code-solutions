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
        pytest.param("puzzle-input-example.txt", 51),
        pytest.param("puzzle-input-full.txt", 6766), # 6679 too low!
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    