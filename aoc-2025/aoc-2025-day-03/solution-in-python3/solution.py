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


"""
def get_max_joltage(value:str) -> int:
    d1,i1 = get_max_digit_and_index(value[:-1])
    d2,i2 = get_max_digit_and_index(value[i1+1:])
    return (d1*10) + d2
"""
"""
def get_largest_joltage(value:str) -> int:
    d1,i1 = get_max_digit_and_index(value[:-11])
    d2,i2 = get_max_digit_and_index(value[i1+1:-10])
    d3,i3 = get_max_digit_and_index(value[i1+i2+2:-9])
    d4,i4 = get_max_digit_and_index(value[i1+i2+i3+3:-8])
    d5,i5 = get_max_digit_and_index(value[i1+i2+i3+i4+4:-7])
    d6,i6 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+5:-6])
    d7,i7 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+6:-5])
    d8,i8 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+i7+7:-4])
    d9,i9 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+i7+i8+8:-3])
    d10,i10 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+i7+i8+i9+9:-2])
    d11,i11 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+10:-1])
    d12,i12 = get_max_digit_and_index(value[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+11:])
    return (d1*pow(10,11)) + (d2*pow(10,10)) + (d3*pow(10,9)) + (d4*pow(10,8)) + (d5*pow(10,7)) + (d6*pow(10,6)) + (d7*pow(10,5))  + (d8*pow(10,4)) + (d9*pow(10,3)) + (d10*pow(10,2)) + (d11*10) + d12
"""

def get_largest_joltage(value:str, digits:int=2) -> int:
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
        ans += get_largest_joltage(l, digits)
    return ans
