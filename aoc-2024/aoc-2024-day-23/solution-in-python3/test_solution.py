import pytest

import solution

input_example = "AOC-2024-Day-23_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-23_Puzzle-Input-Full.txt"




@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 12),
        pytest.param(input_full, 11011),
    ],    
)
def test_get_triple_connections(filename, expected):
    value = solution.get_triple_connections(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7),
        pytest.param(input_full, 1302),
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
