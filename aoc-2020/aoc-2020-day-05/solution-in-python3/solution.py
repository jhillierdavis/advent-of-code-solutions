# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_row(boarding_pass:str) -> int:
    row = 0
    value = 128

    for i in range(7):
        char = boarding_pass[i]
        value = value // 2

        #logger.debug(f"boarding_pass={boarding_pass} char={char} i={i} value={value}")
        
        if 'B' == char:
            row += value    

    #logger.debug(f"row={row}")
    return row


def get_column(boarding_pass:str) -> int:
    column = 0
    value = 8

    for i in range(7,10):
        char = boarding_pass[i]
        value = value // 2

        #logger.debug(f"boarding_pass={boarding_pass} char={char} i={i} value={value}")
        
        if 'R' == char:
            column += value    

    #logger.debug(f"row={column}")
    return column


def calculate_seat_id(row:int, column:int) -> int:
    return (row * 8) + column


def get_seat_id(boarding_pass:str):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    return calculate_seat_id(row, column)


def get_sorted_seat_list_ascending(lines:str) -> list[int]:
    seats = []
    for l in lines:
        seat_id = get_seat_id(l)
        seats.append(seat_id)

    seats.sort()
    return seats


def solve_part1(filename:str) -> int:    
    lines = fileutils.get_file_lines_from(filename)

    sorted_seats = get_sorted_seat_list_ascending(lines)
    return sorted_seats[-1] # Last entry


def find_first_non_contiguous_gap(nums_sorted_ascending:list) -> int|None:
    """
    Finds the first non-contiguous gap in a (acending order) sorted list of integers.
    Returns the firt value of the gap, or None if all are contiguous.
    """
    for i in range(1, len(nums_sorted_ascending)):
        prior  = nums_sorted_ascending[i - 1]
        next = prior + 1
        if nums_sorted_ascending[i] != next:
            return next
    return None


def solve_part2(filename:str) -> int:
    lines = fileutils.get_file_lines_from(filename)

    sorted_seats = get_sorted_seat_list_ascending(lines)
    vacant_seat_id = find_first_non_contiguous_gap(sorted_seats)
    
    return vacant_seat_id if vacant_seat_id else Exception(f"Gap not found in seats={sorted_seats}")