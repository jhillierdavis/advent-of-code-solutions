import math

from helpers import fileutils

import solution


g_numpad = solution.create_numerical_keypad_grid()
g_dirpad = solution.create_directional_keypad_grid()


def get_shortest_dirpad_sequences(start, end) -> list:
    sequences = []
    possibilities = solution.get_shortest_possibilities(g_dirpad, start, end)
    
    for p in possibilities:
        ps = ''
        for i in p:
            ps += i
        ps += 'A' # Press button
        sequences.append(ps)            
    return sequences


directional_symbols = ['A', '^', 'v', '<', '>']
dir_pad_paths = {(s1, s2): get_shortest_dirpad_sequences(s1, s2) for s1 in directional_symbols for s2 in directional_symbols}


cache_moves = dict()
def get_min_moves(directions, robots):
    if (directions, robots) in cache_moves:
        return cache_moves[(directions, robots)]

    if robots == 0:
        return len(directions)
    min_moves = 0
    for p1, p2 in zip("A" + directions, directions):
        min_moves += min(get_min_moves(seq, robots - 1) for seq in dir_pad_paths[(p1, p2)])

    cache_moves[(directions, robots)] = min_moves
    return min_moves



def get_min_directional_moves(directions, robots):    
    sequences = solution.get_all_shortest_directional_sequences_for_directions(g_dirpad, directions)

    #print(f"DEBUG: directions={directions} sequences={sequences} robots={robots}")
    min_moves = math.inf    
    if robots <= 0:
        min_moves = len(directions)
    else:
        for s in sequences:
            min_moves = min(min_moves, get_min_moves(s, robots-1))
    return min_moves


def calculate_min_moves_for_code(code, robots):
    min_moves = math.inf
    sequences = solution.get_all_shortest_directional_sequences_for_code(g_numpad, code)
    for s in sequences:
        min_moves = min(min_moves, get_min_directional_moves(s, robots-1))
    return min_moves


def solve_part2(filename, robots):
    lines = fileutils.get_file_lines_from(filename)

    ans = 0    
    for code in lines:
        min_moves = calculate_min_moves_for_code(code, robots)
        complexity = int(code[:-1]) * min_moves
        #print(f"DEBUG: code={code} robots={robots} min_moves={min_moves} complexity={complexity}")
        ans += complexity
    return ans