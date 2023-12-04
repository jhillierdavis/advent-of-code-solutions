import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param(input, True),
    ],    
)
def test_solution(input, expected):
    assert solution.solve(input) == expected