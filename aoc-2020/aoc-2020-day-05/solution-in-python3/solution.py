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

def get_column(boarding_pass:str):
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


def solve_part1(filename):    
    lines = fileutils.get_file_lines_from(filename)

    max_seat_id = 0
    for l in lines:
        seat_id = get_seat_id(l)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    seats = []
    for l in lines:
        seat_id = get_seat_id(l)
        seats.append(seat_id)

    seats.sort()

    #print(seats)

    prior_seat_id = None
    for i, seat_id in enumerate(seats):
        #logger.debug(f"i={i} seat_id={seat_id}")
        if i == 0:
            prior_seat_id = seat_id
            continue
        elif seat_id == (1 + prior_seat_id):
            #logger.debug(f"seat_id={seat_id} prior_seat_id={prior_seat_id}")
            prior_seat_id = seat_id
            continue
        return 1 + prior_seat_id
    raise Exception(f"Gap not found in seats={seats}")