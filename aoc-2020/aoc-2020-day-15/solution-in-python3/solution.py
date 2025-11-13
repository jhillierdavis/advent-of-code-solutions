# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

from collections import defaultdict


def last_index_of(lst, value):
    """
    Returns the index of the last occurrence of 'value' in the list 'lst'.
    If the value is not found, returns -1.
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1


def solve_part1(starting_values, nth=2020):  
    sequence = []
    current_value = 0
    size = len(starting_values)

    for i in range(0, nth):
        if i < size:
            current_value = starting_values[i]
            logger.debug(f"Starting value: i={i} current_value={current_value} sequence={sequence} nth={nth}")
            if i < size -1:
                sequence.append(current_value)
                continue
            
        if i == nth -1:
            break

        last_index = last_index_of(sequence, current_value)
        sequence.append(current_value)
        if last_index >= 0:
            logger.debug(f"i={i} current_value={current_value} last_index={last_index} sequence={sequence}")
            current_value = i - last_index
        else:            
            current_value = 0
        logger.debug(f"i={i} current_value={current_value}")

    return current_value


def solve_part2(starting_values, nth=2020):
    age = defaultdict(lambda:-1)
    current_value = 0
    size = len(starting_values)

    for i in range(0, nth):
        if i < size:
            current_value = starting_values[i]            
            if i < size -1:
                age[current_value] = i
                continue
            
        if i == nth -1:
            break

        last_index = age[current_value]
        age[current_value] = i
        if last_index >= 0:
            #logger.debug(f"i={i} current_value={current_value} last_index={last_index}")
            current_value = i - last_index
        else:            
            current_value = 0
        #logger.debug(f"i={i} current_value={current_value}")

    return current_value

