import math
import utils

# Ref.: https://adventofcode.com/2021/day/1

def count_sequential_increases(list_integers):
    value_last:int = math.nan
    count_sequential_increases:int = 0
    for value_current in list_integers:
        if False == math.isnan(value_last) and (value_current > value_last):
            count_sequential_increases += 1
        value_last = value_current

    return count_sequential_increases


def count_sequential_increases_from_file(filename):
    lines = utils.get_file_lines(filename)
    array_ints = utils.string_to_integer_array(lines)
    return count_sequential_increases(array_ints)


def count_sliding_window_increases_from_file(filename):
    lines = utils.get_file_lines(filename)
    #print(f"DEBUG: lines={lines}")  

    list_windows = []
    length = len(lines)
    for i in range(length):
        if i <= length - 3:
            list_windows.append( int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) )         
    
    #print(f"DEBUG: list_windows={list_windows}")    
    return count_sequential_increases(list_windows)