import pytest

import exploration

def test_calculate_beacon_overlap_in_2d():
    scanner_set_0 = {(0,2),(4,1),(3,3)}
    scanner_set_1 = {(-1,-1),(-5,0),(-2,1)}

    min_intersection = 3
    assert exploration.calculate_beacon_overlap_in_2d(scanner_set_0, scanner_set_1, min_intersection) >= min_intersection 


