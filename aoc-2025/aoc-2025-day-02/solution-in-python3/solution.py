# Shared helper libraries
from helpers import fileutils, numutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

"""
def is_valid_id(id:int) -> bool:
    id_str = str(id)
    size = len(id_str)
    midpoint = size // 2
    left = id_str[0:midpoint]
    right = id_str[midpoint:]
    #logger.debug(f"left={left} right={right} size={size} midpoint={midpoint}")
    return left != right
"""

def has_repeating_half(num: int) -> bool:
    """
    Check if the given number repeats at its midpoint (e.g. 11, 22, 446446, 38593859)
    """
    s = str(num)
    size = len(s)

    if numutils.is_odd(size):
        return False # Must divide evenly

    midpoint = size // 2 
    
    left = s[0:midpoint]
    right = s[midpoint:]
    #logger.debug(f"left={left} right={right} size={size} midpoint={midpoint}")

    return left == right


def has_repeating_subsequences(num: int) -> bool:
    """
    Check if given number fully consists of repeating sub-sequences e.g. 123123123 (123 three times), 2121212121 (sequences of 21).
    """
    s = str(num)
    size = len(s)
    midpoint = size // 2

    for i in range(1, midpoint + 1):
        if size % i != 0:              
            continue # Sub-sequence length must divide evenly into whole

        subpart = s[:i]
        if subpart * (size // i) == s:
            return True # Matching sub-sequences
    return False


def solve_part1(filename):
    return determine_invalid_ids_from_file_input(filename, has_repeating_half)


def solve_part2(filename):
    return determine_invalid_ids_from_file_input(filename, has_repeating_subsequences)


def determine_invalid_ids_from_file_input(filename:str, is_invalid_id:callable) -> int:
    lines = fileutils.get_file_lines_from(filename)
    input = lines[0]
    values = input.split(',')

    ans = 0
    for v in values:        
        v_ranges = v.split("-")
        v_min = int(v_ranges[0])
        v_max = int(v_ranges[1])

        for id in range(v_min, v_max+1):
            
            if is_invalid_id(id):
                #logger.debug(f"Invalid id={id}")
                ans += id

    return ans