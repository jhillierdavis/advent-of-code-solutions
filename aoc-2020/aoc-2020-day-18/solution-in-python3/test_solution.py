import pytest

import solution

input_example = "AOC-2020-Day-18_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-18_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "expression, expected",
    [
        pytest.param("1 + 2 * 3 + 4 * 5 + 6", 71),
        pytest.param("1 + (2 * 3)", 7),
        pytest.param("4 * (5 + 6)", 44),
        pytest.param("(4 * (5 + 6))", 44),
        pytest.param("1 + (2 * 3) + (4 * (5 + 6))", 51),
        pytest.param("2 * 3 + (4 * 5)", 26),
        pytest.param("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
        pytest.param("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
        pytest.param("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
    ],    
)
def test_compute_expression(expression, expected):
    value = solution.compute_expression(expression)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 71 + 51 + 26 + 437 + 12240 + 13632), # 26457
        pytest.param(input_full, 6811433855019),
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
