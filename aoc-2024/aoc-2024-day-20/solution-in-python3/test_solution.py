import pytest

from helpers import fileutils, grid, point
import solution

input_example = "AOC-2024-Day-20_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-20_Puzzle-Input-Full.txt"

input_example_cheat_1 = "example_1_cheat.txt"
input_example_cheat_2 = "example_2_cheat.txt"
input_example_cheat_3 = "example_3_cheat.txt"
input_example_cheat_4 = "example_4_cheat.txt"


import solution_part2


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 84),
        pytest.param(input_full, 9420),
        pytest.param(input_example_cheat_1, 72),
        pytest.param(input_example_cheat_2, 64),
        pytest.param(input_example_cheat_3, 84 - 38),
        pytest.param(input_example_cheat_4, 84 - 64),

    ],    
)
def test_get_shortest_path(filename, expected):
    # When
    path = solution_part2.get_path(filename)    
    size = len(path) - 1 # Deduct 1 for starting point

    # Then
    assert expected == size


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, saving, expected",
    [
        pytest.param(input_example, 2, 14),
        pytest.param(input_example, 4, 14),
        pytest.param(input_example, 6, 2),
        pytest.param(input_example, 8, 4),
        pytest.param(input_example, 10, 2),
        pytest.param(input_example, 12, 3),
        pytest.param(input_example, 20, 1),
        pytest.param(input_example, 36, 1),
        pytest.param(input_example, 38, 1),
        pytest.param(input_example, 40, 1),
        pytest.param(input_example, 64, 1),
    ],    
)
def test_count_number_of_cheats_for_saving(filename, saving, expected):
    value = solution_part2.count_number_of_cheats_for_exact_saving(filename, saving, 2)    
    assert expected == value


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, saving, duration, expected",
    [
        pytest.param(input_example, 64, 2, 1),
        pytest.param(input_full, 100, 2, 1454) # Still a bit slow
    ],    
)
def test_solve_part1(filename, saving, duration, expected):
    value = solution_part2.count_number_of_cheats_for_saving_or_less(filename, saving, duration)    
    assert expected == value


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, saving, duration, expected",
    [
        pytest.param(input_full, 100, 20, 997879), # Still a bit slow
    ],    
)
def test_solve_part2(filename, saving, duration, expected):
    value = solution_part2.count_number_of_cheats_for_saving_or_less(filename, saving, duration)    
    assert expected == value