# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_max_digit_and_index(value:str) -> int:
    size = len(value)
    max_value = 0
    max_index = 0
    for i in range(size):
        iv = int(value[i])
        if iv > max_value:
            max_value = iv
            max_index = i
    #logger.debug(f"value={value} max_value={max_value} max_index={max_index}")
    return max_value, max_index


def max_digits_subsequence(value:str, digits:int=2) -> int:
    result = 0
    offset = 0
    for d in range(0,digits):
        x = digits-(d+1)
        sub_v = value[offset:-x] if x > 0 else value[offset:]
        v,i = get_max_digit_and_index(sub_v)
        offset += (i + 1)
        result += v * pow(10,x)
        #logger.debug(f"value={value} d={d} x={x} sub_v={sub_v} v={v} i={i} offset={offset} result={result}")
    return result


def solve_part1(filename):
    return process_input_data_lines(filename, 2)


def solve_part2(filename):
    return process_input_data_lines(filename, 12)


def process_input_data_lines(filename:str, digits:int=2) -> int:
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    for l in lines:
        # Get largest 'joltage' value
        ans += max_digits_subsequence(l, digits)
    return ans
