from collections import defaultdict, Counter

# Local
import common
from helpers import fileutils 


def polymer_fragment_counter(mapping:dict, before:str, after:str, depth:int, cache:dict) -> Counter:
    # Lookup in cache (& return if present)
    key = before + after + str(depth) # Cache key
    if  key in cache:
        return cache[key]


    counter = Counter() # Use Python3's counter (dictionary subclass)
    insertion = common.get_insertion_char(mapping, before, after)

    if depth <= 1:
        #print(f"DEBUG: depth={depth} before={before} after={after} insertion={insertion}")
        counter.update(insertion + after)        
    else:
        c1 = polymer_fragment_counter(mapping, before, insertion, depth - 1, cache)
        c2 = polymer_fragment_counter(mapping, insertion, after, depth - 1, cache)
        counter = c1 + c2


    cache[key] = counter
    return counter


def polymer_transformation_counter(polymer:str, mapping_rules:dict, steps:int) -> Counter:
    if steps <= 0:
        return polymer

    cache = defaultdict(int) # Use a dictorary as a cache for performance
    counter = Counter() # Count letter occurances

    last = None
    current = None
    for i in range(len(polymer)):
        if None == last:
            last = polymer[0]     
            counter[last] = 1       
            continue

        current = polymer[i]
        fragment_counter = polymer_fragment_counter(mapping_rules, last, current, steps, cache)
        counter += fragment_counter

        last = current       

    return counter



def determine_score(filename:str, steps:int) -> int:
    initial_polymer_template = fileutils.get_lines_before_empty_from_file(filename)[0]

    map_pair_to_insertion_rules = common.get_pair_insertion_rules(filename)

    counter = polymer_transformation_counter(initial_polymer_template, map_pair_to_insertion_rules, steps)

    return max(counter.values()) - min(counter.values())