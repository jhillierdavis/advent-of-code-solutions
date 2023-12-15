from collections import defaultdict

from helpers import fileutils

def hash_of(input):
    value = 0

    for i in range(len(input)):
        char = input[i]
        value += ord(char)
        value *= 17
        value = value % 256        
    return value

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    assert len(lines) == 1

    entries = lines[0].split(',')
    print(f"DEBUG: entries={entries}")

    sum = 0
    for e in entries:
        sum += hash_of(e)
    return sum

def focusing_power_of(input):
    # TODO
    return 0

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    assert len(lines) == 1

    entries = lines[0].split(',')
    print(f"DEBUG: entries={entries}")

    sum = 0
    for e in entries:
        sum += focusing_power_of(e)
    return sum

