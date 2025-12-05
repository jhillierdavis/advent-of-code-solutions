"""
Utility functions for range of intervals (list of tuples)
Each list entry is a tuple.
Each tuple consists of (min, max) with integer values representing an inclusive range e.g. (3,5) represents the values: 3,4,5 .
"""


def is_number_in_range_list(num:int, range_list:list[tuple[int,int]]) -> bool:
    for r in range_list:
        r_min = r[0]
        r_max = r[1]

        if num >= r_min and num <= r_max:
            return True
    return False    


def get_range_list_sorted_ascending(range_list:list[tuple[int,int]]) -> list[tuple[int,int]]:
    """
    Return a sorted (ascending) copy of the input range list without modifying the original.
    
    Args:
        range_list (list): The range list to sort.
    
    Returns:
        list: A new sorted (asc) list.
    """    
    return sorted(range_list, key=lambda r: r[0]) 


def merge_overlapping_ranges(range_list:list[tuple[int,int]]) -> set[tuple[int,int]]:
    """
    Merge overlapping range intervals in an input list and return a non-overlapping set.
    
    Args:
        range of intervals (list of tuples): Each tuple is (min, max) with integer values representing a range.
        
    Returns:
        set of tuples: Non-overlapping merged range intervals (each as a tuple).
    """

    # Guard against empty input list
    size = len(range_list)    
    if size == 0:
        return set()

    # Sort (ascending) by min value in each range(min,max) in list (without changing the input range)
    range_list = get_range_list_sorted_ascending(range_list)
    
    merged_range_list = [range_list[0]]
    
    for current in range_list[1:]:
        previous = merged_range_list[-1]
        
        # Check for overlap of values (merge range if so)
        if current[0] <= previous[1]:
            merged_max = max(previous[1], current[1]) # Account for partial or full overlaps
            merged_range_list[-1] = (previous[0], merged_max)
        else: # No overlap
            merged_range_list.append(current)
    
    return set(merged_range_list) # TODO: Decide: Preserve order via leaving as a list?