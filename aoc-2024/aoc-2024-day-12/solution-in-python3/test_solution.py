import pytest

from helpers import fileutils, grid
import solution

example_1 = "example-1.txt"
example_2 = "example-2.txt"
example_3 = "example-3.txt"
example_4 = "example-4.txt"
input_example = "AOC-2024-Day-12_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-12_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(example_1, 5),
        pytest.param(example_2, 5),
        pytest.param(input_example, 11),
    ],    
)
def test_count_regions(filename, expected):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    assert expected == solution.count_regions(g)


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(example_1, 140),
        pytest.param(example_2, 772),
        pytest.param(input_example, 1930),
        pytest.param(input_full, 1396562), # TODO: A bit slow, improve performance
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(example_1, 80),
        pytest.param(example_2, 436),
        pytest.param(example_3, 236),
        pytest.param(example_4, 368),
        pytest.param(input_example, 1206),
        pytest.param(input_full, 844132), # TODO: A bit slow, improve performance
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value