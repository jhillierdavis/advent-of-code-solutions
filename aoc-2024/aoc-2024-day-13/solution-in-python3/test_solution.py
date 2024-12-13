import pytest

import solution

input_example = "AOC-2024-Day-13_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-13_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "presses_A, presses_B, expected",
    [
        pytest.param(80, 40, 280),
        pytest.param(38, 86, 200),
    ],    
)
def test_calculcate_cost(presses_A, presses_B, expected):
    value = solution.calculate_cost(presses_A, presses_B)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 480),
        pytest.param(input_full, 35729),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, -1),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
