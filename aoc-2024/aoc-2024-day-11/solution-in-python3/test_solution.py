import pytest

import solution

input_example = "AOC-2024-Day-11_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-11_Puzzle-Input-Full.txt"



@pytest.mark.parametrize(
    "input, blinks, expected",
    [    
        pytest.param('0', 1, '1'),
        pytest.param('1', 1, '2024'),
        pytest.param('10', 1, '1 0'),
        pytest.param('99', 1, '9 9'),
        pytest.param('999', 1, '2021976'),
        pytest.param('0 1 10 99 999', 1, '1 2024 1 0 9 9 2021976'),     
        pytest.param('125 17', 1, '253000 1 7'),
        pytest.param('253000 1 7', 1, '253 0 2024 14168'),
        pytest.param('125 17', 2, '253 0 2024 14168'),
        pytest.param('125 17', 3, '512072 1 20 24 28676032'),
        pytest.param('125 17', 4, '512 72 2024 2 0 2 4 2867 6032'),
        pytest.param('125 17', 5, '1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32'),
        pytest.param('125 17', 6, '2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2'),
    ],    
)
def test_evolve_stones(input, blinks, expected):
    stones = solution.evolve_stone_values(input, blinks)
    assert expected == stones


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "input, blinks, expected",
    [
        pytest.param('125 17', 1, 3),
        pytest.param('125 17', 2, 4),
        pytest.param('125 17', 3, 5),
        pytest.param('125 17', 4, 9),
        pytest.param('125 17', 5, 13),
        pytest.param('125 17', 6, 22),
        pytest.param('125 17', 25, 55312),
    ],    
)
def test_count_stones_after_blinks(input, blinks, expected):
    stone_values = solution.evolve_stone_values(input, blinks)
    assert expected == solution.count_stone_values(stone_values)



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, blinks, expected",
    [
        pytest.param(input_example, 25, 55312),
        pytest.param(input_full, 25, 197157),
    ],    
)
def test_solve_part1(filename, blinks, expected):
    value = solution.solve_part1(filename, blinks)
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, blinks, expected",
    [
        pytest.param(input_example, 25, 55312),
        pytest.param(input_example, 75, 65601038650482),
        pytest.param(input_full, 25, 197157),
        pytest.param(input_full, 75, 234430066982597),
    ],    
)
def test_solve_part2(filename, blinks, expected):
    value = solution.solve_part2(filename, blinks)
    assert expected == value
