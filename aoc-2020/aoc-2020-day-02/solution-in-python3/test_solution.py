import pytest

import solution

input_example = "AOC-2020-Day-02_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-02_Puzzle-Input-Full.txt"

@pytest.mark.parametrize(
    "str_input, char, expected",
    [
        pytest.param("abcde", 'a', 1),
        pytest.param("cdefg", 'b', 0),
        pytest.param("ccccccccc", 'c', 9),
    ],    
)
def test_count_chars(str_input, char, expected):
    assert expected == solution.get_char_count(str_input, char)


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 2),
        pytest.param(input_full, 643),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)

    assert expected == value

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1),
        pytest.param(input_full, 388),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)

    assert expected == value 