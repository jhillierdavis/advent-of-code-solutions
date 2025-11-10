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

import re

def extract_numbers(input_string):
    return [int(num) for num in re.findall(r'\d+', input_string)]


def combine_with_mask_value(value, current_mask):
    new_value = ""
    for i in range(len(current_mask)):
        if current_mask[i] == 'X':
            new_value += value[i]
        else:
            new_value += current_mask[i]
            logger.debug(f"i={i} new_value={new_value}")                

    logger.debug(f"new_value={new_value}")
    return new_value


def solve_part1(filename):
    logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    memvalues = defaultdict(int)
    
    current_mask = None
    mask_length = 36
    for l in lines:
        if len(l) == 0:
            continue

        k,v = l.split(" = ")
        #logger.debug(f"{l} k={k} v={v}")
        
        if k.startswith('mask'):            
            #logger.debug(f"mask = {v}")
            current_mask = v
        elif k.startswith('mem'):
            nums = extract_numbers(l)
            index = nums[0]
            value = format(nums[1], '0' + str(mask_length) + 'b')
            #logger.debug(f"index={index} value={value} current_mask={current_mask}")
            
            new_value = combine_with_mask_value(value, current_mask)
            memvalues[index] = int(new_value,2)

    total = sum(memvalues.values())
    return total


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
