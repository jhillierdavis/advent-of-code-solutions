"""
AI Prompt:

Write Python code that takes a list of ranges of integer values, where each range is given as a string with min and max separated by a dash (e.g. '3-5'). 
The ranges may overlap. 
The program should merge overlapping ranges and count the total number of unique integer values that fall within the supplied ranges (inclusive). 
Ensure the solution works efficiently for very large ranges without expanding them into sets of integers. 
Provide the full implementation and parameterised PyTest unit tests that cover cases such as overlapping ranges, touching ranges, disjoint ranges, single ranges, single‑value ranges, large ranges, and empty input. 
For example, given ranges ['3-5', '10-14', '16-20', '12-18'], the function should return 14.
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


def count_unique_integers(range_strings: List[str]) -> int:
    """
    Count the total number of unique integer values that fall within the supplied ranges.
    """
    intervals = parse_ranges(range_strings)
    merged = merge_intervals(intervals)
    
    total = 0
    for start, end in merged:
        total += (end - start + 1)  # inclusive count
    return total



# Manual additions (for overall solution unit testing - see 'test_solution.py')

from helpers import fileutils

def solve_part2(filename:str) -> int:
    range_strings = fileutils.get_lines_before_empty_from_file(filename)
    ans = count_unique_integers(range_strings)
    return ans
