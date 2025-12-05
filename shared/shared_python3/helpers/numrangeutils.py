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
