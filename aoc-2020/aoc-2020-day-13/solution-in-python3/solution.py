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

    earliest_departure = int(lines[0])
    buses = lines[1].split(',')
    while 'x' in buses:
        buses.remove('x')
    buses = list(map(int, buses))

    logger.debug(f"earliest_departure={earliest_departure} buses={buses}")

    min_wait = max(buses) + 1
    bus_to_get = None
    for bus in buses:
        remainder = earliest_departure % bus
        wait = bus - remainder
        if wait < min_wait:            
            min_wait = wait
            bus_to_get = bus
            logger.debug(f"bus={bus} wait={wait} ans={bus*wait} remainder={remainder}")

    return min_wait * bus_to_get

import math


def get_earliest_sequence_timestamp(input, offset = 0):
    buses = [-1 if item == 'x' else int(item) for item in input]
    

    found = False    
    timestamp = offset//buses[0] * buses[0] if offset > 0 else 0
    assert buses[0] > 0
    size = len(buses) -1

    logger.debug(f"buses={buses} size={size} timestamp={timestamp}")

    while not found:
        timestamp += buses[0]

        for i, e in enumerate(buses):
            if e < 0:
                continue

            if (timestamp + i) % e != 0:
                break
            
            if i == size:
                found = True
        
    return timestamp
 
import crt # for CRT (Chinese Remainder Theorem) from modular number theory
#from sympy.ntheory.modular import crt # Alternately use sympy

def get_earliest_sequence_timestamp_using_crt(input:list):
    moduli_list = list()
    remainder_list = list()

    for i,e in enumerate(input):
        if not e == 'x':
            v = int(e)
            moduli_list.append(v)
            #r = -i % v # TODO: Explain this part!   
            #logger.debug(f"r={r} v={v} i={i} for input={input}")

            # Determine the remainder at timestamp t (when the 1st value has no remainder) 
            r = v - (i % v)   
            #assert v > i, f"r={r} v={v} i={i} for input={input}" 
            
            remainder_list.append(r)

    logger.debug(f"remainder_list={remainder_list} moduli_list={moduli_list}")
    timestamp = crt.chinese_remainder_theorem(remainder_list, moduli_list)
    #timestamp = crt(remainder_list, moduli_list)

    return timestamp


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    buses = lines[1].split(',')
    return get_earliest_sequence_timestamp_using_crt(buses)
