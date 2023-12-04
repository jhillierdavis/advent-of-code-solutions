import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 13),
        pytest.param('puzzle-input-full.txt', 0), # Not 1538
    ],    
)
def test_solution(input, expected):
    assert solution.solve(input) == expected