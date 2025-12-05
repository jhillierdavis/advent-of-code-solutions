# Shared helper libraries
from helpers import fileutils, numrangeutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def is_fresh(id:int, range_list:list[tuple[int,int]]) -> bool:
    return numrangeutils.is_number_in_range_list(id, range_list)


def get_ranges_from_input_file(filename:str) -> list[tuple[int,int]]:
    range_lines = fileutils.get_lines_before_empty_from_file(filename)

    range_list = []
    for rl in range_lines:
        r_min, r_max = rl.split('-')
        r = (int(r_min),int(r_max))
        assert r[0] <= r[1], f"r_min={r_min} r_max={r_max}"
        range_list.append(r)
    return range_list


def get_ingredient_ids_from_input_file(filename:str) -> list[int]:
    ids = list()
    ingredient_lines = fileutils.get_lines_after_empty_from_file(filename)    
    for il in ingredient_lines:
        ids.append(int(il))
    return ids


def solve_part1(filename:str) -> int:
    range_list = get_ranges_from_input_file(filename)
    ids = get_ingredient_ids_from_input_file(filename)

    #logger.debug(f"range_list={range_list}")

    # Count the number of ingredient IDs in any of input ranges provided
    fresh_count = 0
    for id in ids:
        if is_fresh(id, range_list): 
            fresh_count += 1

    return fresh_count


def solve_part2(filename:str) -> int:
    range_list = get_ranges_from_input_file(filename)
    #logger.debug(f"Original: range_list={range_list}")
    
    unique_range_set = numrangeutils.merge_overlapping_ranges(range_list)
    #logger.debug(f"Merged: unique_range_set={unique_range_set}")

    # Determine the total number of potential valid IDs (the count of unique numbers in the ranges provided)
    ans = 0
    for r in unique_range_set:
        r_size = (r[1] - r[0]) + 1
        ans += r_size    

    return ans
