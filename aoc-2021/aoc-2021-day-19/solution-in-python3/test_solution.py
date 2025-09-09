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
    scanner_beacon_map = solution.get_input_scanner_beacon_map(filename)

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


#{(404,-588,-901),(528,-643,409),(-838,591,734),(390,-675,-793),(-537,-823,-458),(-485,-357,347),(-345,-311,381),(-661,-816,-575),(-876,649,763),(-618,-824,-621),(553,345,-567),(474,580,667),(-447,-329,318),(-584,868,-557),(544,-627,-890),(564,392,-477),(455,729,728),(-892,524,684),(-689,845,-530),(423,-701,434),(7,-33,-71),(630,319,-379),(443,580,662),(-789,900,-5510),(459,-707,401)}
#{(686,422,578),(605,423,415),(515,917,-361),(-336,658,858),(95,138,22),(-476,619,847),(-340,-569,-846),(567,-361,727),(-460,603,-452),(669,-402,600),(729,430,532),(-500,-761,534),(-322,571,750),(-466,-666,-811),(-429,-592,574),(-355,545,-477),(703,-491,-529),(-328,-685,520),(413,935,-424),(-391,539,-444),(586,-435,557),(-364,-763,-893),(807,-499,-711),(755,-354,-619),(553,889,-390    )}
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
    #print(f"pp_info={pp_info}")
    #print(f"pp_info_0.keys={sorted(pp_info_0.keys())}")


    
    #print(f"pp_info={pp_info}")
    #print(f"pp_info_0.keys={sorted(pp_info_0.keys())}")

    scanner_1_beacons = scanner_beacon_map[1]

    shared_beacons = solution.get_shared_beacons(scanner_1_beacons, pp_info_0)

    """
    orientation_map = solution.get_orientation_map(scanner_1_beacons)
    beacons = set()
    for k, v in orientation_map.items():
        #print(f"scanner_1_beacons={scanner_1_beacons}")    
        pp_info = solution.get_point_pairs_diff_map(v)

        intersect = set(pp_info.keys()).intersection(pp_info_0.keys())
        if len(intersect) >= 24:
            print(f"k={k} len(intersect)={len(intersect)} intersect={intersect}")
            for key in intersect:
                print(f"key={key}")
                tx_0, ty_0, tz_0 = pp_info_0[key][0]
                tx_1, ty_1, tz_1 = pp_info[key][0]
                print(f"pp_info_0[key]={pp_info_0[key]}")
                print(f"pp_info[key]={pp_info[key]}")
                offset = (tx_1 - tx_0, ty_1 - ty_0, tz_1 - tz_0)
                print(f"offset={offset}")
                print()
                beacons.add(pp_info_0[key][0])
                beacons.add(pp_info_0[key][1])

    """
    """
    print(f"len(expected)={len(expected)}")

    md_expected = solution.get_manhatten_distances_between_points(expected)
    print(f"len(md_expected)={len(md_expected)}")
    print(f"md_expected={sorted(md_expected)}")

    scanner_beacon_map = solution.get_input_scanner_beacon_map(filename)

    scanner_0_beacons = scanner_beacon_map[0]
    print(f"scanner_0_beacons={scanner_0_beacons}")

    scanner_1_beacons = scanner_beacon_map[1]
    print(f"scanner_1_beacons={scanner_1_beacons}")    

    m0_set = solution.get_manhatten_distances_between_points(scanner_0_beacons)
    print(f"m0_set={sorted(m0_set)}")

    m1_set = solution.get_manhatten_distances_between_points(scanner_1_beacons)
    print(f"m1_set={sorted(m1_set)}")

    intersect = m0_set.intersection(m1_set)
    print(f"intersect={sorted(intersect)}")
    print(f"len(intersect)={len(intersect)}")
    """
    print(f"len(beancon)={len(shared_beacons)} beasons={shared_beacons}")
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