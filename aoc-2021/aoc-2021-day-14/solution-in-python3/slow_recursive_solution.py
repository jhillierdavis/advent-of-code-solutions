from collections import defaultdict

# Local
import common
from helpers import fileutils 


def polymer_fragment(mapping:dict, before:str, after:str, depth:int) -> int:
    insertion = common.get_insertion_char(mapping, before, after)

    if depth <= 1:
        #print(f"DEBUG: depth={depth} before={before} after={after} insertion={insertion}")
        return insertion + after
    
    return polymer_fragment(mapping, before, insertion, depth - 1) + polymer_fragment(mapping, insertion, after, depth - 1)


def polymer_transformation(polymer:str, mapping_rules:dict, steps:int) -> str:
    if steps <= 0:
        return polymer

    result = ''

    last = None
    current = None
    for i in range(len(polymer)):
        if None == last:
            last = polymer[0]
            result = last
            continue

        current = polymer[i]
        result += polymer_fragment(mapping_rules, last, current, steps)
        last = current       

    return result


def process_steps(filename, steps:int) -> str:
    initial_polymer_template = fileutils.get_lines_before_empty_from_file(filename)[0]

    map_pair_to_rule = common.get_pair_insertion_rules(filename)
    #print(f"DEBUG: {map_pair_to_rule}")

    polymer = polymer_transformation(initial_polymer_template, map_pair_to_rule, steps)

    #print(f"DEBUG: polymer={polymer}")
    return polymer

def determine_score(filename, steps) -> int:
    polymer = process_steps(filename, steps)

    map_counts = defaultdict(int)
    for ch in polymer:
        map_counts[ch] += 1

    return max(map_counts.values()) - min(map_counts.values())