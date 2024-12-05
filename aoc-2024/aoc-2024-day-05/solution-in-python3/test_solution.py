import pytest

import solution

input_example = "AOC-2024-Day-05_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-05_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "int_array, expected",
    [
        pytest.param([75,47,61,53,29], 61),
        pytest.param([97,61,53,29,13], 53),
        pytest.param([75,29,13], 29),
    ],    
)
def test_get_middle_value(int_array, expected):
    value = solution.get_middle_value(int_array)   
    assert expected == value

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 143),
        pytest.param(input_full, 7307),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 123),
        pytest.param(input_full, 4713), # 4713 # 4454 too low!, 4738 too high!
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
