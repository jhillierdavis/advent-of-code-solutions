import pytest

import solution

input_example = "AOC-2020-Day-03_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-03_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7),
        pytest.param(input_full, 228),
    ],    
)
def test_find_terms(filename, expected):
    value = solution.solve(filename)
    
    assert expected == value
