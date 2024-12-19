#from functools import cache

from helpers import fileutils


def is_possible_design(towel_pattern, design) -> bool:
    patterns = towel_pattern.split(", ")
    patterns = sorted(patterns, key=len, reverse=True)
    #print(f"DEBUG: {patterns}")

    has_patterns = False
    
    s = design
    size = len(design)
    for i in range(size):
        for p in patterns:
            if s.startswith(p):                
                s = s[len(p):]
                #print(f"DEBUG: {s}")
                continue

    has_patterns = len(s) <= 0
    return has_patterns



#@cache # Will not work with list!
def has_patterns(patterns, design, cache=dict()):
    if design in cache:
        return cache[design]

    """
    if len(design) <= 0:
        print(f"Matched design={design}")
        return True    
    """
    if not design: # Nothing left to match
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

    patterns = lines[0].split(', ')
    designs = fileutils.get_lines_after_empty_from_file(filename)
    print(patterns)

    ans = 0
    for d in designs:
        cache = dict() # Cache whether known designs can be constructed from patterns provided
        if has_patterns(patterns, d, cache):
            ans += 1
    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    patterns = lines[0].split(', ')
    designs = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: patterns={patterns}")

    ans = 0
    for d in designs:
        cache = dict() # Cache the number of ways each design can be constructed from patterns provided (0 is impossible)
        ans += count_patterns(patterns, d, cache)
    return ans