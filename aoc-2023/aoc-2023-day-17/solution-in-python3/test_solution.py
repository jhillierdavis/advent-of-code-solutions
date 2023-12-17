import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 102),
        pytest.param("puzzle-input-full.txt", 767), # 748 too low!
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 94),
        #pytest.param("puzzle-input-example-part2.txt", 71), # 47?
        pytest.param("puzzle-input-full.txt", -1), # 902 too low! #987 too high!
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    