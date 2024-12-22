import math
#from collections import deque

from helpers import fileutils, grid, point, listutils


def get_shortest_possibilities(g:grid.Grid2D, start_symbol, end_symbol):
    start = grid.get_single_symbol_point(g, start_symbol)
    end = grid.get_single_symbol_point(g, end_symbol)
    #block = grid.get_single_symbol_point(g, '#')
    #visited = set()
    #visited.add(block)

    possibilities = []

    def dfs(p, instructions, visited):
        ps = g.get_symbol(p)
        #print(f"DEBUG: p={p} {ps} end={end} {end_symbol} instructions={instructions}")
        if p == end:
            possibilities.append(instructions)
            return
        
        visited.add(p)

        #ps = g.get_symbol(p)
        np = g.get_neighbour_north(p)        
        if None != np and np not in visited:        
            dfs(np, instructions + ['^'], set(visited))

        np = g.get_neighbour_east(p)
        if None != np and np not in visited:
            dfs(np, instructions + ['>'], set(visited))

        np = g.get_neighbour_south(p)
        if None != np and np not in visited:
            dfs(np, instructions + ['v'], set(visited))

        np = g.get_neighbour_west(p)
        if None != np and np not in visited:
            dfs(np, instructions + ['<'], set(visited))

    block = grid.get_single_symbol_point(g, '#')
    initial_visited = set()
    initial_visited.add(block)
    dfs(start, [], initial_visited)

    return listutils.find_shortest_sublists(possibilities)


def calculate_complexity(code, sequence):
    return int(code[:-1]) * len(sequence)


def create_directional_keypad_grid():
    g = grid.Grid2D(3,2)
    g.set_symbol(point.Point2D(0,0), '#')
    g.set_symbol(point.Point2D(1,0), '^')
    g.set_symbol(point.Point2D(2,0), 'A')
    g.set_symbol(point.Point2D(0,1), '<')
    g.set_symbol(point.Point2D(1,1), 'v')
    g.set_symbol(point.Point2D(2,1), '>')
    #grid.display_grid(g)
    #print()
    return g


def create_numerical_keypad_grid():
    g = grid.Grid2D(3,4)
    g.set_symbol(point.Point2D(0,0), '7')
    g.set_symbol(point.Point2D(1,0), '8')
    g.set_symbol(point.Point2D(2,0), '9')
    g.set_symbol(point.Point2D(0,1), '4')
    g.set_symbol(point.Point2D(1,1), '5')
    g.set_symbol(point.Point2D(2,1), '6')
    g.set_symbol(point.Point2D(0,2), '1')
    g.set_symbol(point.Point2D(1,2), '2')
    g.set_symbol(point.Point2D(2,2), '3')
    g.set_symbol(point.Point2D(0,3), '#')
    g.set_symbol(point.Point2D(1,3), '0')
    g.set_symbol(point.Point2D(2,3), 'A')

    #grid.display_grid(g)
    #print()
    return g


def get_sequence_for_shortest_possibilities(g, start, end, partial_sequences) -> list:
    sequences = []
    possibilities = get_shortest_possibilities(g, start, end)
    
    for p in possibilities:
        for ps in partial_sequences:
            for i in p:
                ps += i
            ps += 'A' # Press button
            sequences.append(ps)            
    return sequences


def get_all_shortest_directional_sequences_for_code(g_numpad, code):
    start = 'A'
    sequences = list()
    sequences.append('')
    for c in code:            
        sequences = get_sequence_for_shortest_possibilities(g_numpad, start, c, sequences)
        start = c        
    return sequences


def get_all_shortest_directional_sequences_for_directions(g_dirpad, directions):
    start = 'A'
    sequences = list()
    sequences.append('')
    for c in directions:            
        sequences = get_sequence_for_shortest_possibilities(g_dirpad, start, c, sequences)
        start = c        
    return sequences


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    g_numpad = create_numerical_keypad_grid()
    g_dirpad = create_directional_keypad_grid()
    
    ans = 0
    for code in lines:
        sequences = get_all_shortest_directional_sequences_for_code(g_numpad, code)
        complexity = math.inf
        for s in sequences:
            #directions = get_shortest_directional_sequence_for_directions(s)            
            directions = get_all_shortest_directional_sequences_for_directions(g_dirpad, s)
            for d in directions:
                next_directions = get_all_shortest_directional_sequences_for_directions(g_dirpad, d)
                for nd in next_directions:
                    s_complexity = calculate_complexity(code, nd)
                    if complexity > s_complexity:
                        complexity = s_complexity 
        ans += complexity

    return ans