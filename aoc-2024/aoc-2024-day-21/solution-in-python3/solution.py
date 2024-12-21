import math
from collections import deque

from helpers import fileutils, grid, point

# TODO: Handle '•' sysmbol (non-navigatable)

def find_paths_with_directions(g:grid.Grid2D, start_symbol, end_symbol):
    start = grid.get_single_symbol_point(g, start_symbol)
    end = grid.get_single_symbol_point(g, end_symbol)

    def dfs(p, path, directions_path, visited):
        if p == end:
            paths.append((path, directions_path))
            return
        
        visited.add(p)

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
    dfs(start, [(start.get_x(), start.get_y())], [], set())
    return paths


cache = {}
def find_min_directions(g:grid.Grid2D, start_symbol, end_symbol):
    if (start_symbol, end_symbol) in cache:
        return cache[(start_symbol, end_symbol)]

    paths = find_paths_with_directions(g, start_symbol, end_symbol)
    #print(f"DEBUG: paths={paths}")
    min_size = math.inf
    min_directions = None
    for p, d in paths:
        size = len(d)
        if size < min_size:
            min_directions = d
            min_size = size

    cache[(start_symbol, end_symbol)] = min_directions

    return min_directions


def calculate_complexity(code, sequence):
    return int(code[:-1]) * len(sequence)


def create_directional_keypad_grid():
    g = grid.Grid2D(3,2)
    g.set_symbol(point.Point2D(0,0), '*')
    g.set_symbol(point.Point2D(1,0), '^')
    g.set_symbol(point.Point2D(2,0), 'A')
    g.set_symbol(point.Point2D(0,1), '<')
    g.set_symbol(point.Point2D(1,1), 'v')
    g.set_symbol(point.Point2D(2,1), '>')
    grid.display_grid(g)
    print()
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
    g.set_symbol(point.Point2D(0,3), '*')
    g.set_symbol(point.Point2D(1,3), '0')
    g.set_symbol(point.Point2D(2,3), 'A')

    grid.display_grid(g)
    print()
    return g


def get_shortest_directional_sequence_for_code(code):
    g = create_numerical_keypad_grid()

    start = 'A'
    sequence = ''
    for c in code:
        min_directions = find_min_directions(g, start, c)
#       print(f"DEBUG: c={c} min_directions={min_directions}")        
        for md in min_directions:
            sequence += md
        sequence += 'A'
        start = c

    return sequence

def get_shortest_directional_sequence_for_directions(directions):
    g = create_directional_keypad_grid()

    start = 'A'
    sequence = ''
    for c in directions:
        min_directions = find_min_directions(g, start, c)
#       print(f"DEBUG: c={c} min_directions={min_directions}")        
        for md in min_directions:
            sequence += md
        sequence += 'A'
        start = c
        
    return sequence


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    nkg = create_numerical_keypad_grid()
    dkg = create_directional_keypad_grid()
    return "TODO"