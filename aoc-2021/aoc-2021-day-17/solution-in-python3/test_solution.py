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
        pytest.param(17, -4, 4, [(17, -4), (33, -9), (48, -15), (62, -22)]),
        pytest.param(6, 9, 20, [(6, 9), (11, 17), (15, 24), (18, 30), (20, 35), (21, 39), (21, 42), (21, 44), (21, 45), (21, 45), (21, 44), (21, 42), (21, 39), (21, 35), (21, 30), (21, 24), (21, 17), (21, 9), (21, 0), (21, -10)])
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
        pytest.param([(6, 9), (11, 17), (15, 24), (18, 30), (20, 35), (21, 39), (21, 42), (21, 44), (21, 45), (21, 45), (21, 44), (21, 42), (21, 39), (21, 35), (21, 30), (21, 24), (21, 17), (21, 9), (21, 0), (21, -10)], (20,30,-10,-5), True),
        pytest.param([(17, -4), (33, -9), (48, -15), (62, -22)], (20,30,-10,-5), False)
    ],    
)

def test_transits_target_area(sequence, target_area, expected):
    assert solution.transits_target_rectangle(sequence, target_area) == expected


@pytest.mark.parametrize(
    "speed_x, speed_y, expected_max_y",
    [
        pytest.param(7, 2, 3),
        pytest.param(6, 3, 6),
        pytest.param(9, 0, 0),
        pytest.param(17, -4, -4),
        pytest.param(6, 8, 36),
        pytest.param(6, 9, 45),
        pytest.param(6, 10, 55),
    ],    
)
def test_max_height(speed_x, speed_y, expected_max_y):
    seq = solution.calculate_sequence(speed_x, speed_y, 10)

    assert solution.calculate_max_y_in_xy_sequence_list(seq) == expected_max_y


@pytest.mark.parametrize(
    "target_min_x, target_max_x, target_min_y, target_max_y, expected_max_y, expected_number_of_solutions",
    [
        pytest.param(20, 30, -10, -5, 45, 112), # Example data (part's 1 & 2)
        pytest.param(244, 303, -91, -54, 4095, 3773) # Full data (part's 1 & 2)
    ],    
)
def test_solution(target_min_x, target_max_x, target_min_y, target_max_y, expected_max_y, expected_number_of_solutions):
    valid_sequence_list = []

    for x in range(1,target_max_x+1):
        for y in range(target_min_y, abs(target_min_y)): 
            seq = solution.calculate_sequence(x, y, target_max_x)
            if solution.transits_target_rectangle(seq, (target_min_x , target_max_x, target_min_y, target_max_y)):
                valid_sequence_list.append(seq)

    max_y = 0
    for entry in valid_sequence_list:
        entry_max_y = solution.calculate_max_y_in_xy_sequence_list(entry)
        if entry_max_y > max_y:
            max_y = entry_max_y

    assert max_y ==expected_max_y
    assert len(valid_sequence_list) == expected_number_of_solutions