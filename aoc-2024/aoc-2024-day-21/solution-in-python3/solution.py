import math
from collections import deque

from helpers import fileutils, grid, point

# TODO: Handle '#' sysmbol (non-navigatable)

def find_shortest_lists(list_of_lists):
    if not list_of_lists:
        return []

    # Find the length of the shortest list(s)
    min_length = min(len(lst) for lst in list_of_lists)

    # Collect all lists that have the shortest length
    shortest_lists = [lst for lst in list_of_lists if len(lst) == min_length]
    return shortest_lists


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

    return find_shortest_lists(possibilities)



def find_paths_with_directions(g:grid.Grid2D, start_symbol, end_symbol):
    start = grid.get_single_symbol_point(g, start_symbol)
    end = grid.get_single_symbol_point(g, end_symbol)
    block = grid.get_single_symbol_point(g, '#')
    visited = set()
    visited.add(block)

    def dfs(p, path, directions_path, visited):
        if p == end:
            paths.append((path, directions_path))
            return
        
        visited.add(p)

        #ps = g.get_symbol(p)
        np = g.get_neighbour_north(p)        
        if None != np and np not in visited:        
            new_path = path + [(np.get_x(), np.get_y())]
            dfs(np, new_path, directions_path + ['^'], set(visited))

        np = g.get_neighbour_east(p)
        if None != np and np not in visited:
            new_path = path + [(np.get_x(), np.get_y())]
            dfs(np, new_path, directions_path + ['>'], set(visited))

        np = g.get_neighbour_south(p)
        if None != np and np not in visited:
            new_path = path + [(np.get_x(), np.get_y())]
            dfs(np, new_path, directions_path + ['v'], set(visited))

        np = g.get_neighbour_west(p)
        if None != np and np not in visited:
            new_path = path + [(np.get_x(), np.get_y())]
            dfs(np, new_path, directions_path + ['<'], set(visited))

    paths = []
    dfs(start, [(start.get_x(), start.get_y())], [], visited)
    return paths


#cache = {}
def find_min_directions(g:grid.Grid2D, start_symbol, end_symbol):
    #if (start_symbol, end_symbol) in cache:
    #    return cache[(start_symbol, end_symbol)]

    paths = find_paths_with_directions(g, start_symbol, end_symbol)
    #print(f"DEBUG: paths={paths}")
    min_size = math.inf
    min_directions = None
    for p, d in paths:
        size = len(d)
        if size < min_size:
            min_directions = d        
            min_size = size

    #cache[(start_symbol, end_symbol)] = min_directions

    return min_directions


def find_set_of_min_directions(g:grid.Grid2D, start_symbol, end_symbol):
    paths = find_paths_with_directions(g, start_symbol, end_symbol)
    d = list()
    for p in paths:
        _, directions = p 
        d.append(directions)
    return min(d)


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


def get_shortest_directional_sequence_for_code(code):
    g = create_numerical_keypad_grid()

    start = 'A'
    sequence = ''
    for c in code:
        min_directions = find_min_directions(g, start, c)
#       print(f"DEBUG: start={start} c={c} min_directions={min_directions}")        
        for md in min_directions:
            sequence += md
        sequence += 'A' # Press button
        start = c

    return sequence

def foo(g, start, end, partial_sequences) -> list:
    sequences = []
    possibilities = get_shortest_possibilities(g, start, end)

    
    for p in possibilities:
        for ps in partial_sequences:
            for i in p:
                ps += i
            ps += 'A' # Press button
            sequences.append(ps)            
    return sequences


def get_all_shortest_directional_sequences_for_code(code):
    g = create_numerical_keypad_grid()    
    start = 'A'
    sequences = list()
    sequences.append('')
    for c in code:            
        sequences = foo(g, start, c, sequences)
        start = c        
    return sequences


def get_all_shortest_directional_sequences_for_directions(directions):
    g = create_directional_keypad_grid()    
    start = 'A'
    sequences = list()
    sequences.append('')
    for c in directions:            
        sequences = foo(g, start, c, sequences)
        start = c        
    return sequences


def get_shortest_directional_sequence_for_directions(directions):
    g = create_directional_keypad_grid()
    #print(f"DEBUG: directions={directions}")
    start = 'A'
    sequence = ''
    for end in directions:
        min_directions = find_min_directions(g, start, end)
        
        for md in min_directions:
            sequence += md
        sequence += 'A' # Press button
        #print(f"DEBUG: sequence={sequence} start={start} end={end} min_directions={min_directions}")        
        start = end

    return sequence


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    for code in lines:
        sequences = get_all_shortest_directional_sequences_for_code(code)
        complexity = math.inf
        for s in sequences:
            #directions = get_shortest_directional_sequence_for_directions(s)
            directions = get_all_shortest_directional_sequences_for_directions(s)
            for d in directions:
                value = get_shortest_directional_sequence_for_directions(d)
                s_complexity = calculate_complexity(code, value)
                if complexity > s_complexity:
                    complexity = s_complexity 
                    print(f"DEBUG: code={code} complexity={complexity}")
        ans += complexity
        
    return ans

"""
g = create_numerical_keypad_grid()
grid.display_grid(g)
possibilities = get_shortest_possibilities(g, '2', '9')
print(f"DEBUG: possibilities={possibilities}")   
"""