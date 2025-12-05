# Shared helper libraries
from helpers import fileutils, numrangeutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def is_fresh(i_id, range_list):
    for r in range_list:
        r_min = r[0]
        r_max = r[1]

        if i_id >= r_min and i_id <= r_max:
            #logger.debug(f"Fresh: i_id={i_id} in range r={r}")
            return True
    return False


def get_ranges_from_input_file(filename):
    range_lines = fileutils.get_lines_before_empty_from_file(filename)

    range_list = []
    for rl in range_lines:
        r_min, r_max = rl.split('-')
        r = (int(r_min),int(r_max))
        assert r[0] <= r[1], f"r_min={r_min} r_max={r_max}"
        range_list.append(r)
    return range_list


def get_ingredient_ids_from_input_file(filename):
    ids = list()
    ingredient_lines = fileutils.get_lines_after_empty_from_file(filename)    
    for il in ingredient_lines:
        ids.append(int(il))
    return ids


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    #lines = fileutils.get_file_lines_from(filename)
    
    range_list = get_ranges_from_input_file(filename)
    ids = get_ingredient_ids_from_input_file(filename)

    #logger.debug(f"range_list={range_list}")

    fresh_count = 0
    for id in ids:
        if is_fresh(id, range_list): # Increment count if ingredient ID in a range provided
            fresh_count += 1

    return fresh_count

"""
def merge_overlapping_ranges(range_list:list[tuple[int,int]]) -> set[tuple[int,int]]:
    range_list.sort(key=lambda r: r[0]) # Sort by min value in each range(min,max) in list
    
    merged_range_set = set()

    size = len(range_list)
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

def solve_part2(filename):
    range_list = get_ranges_from_input_file(filename)
    #logger.debug(f"Original: range_list={range_list}")
    
    unique_range_set = numrangeutils.merge_overlapping_ranges(range_list)
    #logger.debug(f"Merged: unique_range_set={unique_range_set}")

    ans = 0
    for r in unique_range_set:
        r_size = (r[1] - r[0]) + 1
        ans += r_size    

    return ans
