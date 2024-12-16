import pytest


import solution

input_example = "AOC-2024-Day-16_Puzzle-Input-Example.txt"
input_example2 = "AOC-2024-Day-16_Puzzle-Input-Example-2.txt"
input_full = "AOC-2024-Day-16_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7036),
        pytest.param(input_example2, 11048),
        pytest.param(input_full,  90460),
    ],    
)
def test_solve_part1(filename, expected):
    #value = solution.solve_part1(filename)
    value = solution.solve_part1(filename)
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 45),
        #pytest.param(input_example2, 64),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value