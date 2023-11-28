import pytest

# Local
import solution

@pytest.mark.parametrize(
    "x,y,max, expected_sequence",
    [
        pytest.param(7, 2, 1, [(7,2)]),
        pytest.param(7, 2, 2, [(7,2), (13,3)]),
        pytest.param(7, 2, 3, [(7,2), (13,3), (18,3)]),
        pytest.param(7, 2, 4, [(7,2), (13,3), (18,3), (22,2)]),
        pytest.param(7, 2, 5, [(7,2), (13,3), (18,3), (22,2), (25,0)]),
        pytest.param(7, 2, 6, [(7,2), (13,3), (18,3), (22,2), (25,0), (27,-3)]),
        pytest.param(7, 2, 7, [(7,2), (13,3), (18,3), (22,2), (25,0), (27,-3), (28,-7)]),
        pytest.param(6, 3, 9, [(6, 3), (11, 5), (15, 6), (18, 6), (20, 5), (21, 3), (21, 0), (21, -4), (21, -9)]),
        pytest.param(9, 0, 4, [(9, 0), (17, -1), (24, -3), (30, -6)]),
        pytest.param(17, -4, 4, [(17, -4), (33, -9), (48, -15), (62, -22)])
    ],    
)
def test_calculate_sequence(x, y, max, expected_sequence):
    assert solution.calculate_sequence(x,y,max) == expected_sequence

    
@pytest.mark.parametrize(
    "sequence, target_area, expected",
    [
        pytest.param([(7,2), (13,3), (18,3), (22,2), (25,0), (27,-3), (28,-7)], (20,30,-10,-5), True),
        pytest.param([(6, 3), (11, 5), (15, 6), (18, 6), (20, 5), (21, 3), (21, 0), (21, -4), (21, -9)], (20,30,-10,-5), True),
        pytest.param([(9, 0), (17, -1), (24, -3), (30, -6)], (20,30,-10,-5), True),
        pytest.param([(17, -4), (33, -9), (48, -15), (62, -22)], (20,30,-10,-5), False)
    ],    
)

def test_transits_target_area(sequence, target_area, expected):
    assert solution.transits_target_rectangle(sequence, target_area) == expected

"""
@pytest.mark.parametrize(
    "target_rectangle, expected_max_y",
    [
        pytest.param("x=20..30, y=-10..-5", 45),
    ],    
)
def test_calculate_max_height(target_rectangle, expected_max_y):
    assert solution.calculate_max_height(target_rectangle) == expected_max_y
"""