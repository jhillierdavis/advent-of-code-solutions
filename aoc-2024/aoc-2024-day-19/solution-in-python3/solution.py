#from functools import cache

from helpers import fileutils


def comma_separated_values_to_list(csvs:str) -> list:
    return [value.strip() for value in csvs.split(',')]


#@cache # Will not work with list!
def has_patterns(patterns, design, cache=dict()):
    #print(f"DEBUG: has_patterns {patterns} design={design} cache={cache}")

    if design in cache: 
        print(f"DEBUG: Cache: {design} {cache[design]}")
        return cache[design]

    if not design: # Nothing left to match i.e. len(design) <= 0
        #print(f"DEBUG: Cache: {design}")
        return True

    #print(f"DEBUG: Patterns {patterns}")
    found = False
    for p in patterns:
        #print(f"DEBUG: p={p}")
        if design.startswith(p):
            remainder = design[len(p):]
            # Check remainder
            #print(f"DEBUG: Matched {p} remainder={remainder}")
            if has_patterns(patterns, remainder, cache):
                found = True
                break
    cache[design] = found
    return found


def count_patterns(patterns, design, cache):
    if design in cache:
        return cache[design]

    if not design: # Nothing left to match
        return 1

    #print(f"DEBUG: Patterns {patterns}")
    count = 0
    for p in patterns:
        #print(f"DEBUG: p={p}")
        if design.startswith(p):
            remainder = design[len(p):]
            # Check remainder
            #print(f"DEBUG: Matched {p} remainder={remainder}")
            count += count_patterns(patterns, remainder, cache)
    cache[design] = count
    return count

    

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    patterns = comma_separated_values_to_list(lines[0])
    designs = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: patterns={patterns}")

    ans = 0
    for d in designs:
        cache = dict() # Cache whether known designs can be constructed from patterns provided
        if has_patterns(patterns, d, cache):
            ans += 1
    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    patterns = comma_separated_values_to_list(lines[0])
    designs = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: patterns={patterns}")

    ans = 0
    for d in designs:
        cache = dict() # Cache the number of ways each design can be constructed from patterns provided (0 is impossible)
        ans += count_patterns(patterns, d, cache)
    return ans