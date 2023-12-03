import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 4361),
        pytest.param('puzzle-input-full.txt', 409971),
    ],    
)
def test_solution(input, expected):
    assert solution.solve(input) == expected