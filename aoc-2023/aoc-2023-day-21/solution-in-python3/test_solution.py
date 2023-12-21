import pytest

import solution

@pytest.mark.parametrize(
    "filename,steps,expected",
    [
        pytest.param("puzzle-input-example.txt", 1, 2),
        pytest.param("puzzle-input-example.txt", 2, 4),
        #pytest.param("puzzle-input-example.txt", 3, 6),
        pytest.param("puzzle-input-example.txt", 6, 16),
        pytest.param("puzzle-input-full.txt", 64, 3814), # 241 too low
    ],    
)
def test_solve_part1(filename, steps, expected):
    assert solution.solve_part1(filename, steps) == expected

@pytest.mark.parametrize(
    "filename, steps, expected",
    [
        pytest.param("puzzle-input-example.txt", 6, 16),
        pytest.param("puzzle-input-example.txt", 10, 50),
        #pytest.param("puzzle-input-example.txt", 50, 1594),
        #pytest.param("puzzle-input-example.txt", 100, 6536),
        #pytest.param("puzzle-input-example.txt", 500, 167004),
        #pytest.param("puzzle-input-example.txt", 1000, 668697),
        #pytest.param("puzzle-input-example.txt", 1000, 16733044),
        #pytest.param("puzzle-input-full.txt", 26501365, -1),
    ],    
)
def test_solve_part2(filename, steps, expected):
    assert solution.solve_part2(filename, steps) == expected    