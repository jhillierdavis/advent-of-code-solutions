from collections import defaultdict

from helpers import fileutils


def get_damaged_contiguous_spring_list_from_condition_record(input):
    values = []
    springs = input + '.' # Add extra char to ease matching

    count_broken = 0
    for i in range(len(springs)):
        char = springs[i]
        if char == '#':
            count_broken += 1
        elif count_broken > 0 :
            values.append(count_broken)
            count_broken = 0
    return values

def replace_str_index(text,index=0,replacement=''):
    #return f'{text[:index]}{replacement}{text[index+1:]}'
    return text[:index].join(replacement).join(text[index+1:])

def replace_next_unknown(input, values):
    index = input.find('?')
    if index < 0:
        values.add(input)
    else:    
        replace_next_unknown(input[:index] + "." + input[index+1:], values)
        replace_next_unknown(input[:index] + "#" + input[index+1:], values)
    


def get_count_of_all_valid_possibilies(condition_record:str, grouping_to_match:[]):
    possibles = set()
    replace_next_unknown(condition_record, possibles)

    count = 0
    for p in possibles:
        damaged = get_damaged_contiguous_spring_list_from_condition_record(p)        
        if damaged == grouping_to_match:
            count += 1
    return count


def get_spring_condition_record(input):
    return input.split()[0]


def get_list_of_contiguous_damaged_spring_groupings(input):
    right = input.split()[1]
    return [int(e) for e in right.split(',')]


def get_chunks(record):
    chunks = []
    s = record + "."
    buf = ""
    for i in range(len(s)):
        char = s[i]
        if char != '.':
            buf += char
        elif buf:
            chunks.append(buf)
            buf = "" # Reset
    return chunks


def get_combo_count_for_chunk_and_hash_pattern(chunk, hash_pattern):
    if not '?' in chunk:
        return 1
        
    return get_count_of_all_valid_possibilies(chunk, hash_pattern)


def count_valid_arrangements_using_cache(input):
    record = get_spring_condition_record(input)
    grouping = get_list_of_contiguous_damaged_spring_groupings(input)

    #print(f"DEBUG: record={record}")
    #print(f"DEBUG: grouping={grouping}")

    return get_valid_combo_count_for_unknowns(record, grouping)


def get_valid_combo_count_for_unknowns(record, grouping, brute_force=False):
    if brute_force:
        ans = get_count_of_all_valid_possibilies(record, grouping)
    else:
        ans = get_valid_permutations(record, grouping)
    return ans


def unfold_record(spring_record):
    # TODO: Is there a better way (without so much duplication)?
    return '?'.join([spring_record,spring_record,spring_record,spring_record,spring_record])


def unfold_grouping(damaged_spring_grouping):
    multiplied = []
    for i in range(5):
        multiplied.extend(damaged_spring_grouping)
    return multiplied


def count_valid_arrangements_using_brute_force(input:str) -> int:
    record = get_spring_condition_record(input)
    grouping = get_list_of_contiguous_damaged_spring_groupings(input)
    return get_count_of_all_valid_possibilies(record, grouping)


def count_valid_arrangements_using_cache(input:str, unfold:bool=False) -> int:
    record = get_spring_condition_record(input)
    grouping = get_list_of_contiguous_damaged_spring_groupings(input)
    if unfold:
        record = unfold_record(record)
        grouping = unfold_grouping(grouping)   

    return get_valid_combo_count_for_unknowns(record, grouping)


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    total = 0
    for l in lines:
        total += count_valid_arrangements_using_brute_force(l)
    return total


def solve_part1_using_cache(filename):
    lines = fileutils.get_file_lines(filename)

    total = 0
    for l in lines:
        total += count_valid_arrangements_using_cache(l)
    return total


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    total = 0
    for l in lines:
        total += count_valid_arrangements_using_cache(l, True) # Unfolding input
    return total


def get_valid_permutations(record:str, grouping:[]):
    #print(f"DEBUG: record={record} grouping={grouping}") 
    cache = {} # Create a new cache, a map of state to number of permutations
    return get_valid_permutations_using_cache(cache, record.rstrip('.'), grouping)


def get_halting_case_value(grouping, gindex, contiguous):
    is_beyond_last_grouping = gindex >= len(grouping)

    if is_beyond_last_grouping:
        return 1 if contiguous == 0 else 0
    
    is_at_last_grouping = gindex == (len(grouping) - 1) 
    is_grouping_value_matched = grouping[gindex] == contiguous       

    if is_at_last_grouping and is_grouping_value_matched:
        return 1         
    return 0    

def get_recursive_case_value(current_char, cache, record, grouping, rindex, gindex, contiguous):
    if current_char == '#':
        return get_valid_permutations_using_cache(cache, record, grouping, rindex, gindex, 1 + contiguous)

    if current_char =='.': # No longer contiguous (if was)       
        if contiguous == 0:
            return get_valid_permutations_using_cache(cache, record, grouping, rindex, gindex, 0)        
        
        is_within_grouping = gindex < len(grouping)
        if is_within_grouping:
            is_matched_grouping = grouping[gindex] == contiguous
            if is_matched_grouping:
                # Move to next grouping (if present)
                return get_valid_permutations_using_cache(cache, record, grouping, rindex, 1+gindex, 0)

    return 0
    

def get_valid_permutations_using_cache(cache:{}, record:str, grouping:[], rindex:int=0, gindex:int=0, contiguous:int=0):   
    state = (rindex, gindex, contiguous)
    
    if state in cache.keys():
        result = cache[state]
        #print(f"DEBUG: From cache state={state} result={result}")
        return result

    # for convenience / readability
    is_record_fully_processed = rindex >= len(record)    

    # Base case - return 1 if a valid permutation (i.e. record matches grouping)
    if is_record_fully_processed: 
        return get_halting_case_value(grouping, gindex, contiguous)
    
    # Non-base case
    current_char = record[rindex]
    
    rindex += 1 # Move to next index
    #print(f"DEBUG: state={state} cache={cache} char={char}")

    result = 0
    if current_char == '?':
        # Count results for each valid option ('#' or '.')
        result += get_recursive_case_value('#', cache, record, grouping, rindex, gindex, contiguous)
        result += get_recursive_case_value('.', cache, record, grouping, rindex, gindex, contiguous)
    else:
        result += get_recursive_case_value(current_char, cache, record, grouping, rindex, gindex, contiguous)

    cache[state] = result
    return result