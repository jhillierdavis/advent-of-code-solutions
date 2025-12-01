# Shared helper libraries
from helpers import fileutils
from typing import Tuple

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_rotation_direction_and_amount(rotation:str) -> Tuple[str, int]:
    direction = rotation[0]
    amount = int(rotation[1:])
    assert(amount >= 0)
    return direction, amount


def determine_new_dial_value_and_count_zero_values(dial_value:int, direction:str, amount:int) -> Tuple[str, int]:
    zero_value_count = 0
    new_dial_value = dial_value

    if 'L' == direction:
        new_dial_value -= amount            
    elif 'R' == direction:
        new_dial_value += amount
    else:
        raise Exception(f"Unknown direction={direction}")

    new_dial_value %= 100
    if new_dial_value == 100:
        zero_value_count = 0
    
    if new_dial_value == 0:
        zero_value_count += 1

    return new_dial_value, zero_value_count


def execute_algorithm_for_input_file_entries(filename:str, alg:callable) -> int:
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    dial_value = 50 # Initial dial value

    for l in lines:
        direction, amount = get_rotation_direction_and_amount(l)        

        dial_value, zero_value_count = alg(dial_value, direction, amount)
        ans += zero_value_count

    return ans


def solve_part1(filename:str) -> int:
    return execute_algorithm_for_input_file_entries(filename, determine_new_dial_value_and_count_zero_values)


def determine_new_dial_value_and_count_all_zero_clicks_via_unit_increments(value:int, direction:str, amount:int) -> Tuple[str, int]:
    zero_clicks = 0    
    for _ in range(amount):
        value, zero_value_count = determine_new_dial_value_and_count_zero_values(value, direction, 1)
        zero_clicks += zero_value_count
    return value, zero_clicks


def solve_part2_using_single_unit_increments(filename:str) -> int:
    return execute_algorithm_for_input_file_entries(filename, determine_new_dial_value_and_count_all_zero_clicks_via_unit_increments)


def is_passing_zero_by_rotating_left(value:int, offset:int) -> bool:
    diff = value - offset
    return value > 0 and diff < 0


def is_passing_zero_by_rotating_right(value:int, offset:int) -> bool:
    diff = value + offset
    return value > 0 and diff > 100


def determine_new_dial_value_and_count_all_zero_clicks_via_offset(value:int, direction:str, amount:int) -> Tuple[str, int]:
    
    # circuits = amount // 100  
    # offset = amount % 100
    circuits, offset = divmod(amount, 100)      
    ans = circuits    

    if 'L' == direction:
        if is_passing_zero_by_rotating_left(value, offset):            
            ans += 1
        value -= offset      
    elif 'R' == direction:
        if is_passing_zero_by_rotating_right(value, offset):
            ans += 1
        value += offset
    else:
        raise Exception(f"Unknown direction={direction}")

    value %= 100
    if value == 100:
        value = 0
        
    if value == 0:
        ans += 1
    
    return value, ans


def solve_part2_using_modular_arithemtic_offset(filename:str) -> int:
    return execute_algorithm_for_input_file_entries(filename, determine_new_dial_value_and_count_all_zero_clicks_via_offset)