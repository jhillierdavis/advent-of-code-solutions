# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def is_within_range(value:int, min_value:int, max_value:int) -> bool:
    """
    Check if a numeric value is within a given inclusive range.

    Parameters:
    value (float or int): The number to check.
    min_value (float or int): The lower bound of the range.
    max_value (float or int): The upper bound of the range.

    Returns:
    bool: True if value is within [min_value, max_value], False otherwise.
    """
    return min_value <= value <= max_value


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_lines_before_empty_from_file(filename)

    # Get ranges
    ranges = list()
    for l in lines:
        vals = l.split(' ')
        logger.debug(f"line={l} vals={vals}")
        for v in vals:
            if '-' in v:
                vmin, vmax = v.split("-")
                logger.debug(f"vmin={vmin}, vmax={vmax}")
                ranges.append((int(vmin), int(vmax)))
        
    logger.debug(f"ranges={ranges}")


    lines = fileutils.get_lines_after_empty_from_file(filename)
    found = False
    ans = 0
    for l in lines:
        if l == 'nearby tickets:':
            found = True
            continue

        if found:            
            logger.debug(f"l={l}")    
            vals = l.split(',')
            for v in vals:
                is_valid = False
                vnum = int(v)
                for r in ranges:
                    if is_within_range(vnum, r[0], r[1]):
                        is_valid = True
                        continue
                if not is_valid:
                    ans += vnum
    return ans

def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
