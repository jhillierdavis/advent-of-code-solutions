import pytest

import solution

@pytest.mark.parametrize(
    "filename,steps,expected",
    [
        pytest.param("puzzle-input-example.txt", 1, 2),
        pytest.param("puzzle-input-example.txt", 2, 4),
        #pytest.param("puzzle-input-example.txt", 3, 6),
        pytest.param("puzzle-input-example.txt", 6, 16),
        pytest.param("puzzle-input-full.txt", 64, -1), # 241 too low
    ],    
)
def test_solve_part1(filename, steps, expected):
    assert solution.solve_part1(filename, steps) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    