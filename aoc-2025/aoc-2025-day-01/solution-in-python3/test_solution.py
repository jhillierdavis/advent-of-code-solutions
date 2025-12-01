import pytest

import solution

input_example = "AOC-2025-Day-01_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-01_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3),
        pytest.param(input_full, 1180),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 6),
        pytest.param(input_full, 6892),
    ],    
)
def test_solve_part2(filename, expected):
    # Simple (brute force type) approach 
    value = solution.solve_part2_using_single_unit_increments(filename)    
    assert expected == value

    # Alternative approach using calculated offset
    value = solution.solve_part2_using_modular_arithemtic_offset(filename)    
    assert expected == value