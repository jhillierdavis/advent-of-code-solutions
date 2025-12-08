import pytest

import solution

input_example = "AOC-2025-Day-08_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-08_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, connections, expected",
    [
        pytest.param(input_example, 10, 40),
        pytest.param(input_full, 1000, 103488), # 302978000 too high , 26572
    ],    
)
def test_solve_part1(filename, connections, expected):
    value = solution.solve_part1(filename, connections)     
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 25272),
        pytest.param(input_full, 8759985540),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
