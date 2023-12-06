import pytest

from helpers.interval import Interval

def test_interval():
    interval = Interval(98, 2)
    
    assert interval.contains_value(97) == False
    assert interval.contains_value(98) == True
    assert interval.contains_value(99) == True
    assert interval.contains_value(100) == False

def test_whether_interval_overlaps():
    interval_7_5 = Interval(7, 5)
    interval_3_2 = Interval(3, 2)
    interval_5_5 = Interval(5, 5)

    assert interval_7_5.has_intersection(interval_3_2) == False
    assert interval_3_2.has_intersection(interval_5_5) == False
    assert interval_7_5.has_intersection(interval_5_5) == True
    
@pytest.mark.parametrize(
    "interval_a, interval_b, expected",
    [
        pytest.param((7,5), (3,2), None),
        pytest.param((3,2), (5,5), None),
        pytest.param((7,5), (5,5), (7,3)),
        pytest.param((1,7), (5,5), (5,3)),
        pytest.param((5,5), (7,5), (7,3)),
        pytest.param((5,5), (2,5), (5,2)),
        pytest.param((1,15), (2,5), (2,5)),
    ],    
)
def test_intersection(interval_a, interval_b, expected):
    # Given: 2 interval and an expected intersection
    ia = Interval(interval_a[0], interval_a[1])
    ib = Interval(interval_b[0], interval_b[1])
    ie = None if not expected else Interval(expected[0], expected[1])
    
    # Then: obtained intersection is as expected
    assert ia.get_intersection(ib) == ie

@pytest.mark.parametrize(
    "interval_a, interval_b, expected",
    [
        pytest.param((7,5), (3,2), [(3,2), (7,5)]),
        pytest.param((3,2), (5,5), [(3,2), (5,5)]),
        pytest.param((7,5), (5,5), [(5,2), [10, 2]]),
        pytest.param((5,5), (7,5), [(5,2), [10, 2]]),
        pytest.param((1,7), (5,5), [(1,4), (8,2)]),
        pytest.param((1,10), (3,4), [(1,2), (7,3)]), # Subset
        pytest.param((1,10), (1,4), [(5,6)]), # Subset at start
        pytest.param((1,10), (7,4), [(1,6)]), # Subset at end
        pytest.param((3,4),(1,10), [(1,2), (7,3)]), # Superset
        pytest.param((1,4), (1,10), [(5,6)]), # Superset at start
        pytest.param((7,4), (1,10), [(1,6)]), # Superset at end
        pytest.param((5,5), (2,5), [(2,3), (7,3)]),
        pytest.param((1,15), (2,5), [(1,1), [7,8]]),
    ],    
)
def test_subtraction(interval_a, interval_b, expected):
    # Given: 2 interval and an expected subtraction (remainder without intersection)
    ia = Interval(interval_a[0], interval_a[1])
    ib = Interval(interval_b[0], interval_b[1])
    expected_list = []
    for e in expected:
        expected_list.append(Interval(e[0], e[1]))
    
    # Then: obtained subtraction is as expected
    assert ia.get_subtraction(ib) == expected_list


def test_union():
    interval_7_5 = Interval(7, 5)
    interval_3_2 = Interval(3, 2)
    interval_5_5 = Interval(5, 5)
    interval_2_5 = Interval(2, 5)
    interval_1_15 = Interval(1, 15)

    assert interval_7_5.get_union(interval_3_2) == [interval_3_2, interval_7_5] # Disjoint (mutually exclusive)
    assert interval_3_2.get_union(interval_5_5) == [interval_3_2, interval_5_5] # Disjoint
    #assert interval_7_5.get_union(interval_5_5) == [Interval(5,7)]  
    #assert interval_5_5.get_intersection(interval_7_5) == Interval(7,3)
    #assert interval_2_5.get_intersection(interval_5_5) == Interval(5,2)
    #assert interval_5_5.get_intersection(interval_2_5) == Interval(5,2)
    #assert interval_1_15.get_intersection(interval_2_5) == interval_2_5    