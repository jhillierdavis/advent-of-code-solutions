import pytest

import solution

input_example = "AOC-2020-Day-16_Puzzle-Input-Example.txt"
input_full = "AOC-2020-Day-16_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 71),
        pytest.param(input_full, 25059),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


input_example_part2 = "AOC-2020-Day-16_Puzzle-Input-Example-Part2.txt"

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, [[7,3,47]]),
        pytest.param(input_example_part2, [[3, 9, 18], [15, 1, 5], [5, 14, 9]]),
    ],    
)
def test_get_valid_nearby_tickets(filename, expected):
    value = solution.get_valid_nearby_tickets(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, {'class': [(0, 1), (4, 19)], 'row': [(0, 5), (8, 19)], 'seat': [(0, 13), (16, 19)]}),
    ],    
)
def test_extract_field_ranges(filename, expected):
    value = solution.extract_field_ranges(filename)
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example_part2, ['row', 'class', 'seat']),
        pytest.param(input_full, ['arrival platform', 'seat', 'departure location', 'class', 'departure station','train', 'arrival location', 'route','type', 'arrival track', 'wagon','departure date', 'zone', 'departure time', 'departure platform','price', 'row', 'arrival station','duration', 'departure track']),
    ],    
)
def test_get_field_order(filename, expected):
    value = solution.get_field_order(filename)
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        #pytest.param(input_example, -1),
        pytest.param(input_full, 3253972369789),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
