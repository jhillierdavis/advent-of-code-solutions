import pytest

import solution_part2 as solution

def test_interval():
    interval = solution.Interval(98, 2)
    
    assert interval.contains_value(97) == False
    assert interval.contains_value(98) == True
    assert interval.contains_value(99) == True
    assert interval.contains_value(100) == False

def test_whether_interval_overlaps():
    interval_7_5 = solution.Interval(7, 5)
    interval_3_2 = solution.Interval(3, 2)
    interval_5_5 = solution.Interval(5, 5)

    assert interval_7_5.overlaps(interval_3_2) == False
    assert interval_3_2.overlaps(interval_5_5) == False
    assert interval_7_5.overlaps(interval_5_5) == True
    
def test_whether_interval_overlaps():
    interval_7_5 = solution.Interval(7, 5)
    interval_3_2 = solution.Interval(3, 2)
    interval_5_5 = solution.Interval(5, 5)
    interval_2_5 = solution.Interval(2, 5)
    interval_1_15 = solution.Interval(1, 15)

    assert interval_7_5.get_overlap_interval(interval_3_2) == None
    assert interval_3_2.get_overlap_interval(interval_5_5) == None
    assert interval_7_5.get_overlap_interval(interval_5_5) == solution.Interval(7,3)
    #assert interval_5_5.get_overlap_interval(interval_7_5) == solution.Interval(7,3)
    #assert interval_2_5.get_overlap_interval(interval_5_5) == solution.Interval(5,2)
    #assert interval_5_5.get_overlap_interval(interval_2_5) == solution.Interval(5,2)
    #assert interval_1_15.get_overlap_interval(interval_2_5) == interval_2_5


def test_get_interval_sorted_set():
    existing_intervals = set()
    interval_98_2 = solution.Interval(98, 2)
    existing_intervals.add(interval_98_2)
    interval_10_50 = solution.Interval(10, 50)
    existing_intervals.add(interval_10_50)
    assert len(existing_intervals) == 2
            
    interval_set = solution.get_intervals(1, 100, existing_intervals)
    assert len(interval_set) == 5


def test_get_seed_intervals():
    list_seed_intervals = solution.get_seed_intervals_from_filename('puzzle-input-example.txt')

    assert len(list_seed_intervals) == 2
    assert list_seed_intervals[0] == solution.Interval(55,13)
    assert list_seed_intervals[1] == solution.Interval(79,14)


from solution import Adjuster, AdjusterMap

"""
def test_get_mapping_intervals():
    list_seed_intervals = solution.get_seed_intervals_from_filename('puzzle-input-example.txt')

    adjustermap = AdjusterMap()
    adjustermap.add_adjuster(50,98,2)
    adjustermap.add_adjuster(52,50,48)

#    mapped_intervals = map_intervals(list_seed_intervals, adjustermap)

    assert len(mapped_intervals) == 2
    assert list_seed_intervals[0] == solution.Interval(57,13)
    assert list_seed_intervals[1] == solution.Interval(79,14)
"""

