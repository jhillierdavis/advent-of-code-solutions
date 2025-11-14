# Shared helper libraries
from helpers import fileutils, numutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def extract_anonymous_ranges(lines):
    ranges = list()
    for l in lines:
        vals = l.split(' ')
        #logger.debug(f"line={l} vals={vals}")
        for v in vals:
            if '-' in v:
                vmin, vmax = v.split("-")
                #logger.debug(f"vmin={vmin}, vmax={vmax}")
                ranges.append((int(vmin), int(vmax)))
        
    #logger.debug(f"ranges={ranges}")
    return ranges


def count_invalid_nearby_ticket_entries(lines, ranges):
    found = False
    ans = 0
    for l in lines:
        if l == 'nearby tickets:':
            found = True
            continue

        if found:            
            logger.debug(f"l={l}")    
            vals = l.split(',')
            for v in vals:
                is_valid = False
                vnum = int(v)
                for r in ranges:
                    if numutils.is_within_range(vnum, r[0], r[1]):
                        is_valid = True
                        continue
                if not is_valid:
                    ans += vnum
    return ans


def solve_part1(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    ranges = extract_anonymous_ranges(lines)

    lines = fileutils.get_lines_after_empty_from_file(filename)
    ans = count_invalid_nearby_ticket_entries(lines, ranges)
    return ans


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
