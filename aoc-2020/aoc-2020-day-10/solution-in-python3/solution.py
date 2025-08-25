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

    adaptor_list.sort()

    max_adaptor = max(adaptor_list)
    adaptor_list.append(max_adaptor + 3)

    logger.debug(f"adaptor_list={adaptor_list}")
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


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"