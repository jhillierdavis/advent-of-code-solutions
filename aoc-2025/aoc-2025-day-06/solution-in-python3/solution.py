# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_initial_operator_value(op:str):
    if op == '*':
        return 1
    
    if op == '+':
        return 0
    
    raise Exception(f"Unknown operator={op}")


def apply_operation_to_value(op:str, value:int, amendment:int) -> int:
    result = value
    if op == '*':
        result *= amendment
    elif op == '+':
        result += amendment
    else:
        raise Exception(f"Unknown operator={op}")    
    return result


def get_column_widths(lines):
    op_line = lines[-1]
    #logger.debug(f"op_line={op_line}")

    # Determine columns size
    c_size = 0
    column_widths = list()
    for i, c in enumerate(op_line):
        #logger.debug(f"i={i} c={c}")
        if c in ['+', '*'] or i >= len(op_line) -1:
            if i >= len(op_line) -1:
                c_size += 1
            if c_size > 0:
                #logger.debug(f"i={i} c_size={c_size}")
                column_widths.append(c_size)
                c_size = 0
        c_size += 1

    #logger.debug(f"op_line={op_line}")
    #logger.debug(f"column_widths={column_widths}")
    return column_widths


def get_adjusted_lines_from_file(filename):
    lines = list()
    with open(filename, "r") as f:
        for line in f:
            # Add space character to end-of-line to aid processing by space stripping per (space separated) entry
            lines.append(line + ' ') 
    return lines


def get_operator_row_index_from_input_data(lines):
    op_row_idx = len(lines) - 1  
    return op_row_idx  


def get_row_entries_map_from_input_data(lines):
    column_widths = get_column_widths(lines)
    op_row_idx = get_operator_row_index_from_input_data(lines)

    entry_map = dict()
    for i, l in enumerate(lines):
        vals = list()
        idx = 0
        for j, cw in enumerate(column_widths):
            if j >= len(column_widths):
                entry = l[idx:idx+cw]
            else:
                entry = l[idx:idx+cw-1]
            
            if i < op_row_idx:
                vals.append(entry)
            else:
                vals.append(entry.strip())

            idx += cw
        #logger.debug(f"i={i} vals={vals}")

        entry_map[i] = vals
    return entry_map


def get_column_operator_list(lines, column_entry_map):
    op_idx = len(lines) - 1            
    column_operator_list = column_entry_map[op_idx]
    return column_operator_list


def get_column_entries_at_index(row_entries_map, column_index:int):
    column_entry_list = list()

    size = len(row_entries_map.keys()) -1 # Subtract 1 for the last operator row

    # Iterate through each row of input data (up to, but not including, the last operator row)             
    for row_idx in range(size):
        row_entry = row_entries_map[row_idx]
        column_entry_list.append(row_entry[column_index])

    return column_entry_list


def solve_part1(filename):
    lines = get_adjusted_lines_from_file(filename)
    row_entries_map = get_row_entries_map_from_input_data(lines)    
    total_sum = sum_column_values(row_entries_map, apply_part1_cephalopod_math_to_column_entry_values)
    return total_sum


def solve_part2(filename):
    lines = get_adjusted_lines_from_file(filename)
    row_entries_map = get_row_entries_map_from_input_data(lines)    
    total_sum = sum_column_values(row_entries_map, apply_part2_cephalopod_math_to_column_entry_values)
    return total_sum


def sum_column_values(row_entries_map:dict[int, list[str]], func:callable) -> int:
    last_row_index = len(row_entries_map.keys()) -1
    column_operators = row_entries_map[last_row_index] 

    total_sum = 0
    for col_idx, op in enumerate(column_operators):
        column_entry_list = get_column_entries_at_index(row_entries_map, col_idx)

        result = func(column_entry_list, op)
        total_sum += result
    
    return total_sum


def apply_part1_cephalopod_math_to_column_entry_values(nums, op):
    result = get_initial_operator_value(op)
    
    for entry in nums:
        num = int(entry)
        result = apply_operation_to_value(op, result, num)    

    return result


def apply_part2_cephalopod_math_to_column_entry_values(nums, op):
    result = get_initial_operator_value(op)
    
    size = len(nums[0])
    for i in range(size):
        v = column_number_value_at_index(nums, i)
        result = apply_operation_to_value(op, result, v)

    return result


def column_number_value_at_index(column_entry_list:list[str], idx:int) -> int:
    result = 0
    multiplier = 1
    
    # Work row data from bottom to top
    reversed_column_entry_list = reversed(column_entry_list) 

    for n in reversed_column_entry_list:
        if n[idx] == ' ':
            continue

        val = int(n[idx])        
        result += (val * multiplier)
        #logger.debug(f"idx={idx} val={val} multiplier={multiplier} result={result}")
        multiplier *=10

    return result