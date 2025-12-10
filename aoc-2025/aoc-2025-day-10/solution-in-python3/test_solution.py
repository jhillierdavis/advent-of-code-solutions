import pytest

import solution

input_example = "AOC-2025-Day-10_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-10_Puzzle-Input-Full.txt"



@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}", 2),
        pytest.param("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}", 3),
        pytest.param("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}", 2),
    ],    
)
def test_calculate_fewest_button_presses(input, expected):
    value = solution.calculate_fewest_button_presses(input)    
    assert expected == value



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7),
        pytest.param(input_full, 473),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
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
