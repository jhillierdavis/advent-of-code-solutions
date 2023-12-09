from helpers import fileutils

from collections import defaultdict

def get_sequence_incremental_difference(sequence):
    diff_list = []
    length = len(sequence)
    for i in range(length -1):
        diff = sequence[i+1] - sequence[i]
        #print(f"DEBUG: {sequence[i]} {sequence[i+1]} -> {diff}")
        diff_list.append(diff)
    #print(f" ")
    return diff_list
    

def get_sequence_next_value(sequence):
    placeholders = []

    diff_list = sequence
    while not (len(set(diff_list)) == 1 and diff_list[0] == 0):
        diff_list = get_sequence_incremental_difference(diff_list)
        placeholders.append(diff_list[-1])
    #print(f"DEBUG: last_value={sequence[-1]} placeholders={placeholders}")
    return sequence[-1] + sum(placeholders)


def line_to_list(line):
    return list(map(int, line.split()))

def subtract_placeholders(placeholders):
    placeholders.reverse()
    length = len(placeholders)
    diff = 0
    for i in range(length):
        diff = placeholders[i] - diff
    return diff


def get_sequence_previous_value(sequence):
    placeholders = []

    diff_list = sequence
    while not (len(set(diff_list)) == 1 and diff_list[0] == 0):
        diff_list = get_sequence_incremental_difference(diff_list)
        placeholders.append(diff_list[0])
    #print(f"DEBUG: first_value={sequence[0]} placeholders={placeholders}")
    return sequence[0] - subtract_placeholders(placeholders)


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    ans = 0
    for l in lines:
        sequence = line_to_list(l)
        next = get_sequence_next_value(sequence)        
        sequence.append(next)
        #print(f"DEBUG: {sequence}")
        ans += next

    return ans

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    
    ans = 0
    for l in lines:
        sequence = line_to_list(l)
        next = get_sequence_previous_value(sequence)        
        ans += next

    return ans