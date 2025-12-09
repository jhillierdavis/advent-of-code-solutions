import pytest

import solution

input_example = "AOC-2025-Day-09_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-09_Puzzle-Input-Full.txt"


def test_get_rectange_size():
    assert 50 == solution.get_rectangle_size((2,5), (11,1))


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 50),
        pytest.param(input_full, 4761736832),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


input_example_other = "AOC-2025-Day-09_Puzzle-Input-Example-Other.txt"

"""
.X#X............X#X.
.###............###.
.###............###.
.###............###.
.###............###.
.###............###.
.##X############X##.
.#####X######X#####.
.######......######.
.X####X......X####X.
....................
"""

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 24),
        pytest.param(input_example_other, 30), # Not 98!
        #pytest.param(input_full, 1452422268), # 173060152 too low! , 172842768 too low, not 4602912072, not 4603255632, not 4602912072, not 4761736832, 3143017900, not 4602534508
    ],    
)
def test_solve_part2(filename, expected):
    # Slow! (~ 15 mins)
    value = solution.solve_part2_using_brute_force_approach(filename)
    assert expected == value

    # TODO: find a better (quicker) way!
    #value = solution.solve_part2(filename)    
    #assert expected == value
