# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    count = 0
    yes_set = set()
    for l in lines:
        if len(l) == 0:
            count += len(yes_set) # Add number of unique entries
            yes_set = set() # Clear set
        else:
            for ch in l:
                yes_set.add(ch)

    # Remember to count the last entry (if present)
    count += len(yes_set)

    return count

def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    count = 0
    yes_dict = dict()
    group_size = 0
    for l in lines:
        if len(l) == 0:
            for _,v in yes_dict.items():
                if v == group_size:
                    count += 1     
            yes_dict.clear()
            group_size = 0       
        else:
            group_size += 1
            for ch in l:                
                if not ch in yes_dict:
                    yes_dict[ch] = 1
                else:
                    value = yes_dict[ch]
                    yes_dict[ch] = 1 + value                

    # Remember to count the last entry (if present)
    for _,v in yes_dict.items():
        if v == group_size:
            count += 1     
 
    return count