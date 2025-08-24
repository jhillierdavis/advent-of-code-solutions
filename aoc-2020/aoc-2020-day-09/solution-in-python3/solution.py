# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def solve_part1(filename, preamble:int):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    input_list = []
    for l in lines:
        input_list.append(int(l))

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


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
