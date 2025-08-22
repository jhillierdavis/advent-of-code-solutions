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
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
