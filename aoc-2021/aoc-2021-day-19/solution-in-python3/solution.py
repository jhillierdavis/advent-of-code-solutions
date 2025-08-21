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
    logger.debug("TODO: Implement AOC 2021 Part 1")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"

def solve_part2(filename):
    logger.debug("TODO: Implement AOC 2021 Part 1")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"