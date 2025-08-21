# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_row(boarding_pass:str):
    return 0

def get_column(boarding_pass:str):
    return 0

def calculate_seat_id(row:int, column:int) -> int:
    return (row * 8) + column

def get_seat_id(boarding_pass:str):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    return calculate_seat_id(row, column)


def solve_part1(filename):
    logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"

def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
