from collections import defaultdict

from helpers import fileutils


def list_broken_springs(input):
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
    
#values=set()
#replace_next_unknown('.?.#?', values)
#print(f"DEBUG: {values}")


def count_valid_arrangements_using_brute_force(input):
    v = get_gear_sequence(input)
    lg = get_broken_gear_groupings(input)
    print(f"DEBUG: v={v}")
    print(f"DEBUG: lg={lg}")

    possibles = set()
    replace_next_unknown(v, possibles)

    count = 0
    for p in possibles:
        lb = list_broken_springs(p)        
        #print(f"DEBUG: p={p} lb={lb} lg={lg}")
        if lb == lg:
            count += 1

    return count

def unfold(input,times):
    return input * times

def get_count_of_all_valid_possibilies(chunk:str, grouping_to_match:[]):
    possibles = set()
    replace_next_unknown(chunk, possibles)

    count = 0
    for p in possibles:
        lb = list_broken_springs(p)        
        if lb == grouping_to_match:
            count += 1

    return count


def get_gear_sequence(input):
    return input.split()[0]

def get_broken_gear_groupings(input):
    right = input.split()[1]
    bgg = [int(e) for e in right.split(',')]
    return bgg


def count_valid_arrangements_with_unfolding(input):
    v = get_gear_sequence(input)
    lg = get_broken_gear_groupings(input)
    print(f"DEBUG: v={v}")
    print(f"DEBUG: lg={lg}")

    unfolded_v = v + '?' + v + '?' + v + '?' + v + '?' + v
    print(f"DEBUG: unfolded_v={unfolded_v}")

    unfolded_g = g + ',' + g + ',' + g + ',' + g + ',' + g
    print(f"DEBUG: unfolded_g={unfolded_g}")


    possibles = set()
    replace_next_unknown(unfolded_v, possibles)

    count = 0
    for p in possibles:
        lb = list_broken_springs(p)
        
        #print(f"DEBUG: p={p} lb={lb} lg={lg}")
        if lb == lg:
            count += 1

    return count


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    total = 0

    for l in lines:
        total += count_valid_arrangements_using_brute_force(l)
    return total

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

def count_valid_arrangements_using_caching(input):
    (v,g) = input.split()
    lg = [int(e) for e in g.split(',')]
    print(f"DEBUG: v={v}")
    print(f"DEBUG: lg={lg} g={g}")

    chunks = get_chunks(v)
    print(f"DEBUG: chunks={chunks}")

    """
    possibles = set()
    replace_next_unknown(v, possibles)

    count = 0
    for p in possibles:
        lb = list_broken_springs(p)        
        #print(f"DEBUG: p={p} lb={lb} lg={lg}")
        if lb == lg:
            count += 1
    """
    return 0


def get_combo_count_for_chunk_and_hash_pattern(chunk, hash_pattern):
    if not '?' in chunk:
        raise ValueError("No '?' in chunk={chunk} !")
    
    
    return get_count_of_all_valid_possibilies(chunk, hash_pattern)