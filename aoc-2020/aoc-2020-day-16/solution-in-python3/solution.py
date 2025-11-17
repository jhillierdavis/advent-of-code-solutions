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
        s = l.split(': ')
        field = s[0]
        vals = s[1].split(' or ')
        #logger.debug(f"line={l} vals={vals}")
        for v in vals:
            if '-' in v:
                vmin, vmax = v.split("-")
                #logger.debug(f"vmin={vmin}, vmax={vmax}")
                ranges.append((int(vmin), int(vmax)))
        field_ranges[field] = ranges
    #logger.debug(f"ranges={ranges}")
    return field_ranges


def get_single_value_keys(d):
    single_value_keys = set()
    for k, v in d.items():
        if len(v) == 1:
            single_value_keys.add( list(v)[0] )
    return single_value_keys


def are_all_single_valued(d):
    num = len(d.keys())
    single_count = 0
    for v in d.values():
        if len(v) == 1:
            single_count += 1
    return num == single_count



def get_field_order(filename):    
    field_ranges = extract_field_ranges(filename)

    logger.debug(f"field_ranges={field_ranges}")    

    num_fields = len(field_ranges.keys())

    d = dict()
    for x in range(num_fields):
        d[x] = set(field_ranges.keys())

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

    
    for k, v in d.items():
        logger.debug(f"{k}={v}")

    
    i = 0
    while not are_all_single_valued(d) and i < 100:
        single_value_keys = get_single_value_keys(d)
        logger.debug(f"single_value_keys={single_value_keys}")


        for k, v in d.items():
            if len(v) > 1:
                logger.debug(f"Remove at: k={k} v={v}")
                for svk in single_value_keys:
                    if svk in v:
                        v.remove(svk)

        for k, v in d.items():
            logger.debug(f"{k}={v}")
        i += 1

    ans = list()
    for i in range(len(d.keys())):
        ans.append(list(d[i])[0])    
    return ans


def get_valid_your_ticket_entries(lines):
    found = False
    for l in lines:    
        if l == 'your ticket:':
            found = True
            continue

        if found:            
            vals = l.split(',')
            return list(map(int, vals))
    return None
            


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    fields = get_field_order(filename)

    lines = fileutils.get_lines_after_empty_from_file(filename)
    vals = get_valid_your_ticket_entries(lines)

    ans = 1
    for i, f in enumerate(fields):
        if f.startswith('departure'):
            logger.debug(f"f={f} i={i} vals={vals[i]}")
            ans *= vals[i]

    logger.debug(f"vals={vals}")
    return ans
