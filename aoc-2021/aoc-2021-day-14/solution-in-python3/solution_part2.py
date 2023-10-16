from collections import defaultdict

# Local
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

def get_insertion_char(mapping, before, after):
    return mapping[before + after]

def polymer_fragment(mapping, before, after, depth):
    insertion = get_insertion_char(mapping, before, after)

    if depth <= 1:
        #print(f"DEBUG: depth={depth} before={before} after={after} insertion={insertion}")
        return insertion + after
    
    
    return polymer_fragment(mapping, before, insertion, depth - 1) + polymer_fragment(mapping, insertion, after, depth - 1)


def polymer_transformation(polymer, mapping_rules, steps):
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

    map_pair_to_rule = get_pair_insertion_rules(filename)
    #print(f"DEBUG: {map_pair_to_rule}")

    polymer = polymer_transformation(initial_polymer_template, map_pair_to_rule, steps)

    #print(f"DEBUG: polymer={polymer}")
    return polymer



def update_map_of_counts(dict_to_update, dict_to_use):
    for k in dict_to_use.keys():
        dict_to_update[k] += dict_to_use[k]
    return dict_to_update


def polymer_fragment_counter(mapping, before, after, depth, cache):
    key = before + after + str(depth)
    if  key in cache:
        return cache[key]


    map_counter = defaultdict(int)
    insertion = get_insertion_char(mapping, before, after)

    if depth <= 1:
        #print(f"DEBUG: depth={depth} before={before} after={after} insertion={insertion}")
        
        map_counter[insertion] += 1
        map_counter[after] += 1
        
    else:

        mc1 = polymer_fragment_counter(mapping, before, insertion, depth - 1, cache)
        update_map_of_counts(map_counter, mc1)

        mc2 = polymer_fragment_counter(mapping, insertion, after, depth - 1, cache)
        update_map_of_counts(map_counter, mc2)


    cache[key] = map_counter
    return map_counter


    



def polymer_transformation_counter(polymer, mapping_rules, steps):
    if steps <= 0:
        return polymer

    cache = defaultdict(int)
    map_counter = defaultdict(int)

    last = None
    current = None
    for i in range(len(polymer)):
        if None == last:
            last = polymer[0]            
            continue

        current = polymer[i]
        map_fragment_counter = polymer_fragment_counter(mapping_rules, last, current, steps, cache)
        update_map_of_counts(map_counter, map_fragment_counter)

        last = current       

    return map_counter



def determine_score(filename, steps) -> int:
    initial_polymer_template = fileutils.get_lines_before_empty_from_file(filename)[0]

    map_pair_to_rule = get_pair_insertion_rules(filename)

    map_counts = polymer_transformation_counter(initial_polymer_template, map_pair_to_rule, steps)

    min = None
    max = None

    for value in map_counts.values():
        if min == None or value < min:
            min = value

        if max == None or value > max:
            max = value

    return max - min
