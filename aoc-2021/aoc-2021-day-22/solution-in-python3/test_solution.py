import pytest

import solution

input_example_small = "AOC-2021-Day-22_Puzzle-Input-Example-Small.txt"
input_example = "AOC-2021-Day-22_Puzzle-Input-Example.txt"
input_full = "AOC-2021-Day-22_Puzzle-Input-Full.txt"


def test_get_cubes_list():
    cubes = solution.get_cubes("x=10..12,y=10..12,z=10..12")
    assert len(cubes) == 27 # 3x3x3
    assert (10,10,10) in cubes
    assert (10,12,10) in cubes
    assert (11,11,11) in cubes
    assert (12,10,12) in cubes
    assert (12,12,12) in cubes


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_small, 39),
        pytest.param(input_example, 590784),
        pytest.param(input_full, 590467), 
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
