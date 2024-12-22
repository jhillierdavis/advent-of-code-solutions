import math
#from collections import deque

from helpers import fileutils

import solution

"""
def get_min_directional_complexity(g_dirpad, code, sequences, depth):
    for s in sequences:
        directions = solution.get_all_shortest_directional_sequences_for_directions(g_dirpad, s)

        if depth <= 0:
            complexity = math.inf
            for d in directions:
                current_complexity = solution.calculate_complexity(code, d)
                if complexity > current_complexity:
                    complexity = current_complexity 
            return complexity
        
        return get_min_directional_complexity(g_dirpad, code, directions, complexity, depth - 1)
"""       

def get_min_directional_complexity(g_dirpad, code, sequences, intermediaries):        
    complexity = math.inf
    for s in sequences:
        directions = solution.get_all_shortest_directional_sequences_for_directions(g_dirpad, s)
        for d in directions:
            next_directions = solution.get_all_shortest_directional_sequences_for_directions(g_dirpad, d)
            for nd in next_directions:
                s_complexity = solution.calculate_complexity(code, nd)
                if complexity > s_complexity:
                    complexity = s_complexity 
    return complexity


def solve_part2(filename, intermediaries):
    lines = fileutils.get_file_lines_from(filename)

    g_numpad = solution.create_numerical_keypad_grid()
    g_dirpad = solution.create_directional_keypad_grid()
    
    ans = 0
    for code in lines:
        sequences = solution.get_all_shortest_directional_sequences_for_code(g_numpad, code)
        ans += get_min_directional_complexity(g_dirpad, code, sequences, intermediaries)
    return ans