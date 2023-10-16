from collections import defaultdict

# Local
from helpers import fileutils
import common


def polymer_transformation_step(polymer:str, mapping_rules:dict) -> str:
    result = ''

    last = None
    current = None
    for i in range(len(polymer)):
        if None == last:
            last = polymer[0]
            result = last
            continue

        current = polymer[i]
        insert = mapping_rules[last + current]
        #print(f"DEBUG: i={i} last={last} insert={insert} current={current}")
        result += insert + current

        last = current       

    return result


def process_steps(filename:str, steps:int) -> str:
    initial_polymer_template = fileutils.get_lines_before_empty_from_file(filename)[0]

    map_pair_to_rule = common.get_pair_insertion_rules(filename)
    #print(f"DEBUG: {map_pair_to_rule}")

    polymer = initial_polymer_template
    for _ in range(steps):
        polymer = polymer_transformation_step(polymer, map_pair_to_rule)

    #print(f"DEBUG: polymer={polymer}")
    return polymer



def determine_score(filename, steps) -> int:
    polymer = process_steps(filename, steps)

    map_counts = defaultdict(int)
    for ch in polymer:
        map_counts[ch] += 1

    return max(map_counts.values()) - min(map_counts.values())