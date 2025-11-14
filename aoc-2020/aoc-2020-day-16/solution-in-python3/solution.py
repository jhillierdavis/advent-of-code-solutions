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
            #logger.debug(f"l={l}")    
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


def get_valid_nearby_ticket_entries(lines, ranges):
    found = False
    valid_lines = list()
    for l in lines:
        if l == 'nearby tickets:':
            found = True
            continue

        if found:            
            #logger.debug(f"l={l}")    
            vals = l.split(',')

            
            for v in vals:
                is_valid = False                
                vnum = int(v)
                for r in ranges:
                    if numutils.is_within_range(vnum, r[0], r[1]):
                        is_valid = True                        
                        continue
                if not is_valid:
                    break

            if is_valid:
                valid_list = list()
                for v in vals:
                    vnum = int(v)
                    valid_list.append(vnum)
                valid_lines.append(valid_list)
                    
    return valid_lines


def get_valid_nearby_tickets(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    ranges = extract_anonymous_ranges(lines)

    lines = fileutils.get_lines_after_empty_from_file(filename)
    valid_nearby = get_valid_nearby_ticket_entries(lines, ranges)
    return valid_nearby


def extract_field_ranges(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    field_ranges = dict()
    
    for l in lines:
        ranges = list()
        vals = l.split(' ')
        field = vals[0][:-1]
        #logger.debug(f"line={l} vals={vals}")
        for v in vals:
            if '-' in v:
                vmin, vmax = v.split("-")
                #logger.debug(f"vmin={vmin}, vmax={vmax}")
                ranges.append((int(vmin), int(vmax)))
        field_ranges[field] = ranges
    #logger.debug(f"ranges={ranges}")
    return field_ranges


def get_field_order(filename):    
    field_ranges = extract_field_ranges(filename)

    logger.debug(f"field_ranges={field_ranges}")
    num_fields = len(field_ranges.keys())

    d = dict()
    for x in range(num_fields):
        d[x] = set(field_ranges.keys())

    logger.debug(f"d={d}")

    valid_nearby = get_valid_nearby_tickets(filename)

    for kfr, vfr in field_ranges.items():
        for vn in valid_nearby:
            
            for i, v in enumerate(vn):
                is_valid = False    
                for r in vfr:
                    if numutils.is_within_range(v, r[0], r[1]):
                        is_valid = True
#                if is_invalid:
#                    logger.debug(f"{kfr} invalid in range at {i}!") 
                if not is_valid:
                    s = d[i]
                    s.remove(kfr)
                    d[i] = s

    logger.debug(f"d={d}")

    return []


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_lines_before_empty_from_file(filename)
    ranges = extract_anonymous_ranges(lines)

    lines = fileutils.get_lines_after_empty_from_file(filename)
    valid_nearby = get_valid_nearby_ticket_entries(lines, ranges)

    logger.debug(f"valid_nearby={valid_nearby}")
    return "TODO"
