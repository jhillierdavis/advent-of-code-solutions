# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_sorted_ascending_adaptor_list(filename):
    lines = fileutils.get_file_lines_from(filename)

    adaptor_list = []
    for l in lines:
        adaptor_list.append(int(l))    

    # Add the initial charging outlet (with value zero)
    adaptor_list.append(0)

    # Add the device's built-in adapter 
    max_adaptor = max(adaptor_list)
    adaptor_list.append(max_adaptor + 3)

    adaptor_list.sort()

    logger.debug(f"Sorted (asc.) adaptor_list={adaptor_list}")
    return adaptor_list


def get_jolt_diffs(adaptor_list:list, increment:int) -> int:
    count = 0
    prior_value = 0
    for a in adaptor_list:
        diff = a - prior_value
        if diff == increment:
            count += 1
        prior_value = a
    return count



def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")

    adaptor_list = get_sorted_ascending_adaptor_list(filename)
    jolt_diffs_of_1 = get_jolt_diffs(adaptor_list, 1)
    jolt_diffs_of_3 = get_jolt_diffs(adaptor_list, 3)

    return jolt_diffs_of_1 * jolt_diffs_of_3


def get_arrangements(adaptor_list:list, index:int, cache:dict) -> int:
    
    size = len(adaptor_list)
    if index >= size:
        return 1 # Base case

    value = adaptor_list[index]
    if value in cache.keys():
        return cache[value]
    
    arrangements = 1
    for i in range(3):
        next_index = index + 1 + i        
        if next_index < size - 1:
            next_value = adaptor_list[next_index]
            if (next_value - value) > 3:
                continue

            if i == 0:
                arrangements = get_arrangements(adaptor_list, next_index, cache)
            else:
                arrangements += get_arrangements(adaptor_list, next_index, cache)    

    cache[value] = arrangements
    return arrangements


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    adaptor_list = get_sorted_ascending_adaptor_list(filename)

    cache = dict()
    arrangement_count = get_arrangements(adaptor_list, 0, cache)
    return arrangement_count