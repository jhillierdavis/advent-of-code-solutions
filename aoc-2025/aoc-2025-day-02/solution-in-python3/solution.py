# Shared helper libraries
from helpers import fileutils, numutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def solve_part1(filename):
    return determine_invalid_ids_from_file_input(filename, numutils.has_repeating_half)


def solve_part2(filename):
    return determine_invalid_ids_from_file_input(filename, numutils.has_repeating_subsequences)


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