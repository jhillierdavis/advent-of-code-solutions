import pytest

import solution

input_example = "AOC-2020-Day-10_Puzzle-Input-Example.txt"
input_example_larger = "AOC-2020-Day-10_Puzzle-Input-Example-Larger.txt"
input_full = "AOC-2020-Day-10_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "filename, increment, expected",
    [
        pytest.param(input_example, 1, 7),        
        pytest.param(input_example_larger, 1, 22),
        pytest.param(input_example, 3, 5),
        pytest.param(input_example_larger, 3, 10),
    ],    
)
def test_get_1_jolt_diffs(filename, increment, expected):
    adaptor_list = solution.get_sorted_ascending_adaptor_list(filename)
    value = solution.get_jolt_diffs(adaptor_list, increment)
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7*5),
        pytest.param(input_example_larger, 22*10),
        pytest.param(input_full, 2432),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 8),
        pytest.param(input_example_larger, 19208),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
