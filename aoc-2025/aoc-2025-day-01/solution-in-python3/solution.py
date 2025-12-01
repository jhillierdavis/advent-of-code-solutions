# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def determine_value_and_count_zeros(value, direction, amount):
    zero_count = 0

    if 'L' == direction:
        value -= amount            
    elif 'R' == direction:
        value += amount
    else:
        raise Exception(f"Unknown direction={direction}")

    value = (value % 100)
    if value == 100:
        value = 0
    
    if value == 0:
        zero_count += 1
    #logger.debug(f"direction={direction} amount={amount} value={value}")    
    return value, zero_count


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    value = 50
    for l in lines:
        direction = l[0]
        amount = int(l[1:])

        value, zero_count = determine_value_and_count_zeros(value, direction, amount)
        ans += zero_count

    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    
    ans = 0
    value = 50
    for l in lines:
        direction = l[0]
        amount = int(l[1:])

        for i in range(amount):
            value, zero_count = determine_value_and_count_zeros(value, direction, 1)
            ans += zero_count
        
    return ans
