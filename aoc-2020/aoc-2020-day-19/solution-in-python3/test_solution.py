import pytest

import solution

input_example = "AOC-2020-Day-19_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-19_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "message, expected",
    [
        pytest.param('ababbb', True),
        pytest.param('abbbab', True),
        pytest.param('bababa', False),
        pytest.param('aaabbb', False),
        pytest.param('aaaabbb', False),
    ],    
)

def test_is_valid_message(message, expected):
    
    lines = ['0: 4 1 5', '1: 2 3 | 3 2', '2: 4 4 | 5 5', '3: 4 5 | 5 4', '4: "a"', '5: "b"']
    rule_map = solution.create_rule_map_from_lines(lines)

    assert expected == solution.is_valid_message(rule_map, message)



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2),
        pytest.param(input_full, 226),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


input_example_part2 = "AOC-2020-Day-19_Puzzle-Input-Example-Part2.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, 3),
        #pytest.param(input_full, -1),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
