# Local
from helpers import fileutils 

def get_pair_insertion_rules(filename):
    lines = fileutils.get_lines_after_empty_from_file(filename)

    map_insertion_rules = {}
    for l in lines:
        key_value = l.split(" -> ")
        key = key_value[0]
        value = key_value[1]
        map_insertion_rules[key] = value

    return map_insertion_rules

def get_insertion_char(map_insertion_rules, before, after):
    return map_insertion_rules[before + after]

