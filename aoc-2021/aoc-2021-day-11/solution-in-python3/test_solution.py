import pytest

import solution
import grid2d

def test_small_example():
    lines = ["11111","19991","19191","19991","11111"]
    grid = grid2d.lines_to_grid(lines)
    assert lines == grid2d.grid_to_lines(grid)

    solution.step(grid)

    expected = ["34543","40004","50005","40004","34543"]
    assert grid2d.grid_to_lines(grid) == expected


@pytest.mark.parametrize(
    "filename,steps,expected",
    [
        pytest.param("puzzle-input-example.txt", 10, 204),
        pytest.param("puzzle-input-example.txt", 100, 1656),
        pytest.param("puzzle-input-full.txt", 100, 1700),
    ],    
)
def test_part1_solution(filename, steps, expected):
    assert solution.count_flashes(filename, steps) ==  expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 195),
        pytest.param("puzzle-input-full.txt", 273),
    ],    
)

def test_part2_solution(filename, expected):
    assert solution.steps_to_all_flashing(filename) == expected
