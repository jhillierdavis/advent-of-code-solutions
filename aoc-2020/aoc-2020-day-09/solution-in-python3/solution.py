# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def get_input_list(lines):
    input_list = []
    for l in lines:
        input_list.append(int(l))
    return input_list


def solve_part1(filename, preamble:int):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    input_list = get_input_list(lines)
    logger.debug(f"input_list={input_list}")

    """
    preamble_list = []
    for i in range(preamble):
        preamble_list.append(input_list[i])

    logger.debug(f"preamble_list={preamble_list}")

    valid_set = set()   
    for i, e in enumerate(preamble_list):
        for j in range(i+1, preamble):
            valid_set.add(e + preamble_list[j])

    logger.debug(f"valid_set={valid_set}")
    """

    for i, e in enumerate(input_list):
        logger.debug(f"i={i} e={e}")
        if i < preamble:
            continue

        preamble_list = []
        for x in range(i-preamble, i):
            preamble_list.append(input_list[x])
        logger.debug(f"i={i} preamble_list={preamble_list}")

        valid_set = set()   
        for j, je in enumerate(preamble_list):
            for k in range(j+1, preamble):
                valid_set.add(je + preamble_list[k])

        logger.debug(f"valid_set={valid_set}")

        if not e in valid_set:
            return e

    return -1


def get_contiguous_sum_values(input_list, index, contiguous_sum):
    size = len(input_list)
    value_set = set()

    current_sum = 0
    for i in range(index, size):
        value = input_list[i]
        value_set.add(value)
        current_sum += value
        logger.debug(f"i={i} value={value} current_sum={current_sum} contiguous_sum={contiguous_sum}")
        if current_sum == contiguous_sum:            
            return value_set
        elif current_sum > contiguous_sum:
            return None
    return None

def solve_part2(filename, contiguous_sum):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    input_list = get_input_list(lines)
    logger.debug(f"input_list={input_list}")

    for i, e in enumerate(input_list):
        first = e
        value_set = get_contiguous_sum_values(input_list, i, contiguous_sum)
        if value_set:
            min_value = min(value_set)
            max_value = max(value_set)
            logger.debug(f"min_value={min_value} max_value={max_value}")
            return min_value + max_value

    return -1
