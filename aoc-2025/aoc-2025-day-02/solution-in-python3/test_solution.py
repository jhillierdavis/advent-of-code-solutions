import pytest

import solution

input_example = "AOC-2025-Day-02_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-02_Puzzle-Input-Full.txt"

    
#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1227775554),
        pytest.param(input_full, 12850231731),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4174379265),
        pytest.param(input_full, 24774350322),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value