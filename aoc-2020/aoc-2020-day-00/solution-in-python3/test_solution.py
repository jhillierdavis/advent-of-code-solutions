import pytest

import solution

input_example = "AOC-2020-Day-00_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-00_Puzzle-Input-Full.txt"

# Ignore / skip
@pytest.mark.skip(reason="TODO: Implement")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, -1),
        #pytest.param(input_full, -1),
    ],    
)
def test_find_terms(filename, expected):
    value = solution.solve(filename)
    
    assert expected == value
