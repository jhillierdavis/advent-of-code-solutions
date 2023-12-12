import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", -1),
    ],    
)
def test_solution(filename, expected):
    assert solution.solve(filename) == expected