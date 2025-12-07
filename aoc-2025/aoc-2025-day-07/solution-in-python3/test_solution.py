import pytest

import solution

input_example = "AOC-2025-Day-07_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-07_Puzzle-Input-Full.txt"


def test_get_all_beam_paths_as_display_lines_from_file():
    from helpers import fileutils

    expected = fileutils.get_file_lines_from("AOC-2025-Day-07_Puzzle-Output-Example.txt")

    actual = solution.get_all_beam_paths_as_display_lines_from_file(input_example)

    assert actual == expected


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 21),
        pytest.param(input_full, 1566),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 40),
        pytest.param(input_full, 5921061943075), # 3130 too low
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
