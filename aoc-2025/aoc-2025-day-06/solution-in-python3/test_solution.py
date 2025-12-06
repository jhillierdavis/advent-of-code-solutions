import pytest

import solution, hyperneutrino_solution

input_example = "AOC-2025-Day-06_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-06_Puzzle-Input-Full.txt"


def test_get_column_widths():
    input_lines = ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314', '*   +   *   +  ']
    actual = solution.get_column_widths(input_lines)
    assert actual == [4,4,4,3]


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4277556),
        pytest.param(input_full, 6169101504608),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    assert expected == value

    # Solutions from others (for comparison, learning etc.)
    value = hyperneutrino_solution.solve_part1(filename)
    assert expected == value


@pytest.mark.parametrize(
    "nums, idx, expected",
    [
        pytest.param(['123', ' 45', '  6'], 0, 1),
        pytest.param(['123', ' 45', '  6'], 1, 24),
        pytest.param(['123', ' 45', '  6'], 2, 356),
        pytest.param(['328', '64 ', '98 '], 0, 369),
        pytest.param(['328', '64 ', '98 '], 1, 248),
        pytest.param(['328', '64 ', '98 '], 2, 8),
        pytest.param([' 51', '387', '215'], 0, 32),
        pytest.param([' 51', '387', '215'], 1, 581),
        pytest.param([' 51', '387', '215'], 2, 175),
        pytest.param(['64 ', '23 ', '314'], 0, 623),
        pytest.param(['64 ', '23 ', '314'], 1, 431),
        pytest.param(['64 ', '23 ', '314'], 2, 4),
    ],    
)
def test_column_number_value_at_index(nums, idx, expected):
    value = solution.column_number_value_at_index(nums, idx)
    assert value == expected


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3263827),
        pytest.param(input_full, 10442199710797),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value

    # Solutions from others (for comparison, learning etc.)
    value = hyperneutrino_solution.solve_part2(filename)
    assert expected == value

