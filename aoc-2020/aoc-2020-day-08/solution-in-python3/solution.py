# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def get_operation_list(lines):
    operation_list = []

    for l in lines:
        o, v = l.split(' ')
        logger.debug(f"o={o}, v={v}")
        operation_list.append((o, int(v)))
 
    return operation_list

def get_accumulator(operation_list):
    size = len(operation_list)

    accumulator = 0
    executed = set()
    index = 0
    is_looping = False
    
    while(True):
        if index >= size:
            break
        
        e = operation_list[index]
        logger.debug(f"index={index} e={e} accumulator={accumulator}")
        if index in executed:
            logger.debug(f"Loop at index={index}")
            is_looping = True
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

    return accumulator, is_looping



def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    operation_list = get_operation_list(lines)

    size = len(operation_list)                          
    logger.debug(f"operation_list={operation_list} size={size}")

    accumulator, _ = get_accumulator(operation_list)
    return accumulator

def get_variants(operation_list):
    variants_list = []
    variants_list.append(operation_list)

    for i, e in enumerate(operation_list):
        o, v = e
        if o == 'nop':
            copy_list = operation_list.copy()
            copy_list[i] = ('jmp', v)
            variants_list.append(copy_list)
        elif o == 'jmp':
            copy_list = operation_list.copy()
            copy_list[i] = ('nop', v)
            variants_list.append(copy_list)

    return variants_list


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    operation_list = get_operation_list(lines)

    size = len(operation_list)                          
    logger.debug(f"operation_list={operation_list} size={size}")

    variants_list = get_variants(operation_list)
    for vl in variants_list:
        logger.debug(f"vl={vl}")
        accumulator, is_looping = get_accumulator(vl)
        if not is_looping:
            return accumulator
    return -1

