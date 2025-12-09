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
