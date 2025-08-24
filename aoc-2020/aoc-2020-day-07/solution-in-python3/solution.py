# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def get_child_bag_map_count(suffix_line):
    child_bag_to_count_map = dict()

    if suffix_line == 'no other bags.':
        return child_bag_to_count_map

    if ', ' in suffix_line:
        child_bag_list = suffix_line.split(', ') 
        #logger.debug(f"child_bag_list={child_bag_list}")
        for c in child_bag_list:
            s , _ = c.split(" bag")
            count, child_bag = s.split(' ', 1)
            child_bag_to_count_map[child_bag] = int(count)
    else:
        s , _ = suffix_line.split(" bag")
        count, child_bag = s.split(' ', 1)
        child_bag_to_count_map[child_bag] = int(count)

    return child_bag_to_count_map


def get_parents(bag_map, child_bag_to_match):
    direct_parent_set = set()
    for k,v in bag_map.items():
        for sk, _ in v.items():
            if sk == child_bag_to_match:
                direct_parent_set.add(k)
                continue

    grandparent_set = set()
    for dp in direct_parent_set:
        grandparent_set = grandparent_set | get_parents(bag_map, dp)
    return direct_parent_set | grandparent_set

def get_bag_map_from_lines(lines):
    bag_map = dict()

    for l in lines:
        #logger.debug(f"l={l}")
        pre, post = l.split(' contain ')
        parent_bag, _ = pre.split(" bags")
        #logger.debug(f"parent_bag={parent_bag}")

        child_bag_map_count = get_child_bag_map_count(post)
        bag_map[parent_bag] = child_bag_map_count
        
    #logger.debug(f"bag_map={bag_map}")
    return bag_map


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    bag_map = get_bag_map_from_lines(lines)

    direct_parent_set = get_parents(bag_map, 'shiny gold')

    #logger.debug(f"direct_parent_set={direct_parent_set}")
    return len(direct_parent_set)


def get_child_bag_count(bag_map, bag_name_to_match):
    count = 1
    child_bag_map = bag_map[bag_name_to_match]
    #logger.debug(f"bag_name_to_match={bag_name_to_match} child_bag_map={child_bag_map}")
    for k,v in child_bag_map.items():
        count += v * get_child_bag_count(bag_map, k)
    return count

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    bag_map = get_bag_map_from_lines(lines)

    count = get_child_bag_count(bag_map, 'shiny gold')

    return count -1
