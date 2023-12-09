from helpers import fileutils, strutils

def get_sequence_incremental_difference(sequence):
    diff_list = []
    for i in range(len(sequence) -1):
        diff = sequence[i+1] - sequence[i]
        #print(f"DEBUG: {sequence[i]} {sequence[i+1]} -> {diff}")
        diff_list.append(diff)
    return diff_list


def get_sequence_extrapolated_placeholders(sequence, index):
    placeholders = []
    diff_list = sequence
    # While all previous differences are not zero, calculate the next set of differences (e.g. next layer down)
    while not (len(set(diff_list)) == 1 and diff_list[0] == 0):
        diff_list = get_sequence_incremental_difference(diff_list)
        placeholders.append(diff_list[index])
    #print(f"DEBUG: last_value={sequence[-1]} placeholders={placeholders}")
    return placeholders

def get_sequence_next_value(sequence):
    placeholders = get_sequence_extrapolated_placeholders(sequence, -1)
    # Add the last sequence value to the sum of the last of each of the placeholder values
    return sequence[-1] + sum(placeholders) 

def get_sequence_previous_value(sequence):
    placeholders = get_sequence_extrapolated_placeholders(sequence, 0)
    # Subtract the subtraction the first of each of the placeholder values from the first sequence value
    return sequence[0] - subtract_placeholders(placeholders)

def subtract_placeholders(placeholders):
    placeholders.reverse()
    diff = 0
    for i in range(len(placeholders)):
        diff = placeholders[i] - diff
    return diff

def sum_execution_per_file_line(filename, func):
    lines = fileutils.get_file_lines(filename)

    ans = 0
    for l in lines:
        sequence = strutils.string_to_int_list(l)
        next = func(sequence)        
        sequence.append(next)
        #print(f"DEBUG: {sequence}")
        ans += next
    return ans

def solve_part1(filename):
    return sum_execution_per_file_line(filename, get_sequence_next_value)

def solve_part2(filename):
    return sum_execution_per_file_line(filename, get_sequence_previous_value)