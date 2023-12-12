from collections import defaultdict

from helpers import fileutils


def list_broken_springs(input):
    values = []
    springs = input + '|'

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


def count_valid_arrangements(input):
    (v,g) = input.split()
    #print(f"DEBUG: v={v}")
    #print(f"DEBUG: g={g}")

    possibles = set()
    replace_next_unknown(v, possibles)

    count = 0
    for p in possibles:
        lb = list_broken_springs(p)
        lg = [int(e) for e in g.split(',')]
        #print(f"DEBUG: p={p} lb={lb} lg={lg}")
        if list_broken_springs(p) == lg:
            count += 1

    return count


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    total = 0

    for l in lines:
        total += count_valid_arrangements(l)
    return total
