import pytest

import solution

@pytest.mark.parametrize(
    "filename, loops, expected",
    [
        pytest.param("puzzle-input-example.txt", 1, 32), # 8 * 4
        pytest.param("puzzle-input-example.txt", 1000, 32000000), # 8000 * 4000
        #pytest.param("puzzle-input-example-more-interesting.txt", 4, -1), # 8000 * 4000
        pytest.param("puzzle-input-example-more-interesting.txt", 1000, 11687500),
        pytest.param("puzzle-input-full.txt", 1000, 670984704),
    ],    
)
def test_solve_part1(filename, loops, expected):
    assert solution.solve_part1(filename, loops) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    