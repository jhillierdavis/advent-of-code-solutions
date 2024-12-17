import pytest

import solution

input_example = "AOC-2024-Day-17_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-17_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "reg_a, reg_b, reg_c, input, expected_reg_a, expected_reg_b, expected_reg_c, expected_output",
    [
        pytest.param(0,0,9,"2,6",0,1,9,None),
        pytest.param(10,0,0,"5,0,5,1,5,4",10,0,0,"0,1,2"),
        pytest.param(2024,0,0,"0,1,5,4,3,0",0,0,0,"4,2,5,6,7,7,7,7,3,1,0"),
        pytest.param(0,2024,43690,"4,0",0,44354,43690,""),
        pytest.param(0,29,0,"1,7",0,26,0,""),
        pytest.param(2024,0,0,"0,3,5,4,3,0",0,0,0,"5,7,3,0"),
        pytest.param(2024,0,0,"0,3,5,4,3,0",0,0,0,"5,7,3,0"),
        pytest.param(117440,0,0,"0,3,5,4,3,0",0,0,0,"0,3,5,4,3,0"),
    ],    
)
def test_process_string_of_instructions(reg_a, reg_b, reg_c, input, expected_reg_a, expected_reg_b, expected_reg_c, expected_output):
    reg_map = {}
    reg_map['A'] = reg_a
    reg_map['B'] = reg_b
    reg_map['C'] = reg_c

    output = solution.process_string_of_instructions(input, reg_map)
    
    assert reg_map['A'] == expected_reg_a
    assert reg_map['B'] == expected_reg_b
    assert reg_map['C'] == expected_reg_c
    if None != expected_output:
        assert output == expected_output


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, "4,6,3,5,6,3,5,2,1,0"),
        pytest.param(input_full, "3,1,4,3,1,7,1,6,3"),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param([0,3,5,4,3,0], 117440),
        pytest.param([2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0], 37221270076916),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value