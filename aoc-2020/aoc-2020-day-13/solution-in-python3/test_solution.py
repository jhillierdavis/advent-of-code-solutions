import pytest

import solution

input_example = "AOC-2020-Day-13_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-13_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 295),
        pytest.param(input_full, 3385),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


@pytest.mark.parametrize(
    "buses, expected",
    [
        pytest.param(['17','x','13','19'], 3417),
        pytest.param(['67','7','59','61'], 754018),
        pytest.param(['67','x','7','59','61'], 779210),
        pytest.param(['67','7','x','59','61'], 1261476),
        pytest.param(['1789','37','47','1889'],1202161486),
    ],    
)
def test_get_earliest_sequence_timestamp(buses, expected):
    assert solution.get_earliest_sequence_timestamp(buses) == expected


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected, offset",
    [
        pytest.param(input_example, 1068781, 0),
        #pytest.param(input_full, -1, 100000000000000),
    ],    
)
def test_solve_part2(filename, expected, offset):
    value = solution.solve_part2(filename, offset)
    
    assert expected == value
