#import re

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


def get_equation_map_from_lines(lines):
    eq_map = dict()

    for i, l in enumerate(lines):
        #values = re.split(" +",l)
        values = l.split()
        #logger.debug(f"values={values}")

        if values[0] in ['*', '+']:
            eq_map[i] = values
        else:
            int_vals = list()
            for v in values:
                int_vals.append(int(v))
            #logger.debug(f"int_val={int_vals}")
            eq_map[i] = int_vals

    return eq_map


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    eq_map = get_equation_map_from_lines(lines)
    
    #logger.debug(f"eq_map={eq_map}")

    size = len(eq_map)
    op_idx = size - 1
    operators = eq_map[op_idx]
    #logger.debug(f"operators={operators}")

    ans = 0    
    for i, op in enumerate(operators):
        result = get_initial_operator_value(op)

        for x in range(op_idx):
            vals = eq_map[x]
            result = apply_operation_to_value(op, result, vals[i])        

        #logger.debug(f"i={i} op={op} result={result} ans={ans}")
        ans += result

    return ans


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


def to_num(nums, idx):
    result = 0
    multiplier = 1
    for n in nums:
        if n[idx] == ' ':
            continue
        val = int(n[idx])        
        result += (val * multiplier)
        #logger.debug(f"idx={idx} val={val} multiplier={multiplier} result={result}")
        multiplier *=10
    result = int((str(result)[::-1]))
    #logger.debug(f"nums={nums} idx={idx} result={result}")
    return result


def calculate(nums, op):
    #logger.debug(f"nums={nums} op={op}")

    result = get_initial_operator_value(op)
    
    size = len(nums[0])
    for i in range(size):
        v = to_num(nums, i)
        result = apply_operation_to_value(op, result, v)

    return result


def get_adjusted_lines_from_file(filename):
    lines = list()
    with open(filename, "r") as f:
        for line in f:
            lines.append(line + ' ')
    return lines


def get_entry_map(lines):
    column_widths = get_column_widths(lines)
    op_idx = len(lines) - 1

    entry_map = dict()
    for i, l in enumerate(lines):
        vals = list()
        idx = 0
        for j, cw in enumerate(column_widths):
            if j >= len(column_widths):
                entry = l[idx:idx+cw]
            else:
                entry = l[idx:idx+cw-1]
            
            if i < op_idx:
                vals.append(entry)
            else:
                vals.append(entry.strip())

            idx += cw
        #logger.debug(f"i={i} vals={vals}")

        entry_map[i] = vals
    return entry_map


def solve_part2(filename):
    lines = get_adjusted_lines_from_file(filename)

    entry_map = get_entry_map(lines)

    op_idx = len(lines) - 1            
    operators = entry_map[op_idx]
    #logger.debug(f"operators={operators}")

    ans = 0    
    
    for i, op in enumerate(operators):
        nums = list()

        for x in range(op_idx):
            vals = entry_map[x]
            nums.append(vals[i])

        result = calculate(nums, op)
        #logger.debug(f"i={i} op={op} nums={nums} result={result}")
        ans += result
    
    return ans