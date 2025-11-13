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
            #logger.debug(f"i={i} new_value={new_value}")                

    #logger.debug(f"new_value={new_value}")
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


def combine_with_mask_value_part2(value, current_mask):
    new_value = ""
    for i in range(len(current_mask)):
        if current_mask[i] == '0':
            new_value += value[i]
        elif current_mask[i] == '1':
            new_value += '1'
        else:
            new_value += current_mask[i]
    return new_value


def add_values(result, xmask, offset, value):
    size = len(xmask) 
    if offset >= size:
        result.add(value)
        return
    
    prefix = value
    for i in range(offset, size):
        if xmask[i] == 'X':
            add_values(result, xmask, i+1, prefix + '0')
            add_values(result, xmask, i+1, prefix + '1')
            break
        else:
            prefix += xmask[i]
    return result


def generate_floating_value_set(xmask):
    result = set()
    if 'X' not in xmask:
        result.add(xmask)
        return result
    
    add_values(result, xmask, 0, "")
    return result

"""
def generate_floating_values(s):
    if 'X' not in s:
        return s

    addresses = []
    xi = s.index('X')
    s0 = s[:xi] + '0' + s[xi+1:]
    s1 = s[:xi] + '1' + s[xi+1:]

    addresses += generate_floating_values(s0) + ',' + generate_floating_values(s1)
    return addresses
"""

def generate_floating_values(s, results:list):
    if 'X' not in s:
        results.append(s)
        return
    
    xi = s.index('X')
    s0 = s[:xi] + '0' + s[xi+1:]
    s1 = s[:xi] + '1' + s[xi+1:]

    generate_floating_values(s0, results)
    generate_floating_values(s1, results)
    return


def generate_floating_value_set_as_intergers(xmask):
    #results = sorted(generate_floating_value_set(xmask))
    results = []
    generate_floating_values(xmask, results)
    converted_results = set()
    for r in results:
        converted_results.add(int(r,2))
    return converted_results

def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    memvalues = defaultdict(set[int])
    
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
            value = format(index, '0' + str(mask_length) + 'b')
            logger.debug(f"l={l} index={index} value={value} current_mask={current_mask}")
            
            xmask = combine_with_mask_value_part2(value, current_mask)
            values = generate_floating_value_set_as_intergers(xmask)
            logger.debug(f"current_mask={current_mask} xmask={xmask}, index={index} values={values}")
            for v in values:                
                memvalues[v] = nums[1]           

    #logger.debug(memvalues)
    return sum(memvalues.values())

#xmask = '1X0XX'
#print(sorted(generate_floating_value_set(xmask)))
#print(get_addresses(xmask))