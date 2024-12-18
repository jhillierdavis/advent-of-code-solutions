import pytest

import solution
from helpers import fileutils, grid

input_example_small = "AOC-2024-Day-15_Puzzle-Input-Example-Small.txt"
input_example_small_end_state = "AOC-2024-Day-15_Puzzle-Input-Example-Small_End-State.txt"
input_example = "AOC-2024-Day-15_Puzzle-Input-Example.txt"
input_example_end_state = "AOC-2024-Day-15_Puzzle-Input-Example_End-State.txt"
input_full = "AOC-2024-Day-15_Puzzle-Input-Full.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_small_end_state, 2028),
        pytest.param(input_example_end_state, 10092),
    ],    
)
def test_calculate_sum_box_gps_coords(filename, expected):
    g = grid.lines_to_grid(fileutils.get_file_lines(filename))
    assert expected == solution.calculate_sum_box_gps_coords(g)


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename_start_state, filename_end_state, expected",
    [
        pytest.param(input_example_small, input_example_small_end_state, True),
        pytest.param(input_example, input_example_end_state, True),
    ],    
)
def test_end_state(filename_start_state, filename_end_state, expected):
    value = solution.end_state(filename_start_state, filename_end_state)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_small, 2028),
        pytest.param(input_example, 10092),
        pytest.param(input_full, 1499739), # 1494211 Too low!
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


input_example_second_warehouse = "AOC-2024-Day-15_Puzzle-Input-Example-Second-Warehouse.txt"

import solution_part2

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, filename_example_second_warehouse",
    [
        pytest.param(input_example, input_example_second_warehouse),
    ],    
)
def test_generate_second_warehouse(filename, filename_example_second_warehouse):
    expected = grid.lines_to_grid(fileutils.get_file_lines(filename_example_second_warehouse))

    #g = solution.generate_second_warehouse(filename)
    g = solution_part2.generate_second_warehouse(filename)

    assert expected == g

input_example_2 = "example_2.txt"

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_2, 618), # (1,5) -> 105, (2,7) -> 207, (3,6) -> 306, total = 105 + 207 + 306 = 618
        pytest.param(input_example, 9021),
        pytest.param(input_full, 1522215), # not 1502541
    ],    
)
def test_solve_part2(filename, expected):
    #value = solution.solve_part2(filename)
    value = solution_part2.solve_part2(filename)
    assert expected == value

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename",
    [
        pytest.param('bug-example.txt')
    ],    
)
def test_apply_second_warehouse_movements(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    gi = grid.lines_to_grid(lines)
    grid.display_grid(gi)

    go = gi.clone()
    

    movement_lines = [['^']]
    go = solution_part2.apply_second_warehouse_movements(go, movement_lines)

    grid.display_grid(go)
    assert gi == go # Not changed!