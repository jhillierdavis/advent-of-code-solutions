import pytest

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
        #pytest.param(input_example, 11),
        #pytest.param(input_full, -1),
    ],    
)
def test_count_number_of_cheats_for_saving(filename, saving, expected):
    value = solution.count_number_of_cheats_for_saving(filename, saving)    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, saving, expected",
    [
        pytest.param(input_example, 64, 1),
        pytest.param(input_full, 100, 1454), # But, very slow (~ 20 mins!)
    ],    
)
def test_solve_part1(filename, saving, expected):
    value = solution.solve_part1(filename, saving)
    
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
