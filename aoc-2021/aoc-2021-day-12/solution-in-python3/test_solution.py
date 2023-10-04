import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-1.txt", 10),
        pytest.param("puzzle-input-example-2.txt", 19),
        pytest.param("puzzle-input-example-3.txt", 226),
        # pytest.param("puzzle-input-full.txt", -1), # Unknown currently
    ],    
)
def test_part1_solution(filename, expected):
    assert solution.count_paths(filename) ==  expected