import pytest

import solution

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
