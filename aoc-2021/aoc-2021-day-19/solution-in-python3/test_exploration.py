import pytest

import exploration, solution

input_example = "AOC-2021-Day-19_Puzzle-Input-Example.txt"


def test_calculate_beacon_overlap_in_2d():
    scanner_set_0 = {(0,2),(4,1),(3,3)}
    scanner_set_1 = {(-1,-1),(-5,0),(-2,1)}

    min_intersection = 3
    assert exploration.calculate_beacon_overlap_in_2d(scanner_set_0, scanner_set_1, min_intersection) >= min_intersection 


#@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 12),
    ],    
)
def test_calculate_beacon_overlap_in_3d(filename, expected):
    scanner_beacon_map = solution.get_input_scanner_beacon_map(filename)

    min_intersection = expected
    assert exploration.calculate_beacon_overlap_in_3d(scanner_beacon_map[0], scanner_beacon_map[1], min_intersection) >= expected


