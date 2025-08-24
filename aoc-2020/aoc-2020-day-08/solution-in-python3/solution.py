# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    operation_list = []

    for l in lines:
        o, v = l.split(' ')
        logger.debug(f"o={o}, v={v}")
        operation_list.append((o, int(v)))

    size = len(operation_list)                          
    logger.debug(f"operation_list={operation_list} size={size}")

    accumulator = 0
    executed = set()

    index = 0
    
    while(True):
        
        e = operation_list[index]
        logger.debug(f"index={index} e={e} accumulator={accumulator}")
        if index in executed:
            logger.debug(f"Loop at index={index}")
            break
        else:
            executed.add(index)
        
        o, v = e
        if o == 'nop':
            index += 1
        elif o == 'acc':
            accumulator += v
            index += 1
        elif o == 'jmp':
            if v >= 0:
                index += (v % size)
            else:
                offset = (abs(v) % size)
                index -= offset
                logger.debug(f"Jump: index={index} v={v} offset={offset}")

    return accumulator

def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
