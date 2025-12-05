"""
def merge_overlapping_ranges(range_list:list[tuple[int,int]]) -> set[tuple[int,int]]:
    merged_range_set = set()

    size = len(range_list)    
    if size == 0:
        return merged_range_set
    
    range_list.sort(key=lambda r: r[0]) # Sort by min value in each range(min,max) in list
    
    rpmin = range_list[0][0] # First range min
    rpmax = range_list[0][1] # First range max

    for i in range(1,size):
        r = range_list[i]
        if rpmax < r[0]:
            # Add range
            merged_range_set.add((rpmin, rpmax))
            rpmin = r[0] # Range min
            rpmax = r[1] # Range max
        else:
            rpmax = max(rpmax, r[1]) 
    
    # Add last merged range (if not already)
    merged_range_set.add((rpmin, rpmax))

    return merged_range_set
"""

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

    # Sort by min value in each range(min,max) in list
    range_list.sort(key=lambda r: r[0]) 
    
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