from helpers import fileutils

def get_pair_insertion_rules(filename):
    lines = fileutils.get_lines_after_empty_from_file(filename)

    map_pair_to_rule = {}
    for l in lines:
        key_value = l.split(" -> ")
        key = key_value[0]
        value = key_value[1]
        map_pair_to_rule[key] = value
    return map_pair_to_rule


def polymer_transformation_step(polymer, mapping_rules):
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

    map_pair_to_rule = get_pair_insertion_rules(filename)
    #print(f"DEBUG: {map_pair_to_rule}")

    polymer = initial_polymer_template
    for step in range(steps):
        polymer = polymer_transformation_step(polymer, map_pair_to_rule)

    #print(f"DEBUG: polymer={polymer}")
    return polymer


def determine_score(filename) -> int:
    polymer = process_steps(filename, 10)



    map_counts = {}
    for ch in polymer:
        if not ch in map_counts:
            map_counts[ch] = 1
        else:
            map_counts[ch] += 1 

    min = None
    max = None

    for value in map_counts.values():
        if min == None or value < min:
            min = value

        if max == None or value > max:
            max = value

    return max - min
