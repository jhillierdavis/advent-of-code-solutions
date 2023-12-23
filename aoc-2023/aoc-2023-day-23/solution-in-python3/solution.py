import sys
from copy import deepcopy
#from collections import defaultdict

from helpers import fileutils, grid, point

sys.setrecursionlimit(5000) # Allow greater recursion depth (than the 1K default)!

"""
def is_valid(g, p, visited, permitted):
    if not p:
        return False
    
    if p in visited:
        return False


    s = g.get_symbol(p)
    if not (s == '.' or s == permitted):
        return False
    
    return True


def hike(g, cp, ep, steps, visited, results):
    if cp == ep:
        print(f"DEBUG: steps={steps}")
        results.add(steps)
        return steps
    
    n = g.get_neighbour_north(cp)
    if is_valid(g, n, visited, '^'):
        v = deepcopy(visited)
        v.add(n)
        hike(g, n, ep, 1 + steps, v, results)


    n = g.get_neighbour_south(cp)
    if is_valid(g, n, visited, 'v'):
        v = deepcopy(visited)
        v.add(n)
        hike(g, n, ep, 1 + steps, v, results)


    n = g.get_neighbour_east(cp)
    if is_valid(g, n, visited, '>'):
        v = deepcopy(visited)
        v.add(n)
        hike(g, n, ep, 1 + steps, v, results)

    n = g.get_neighbour_west(cp)
    if is_valid(g, n, visited, '<'):
        v = deepcopy(visited)
        v.add(n)
        hike(g, n, ep, 1 + steps, v, results)

"""

def is_valid(g, p, lp, permitted):
    if not p:
        return False
    
    if p == lp:
        return False


    s = g.get_symbol(p)
    if not (s == '.' or s == permitted):
        return False
    
    return True


def hike(g, cp, ep, steps, lp, results):
    if cp == ep:
        print(f"DEBUG: steps={steps}")
        results.add(steps)
        return steps
    
    n = g.get_neighbour_north(cp)
    if is_valid(g, n, lp, '^'):
        hike(g, n, ep, 1 + steps, cp, results)


    n = g.get_neighbour_south(cp)
    if is_valid(g, n, lp, 'v'):
        hike(g, n, ep, 1 + steps, cp, results)


    n = g.get_neighbour_east(cp)
    if is_valid(g, n, lp, '>'):
        hike(g, n, ep, 1 + steps, cp, results)

    n = g.get_neighbour_west(cp)
    if is_valid(g, n, lp, '<'):
        hike(g, n, ep, 1 + steps, cp, results)



def get_first_symbol_point_in_row(g, target_symbol, row_index):
    for c in range(g.get_width()):
        p = point.Point2D(c, row_index)
        s = g.get_symbol(p)
        if s == target_symbol:
            return p
    return None

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    grid.display_grid(g)

    sp = get_first_symbol_point_in_row(g, '.', 0)
    ep = get_first_symbol_point_in_row(g, '.', g.get_height() - 1)
    print(f"DEBUG: sp={sp} ep={ep}")

    
    results = set()
    #visited = set()
    #hike(g, sp, ep, 0, visited, results)
    hike(g, sp, ep, 0, sp, results)
    return max(results)

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

