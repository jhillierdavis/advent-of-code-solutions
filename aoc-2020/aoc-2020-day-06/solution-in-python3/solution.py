# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_entry_count_and_clear(yes_set:set) -> int:
    count = len(yes_set) # Add number of unique entries
    yes_set.clear()
    return count


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    count = 0
    yes_set = set()
    for l in lines:
        if len(l) == 0: # Empty line
            count += get_entry_count_and_clear(yes_set)
            continue

        for ch in l:
            yes_set.add(ch)

    # Remember to count the last entry (if present)
    count += get_entry_count_and_clear(yes_set)

    return count


def get_count_matching_group_size_and_clear(yes_dict:dict, group_size:int) -> int:
    count = 0
    for _,v in yes_dict.items():
        if v == group_size:
            count += 1     
    yes_dict.clear()
    return count


def add_to_dict(yes_dict:dict, line:str):
    for ch in line:                
        if not ch in yes_dict:
            yes_dict[ch] = 1
        else:
            value = yes_dict[ch]
            yes_dict[ch] = 1 + value                


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    
    count = 0
    yes_dict = dict()
    group_size = 0
    for l in lines:
        if len(l) == 0: # Empty
            count += get_count_matching_group_size_and_clear(yes_dict, group_size)
            group_size = 0   
            continue    

        add_to_dict(yes_dict, l)
        group_size += 1

    # Remember to count the last entry (if present)
    count += get_count_matching_group_size_and_clear(yes_dict, group_size)   
 
    return count