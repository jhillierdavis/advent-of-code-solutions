import math
#from collections import deque

from helpers import fileutils

import solution


def solve_part2(filename, intermediaries):
    lines = fileutils.get_file_lines_from(filename)

    g_numpad = solution.create_numerical_keypad_grid()
    g_dirpad = solution.create_directional_keypad_grid()
    
    ans = 0
    for code in lines:
        sequences = solution.get_all_shortest_directional_sequences_for_code(g_numpad, code)
        ans += solution.get_min_directional_complexity_for_intermediaries(g_dirpad, code, sequences, intermediaries, math.inf)
    return ans