import pytest

from helpers import fileutils, grid, point
import solution

input_example = "AOC-2024-Day-20_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-20_Puzzle-Input-Full.txt"

input_example_cheat_1 = "example_1_cheat.txt"
input_example_cheat_2 = "example_2_cheat.txt"
input_example_cheat_3 = "example_3_cheat.txt"
input_example_cheat_4 = "example_4_cheat.txt"


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 84),
        pytest.param(input_full, 9420),
    ],    
)
def test_get_shortest_path(filename, expected):
    value = solution.get_shortest_path(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_cheat_1, 72),
        pytest.param(input_example_cheat_2, 64),
        pytest.param(input_example_cheat_3, 84 - 38),
        pytest.param(input_example_cheat_4, 84 - 64),
    ],    
)
def test_get_shortest_path_with_cheat(filename, expected):
    value = solution.get_shortest_path_with_cheat(filename)    
    assert expected == value





#@pytest.mark.skip(reason="TODO: Ignore until implemented")
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
    value = solution.count_number_of_cheats_for_saving(filename, saving)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, size, expected",
    [
        pytest.param(input_example, 1, ((7,1),(9,1),1)), # from Example 1
        pytest.param(input_example, 1, ((9,7),(11,7),1)), # from Example 2
        pytest.param(input_example, 1, ((8,7),(8,9),1)), # from Example 3
        pytest.param(input_example, 1, ((7,7),(5,7),1)), # from Example 4
    ],    
)
def test_get_cheat_paths(filename, size, expected):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = solution.find_single_symbol_point_and_clear(g,'S')
    ep = solution.find_single_symbol_point_and_clear(g,'E')

    cheat_paths = solution.get_cheat_paths(g, size)
    es, ee, el = expected
    print(f"DEBUG: es={es} ee={ee} el={el}")
    esx, esy = es
    eex, eey = ee
    print(f"DEBUG: esx={esx} esy={esy} eex={eex} eey={eey}")
    esp = point.Point2D(esx,esy)
    eep = point.Point2D(eex,eey)
    print(f"DEBUG: esp={esp} eep={eep}")

    matched = False
    for cp in cheat_paths:
        cs, ce, cl, _ = cp
        if cs == esp and ce == eep and cl == el:
            matched = True
            break
    
    assert matched


@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, saving, expected",
    [
        pytest.param(input_example, 64, 1),
        #pytest.param(input_full, 100, 1454), # But, very slow (~ 20 mins!)
    ],    
)
def test_solve_part1(filename, saving, expected):
    value = solution.solve_part1(filename, saving)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
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
        #pytest.param(input_full, 100, -1),
    ],    
)
def test_solve_part2(filename, saving, expected):
    value = solution.solve_part2(filename, saving)
    
    assert expected == value
