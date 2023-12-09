import pytest

import solution

@pytest.mark.parametrize(
    "sequence,expected",
    [
        pytest.param([0,3,6,9,12,15], 18),
        pytest.param([1,3,6,10,15,21], 28),
        pytest.param([10,13,16,21,30,45], 68),
        pytest.param([1,0,-5,-10,-8,11,60,155,315,562,921,1420,2090,2965,4082,5481,7205,9300,11815,14802,18316], 22415), 
        pytest.param([13, 21, 50, 108, 198, 331, 552, 989, 1955, 4162, 9159, 20221, 44162, 95029, 201507, 421327, 868273, 1760839, 3506560, 6842958, 13065390], 24384403),
    ],    
)
def test_get_sequence_next_value(sequence, expected):
    assert solution.get_sequence_next_value(sequence) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example.txt', 114),
        pytest.param('puzzle-input-full.txt', 1939607039),
    ],    
)
def test_solution_part1(filename, expected):
    assert solution.solve_part1(filename) == expected


@pytest.mark.parametrize(
    "sequence,expected",
    [
        pytest.param([0,3,6,9,12,15], -3),
        pytest.param([1,3,6,10,15,21], 0),
        pytest.param([10,13,16,21,30,45], 5),
    ],    
)
def test_get_sequence_previous_value(sequence, expected):
    assert solution.get_sequence_previous_value(sequence) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example.txt', 2),
        pytest.param('puzzle-input-full.txt',1041),
    ],    
)
def test_solution_part2(filename, expected):
    assert solution.solve_part2(filename) == expected