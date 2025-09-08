import pytest

import solution

input_example = "AOC-2021-Day-19_Puzzle-Input-Example.txt"
input_full = "AOC-2021-Day-19_Puzzle-Input-Full.txt"

#def test_simple_2d_example():

from helpers import point


def test_get_orientation_map():
    input = {(-1,-1,1),(-2,-2,2),(-3,-3,3),(-2,-3,1),(5,6,-4),(8,0,7)}
    expected = [{(1,-1,1),(2,-2,2),(3,-3,3),(2,-1,3),(-5,4,-6),(-8,-7,0)}, 
                {(-1,-1,-1),(-2,-2,-2),(-3,-3,-3),(-1,-3,-2),(4,6,5),(-7,0,8)},
                {(1,1,-1),(2,2,-2),(3,3,-3),(1,3,-2),(-4,-6,5),(7,0,8)},
                {(1,1,1),(2,2,2),(3,3,3),(3,1,2),(-6,-4,-5),(0,7,-8)},
                ]    

    orientation_map = solution.get_orientation_map(input)

    for expected_set in expected:
        found = False
        for k,v in orientation_map.items():            
            if v == expected_set:
                found = True
                break
        assert found


def test_calculate_beacon_overlap_in_2d():
    scanner_set_0 = {(0,2),(4,1),(3,3)}
    scanner_set_1 = {(-1,-1),(-5,0),(-2,1)}

    min_intersection = 3
    assert solution.calculate_beacon_overlap_in_2d(scanner_set_0, scanner_set_1, min_intersection) >= min_intersection 

#@pytest.mark.skip(reason="TODO")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 12),
    ],    
)
def test_calculate_beacon_overlap_in_3d(filename, expected):
    scanner_beacon_map = solution.get_scanner_beacon_map(filename)

    min_intersection = expected
    for k, v in scanner_beacon_map.items():      
        #print(f"Processing k={k} v={v}")  
        assert solution.calculate_beacon_overlap_in_3d(scanner_beacon_map[0], v, min_intersection) >= expected

"""
def test_generate_orientations():
    point3d = point.Point3D(1,2,3)

    expected = [(1,2,3), (-1,2,3), (1,-2,3), (1,2,-3), (-1,-2,3), (-1,2,-3), (1,-2,-3), (-1,-2,-3)]
    actual = solution.generate_orientation_variants(point3d)

    assert len(actual) == 8
    #assert sorted(actual) == sorted(expected)
"""

@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 79),
        #pytest.param(input_full, -1), # < 467
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
