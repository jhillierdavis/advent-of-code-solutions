import pytest

import solution
from helpers import point

input_example = "AOC-2021-Day-19_Puzzle-Input-Example.txt"
input_full = "AOC-2021-Day-19_Puzzle-Input-Full.txt"


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
        for v in orientation_map.values():            
            if v == expected_set:
                found = True
                break
        assert found


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, {(-618,-824,-621),(-537,-823,-458),(-447,-329,318),(404,-588,-901),(544,-627,-890),(528,-643,409),(-661,-816,-575),(390,-675,-793),(423,-701,434),(-345,-311,381),(459,-707,401),(-485,-357,347)}),
    ],    
)
def test_scanner_1_beacons_overlap_points_in_scanner_0_beacons(filename, expected):
    scanner_beacon_map = solution.get_input_scanner_beacon_map(filename)

    scanner_0_beacons = scanner_beacon_map[0]
    print(f"scanner_0_beacons={scanner_0_beacons}")

    pp_info_0 = solution.get_point_pairs_diff_map(scanner_0_beacons)

    scanner_1_beacons = scanner_beacon_map[1]

    shared_beacons = solution.get_shared_beacons(scanner_1_beacons, pp_info_0)

    #print(f"len(beancon)={len(shared_beacons)} beasons={shared_beacons}")
    assert shared_beacons == expected


@pytest.mark.parametrize(
    "filename, index, expected",
    [
        pytest.param(input_example, 1, (68,-1246,-43) ),
        #pytest.param(input_example, 2, (1105,-1205,1229) ),
        #pytest.param(input_example, 3, (-92,-2380,-20) ), # Not working
        #pytest.param(input_example, 4, (-20,-1133,1061) )        
    ],    
)

def test_get_relative_offset_to_scanner_0(filename, index, expected):
    scanner_beacon_map = solution.get_input_scanner_beacon_map(filename)
    origin_scanner_beacons = scanner_beacon_map[0]
    origin_pair_diff_map = solution.get_point_pairs_diff_map(origin_scanner_beacons)

    scanner_beacons = scanner_beacon_map[index]
    orientation_map = solution.get_orientation_map(scanner_beacons)
    
    for k, v in orientation_map.items():
        
        pp_info = solution.get_point_pairs_diff_map(v)

        intersect = set(pp_info.keys()).intersection(origin_pair_diff_map.keys())
        if len(intersect) >= 24:
            offset = solution.get_offset(intersect, origin_pair_diff_map, pp_info)
            assert offset == expected
            return
        
    raise Exception(f"Failed")


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 79),
        pytest.param(input_full, 383), # < 467
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3621),
        pytest.param(input_full, 9854),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value