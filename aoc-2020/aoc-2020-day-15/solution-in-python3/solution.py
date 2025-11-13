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


def solve(starting_values, nth):
    assert nth >= 0
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

