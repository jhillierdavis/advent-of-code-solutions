from helpers import fileutils, csvutils


def has_patterns(patterns, design, cache=dict()):
    return count_patterns(patterns, design, cache) > 0

# Check each initial part of the design provided against available patterns, 
# if matched then check the remainder (repeating for all pattern combos)
def count_patterns(patterns, design, cache=dict()):

    # Check if can used cached result (for performance)
    if design in cache:
        return cache[design]

    if not design: # Nothing left to match i.e. len(design) <= 0
        return 1 # At a match

    #print(f"DEBUG: Patterns {patterns} to match")
    count = 0 # No matches
    for p in patterns:
        #print(f"DEBUG: Pattern to match: p={p}")
        if design.startswith(p):
            # Check remainder
            remainder = design[len(p):] # Remaining design without matched pattern
            #print(f"DEBUG: Matched {p} remainder={remainder}")
            count += count_patterns(patterns, remainder, cache)
    
    # Cache the result (the number of times the design matches different combos of patterns)
    cache[design] = count

    return count


def get_input_patterns(filename):   
    lines = fileutils.get_file_lines(filename)
    patterns = csvutils.comma_separated_values_to_list(lines[0])
    return patterns


def get_input_designs(filename):
    designs = fileutils.get_lines_after_empty_from_file(filename)
    return designs


def solve_part1(filename):
    patterns = get_input_patterns(filename)
    designs = get_input_designs(filename)
    #print(f"DEBUG: patterns={patterns}")

    # Cache whether known designs can be constructed from patterns provided
    # NB: Does not need to be reset between designs (as based on patterns which remain the same)
    cache = dict() 

    total_count = 0
    for d in designs:
        if has_patterns(patterns, d, cache):
            total_count += 1
    return total_count


def solve_part2(filename):
    patterns = get_input_patterns(filename)
    designs = get_input_designs(filename)
    #print(f"DEBUG: patterns={patterns}")

    # Cache the number of ways each design can be constructed from patterns provided (0 indicates impossible)
    # NB: Does not need to be reset between designs (as based on patterns which remain the same througout)
    cache = dict() 

    total_count = 0
    for d in designs:        
        total_count += count_patterns(patterns, d, cache)
    return total_count