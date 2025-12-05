"""
AI Prompt:

Write Python code that takes a list of ranges of integer values (each range given as a string with min and max separated by a dash, e.g. '3-5') and a list of integers. 
The function should count how many of the integers fall within the supplied ranges (inclusive). 
Overlapping ranges should be merged before counting. 
Provide the implementation and parameterised PyTest unit tests that validate different scenarios, including overlapping ranges, touching ranges, single ranges, empty ranges, and integers outside the ranges.
"""

from typing import List, Tuple

def parse_ranges(range_strings: List[str]) -> List[Tuple[int, int]]:
    """
    Parse ranges given as strings like '3-5' into tuples (3,5).
    """
    ranges = []
    for r in range_strings:
        parts = r.split("-")
        if len(parts) != 2:
            raise ValueError(f"Invalid range format: {r}")
        start, end = int(parts[0]), int(parts[1])
        ranges.append((min(start, end), max(start, end)))
    return ranges


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Merge overlapping or touching intervals into a non-overlapping list.
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:  # overlap or touching
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged.append((current_start, current_end))
    return merged


def count_integers_in_ranges(range_strings: List[str], integers: List[int]) -> int:
    """
    Count how many integers fall within the supplied ranges.
    """
    intervals = parse_ranges(range_strings)
    merged = merge_intervals(intervals)
    
    count = 0
    for num in integers:
        for start, end in merged:
            if start <= num <= end:
                count += 1
                break  # avoid double counting
    return count

# Manual additions (for overall solution unit testing - see 'test_solution.py')

import solution
from helpers import fileutils

def solve_part1(filename:str) -> int:
    range_strings = fileutils.get_lines_before_empty_from_file(filename)
    id_list = solution.get_ingredient_ids_from_input_file(filename)
    ans = count_integers_in_ranges(range_strings, id_list)
    return ans
