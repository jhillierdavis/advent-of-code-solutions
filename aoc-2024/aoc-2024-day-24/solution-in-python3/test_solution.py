import pytest

import solution

input_example = "AOC-2024-Day-24_Puzzle-Input-Example.txt"
input_example_larger = "AOC-2024-Day-24_Puzzle-Input-Example-Larger.txt"
input_full = "AOC-2024-Day-24_Puzzle-Input-Full.txt"
input_example_part2 = "AOC-2024-Day-24_Puzzle-Input-Example-Part2.txt"
input_example_part2_corrected = "AOC-2024-Day-24_Puzzle-Input-Example-Part2-Corrected.txt"


@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4),
        pytest.param(input_example_larger, 2024),
        pytest.param(input_full, 38869984335432),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, 'z00,z01,z02,z05'),
        #pytest.param(input_full, 'TODO'),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
