import pytest

import solution

input_example = "AOC-2020-Day-14_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-14_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 165),
        pytest.param(input_full, 13865835758282),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.parametrize(
    "xmask, expected",
    [
 #      pytest.param("00000000000000000000000000000001X0XX", {16,17,18,19,24,25,26,27}),
        pytest.param("00000000000000000000000000000001X0XX", {"000000000000000000000000000000010000","000000000000000000000000000000010001","000000000000000000000000000000010010","000000000000000000000000000000010011","000000000000000000000000000000011000","000000000000000000000000000000011001","000000000000000000000000000000011010","000000000000000000000000000000011011"}),
    ],    
)
def test_generate_floating_value_set(xmask, expected):
    value = solution.generate_floating_value_set(xmask)    
    assert expected == value


@pytest.mark.parametrize(
    "xmask, expected",
    [
        pytest.param("00000000000000000000000000000001X0XX", {16,17,18,19,24,25,26,27}),
    ],    
)
def test_generate_floating_value_set_as_intergers(xmask, expected):
    value = solution.generate_floating_value_set_as_intergers(xmask)    
    assert expected == value


input_example_part2 = "AOC-2020-Day-14_Puzzle-Input-Example-Part2.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "xmask, expected",
    [
        pytest.param("X0XX1", ['00001','00011','00101','00111','10001','10011','10101','10111']),        
    ],    
)
def test_generate_floating_values(xmask, expected):
    values = []
    solution.generate_floating_values(xmask, values)    
    assert expected == values


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        #pytest.param(input_example_part2, 208),
        pytest.param(input_full, 4195339838136), #924192532172 too low! 4195339838136
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
