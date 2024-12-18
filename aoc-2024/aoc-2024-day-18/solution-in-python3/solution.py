# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import fileutils, grid, point

CORRUPTION_BLOCK_CHAR = '#'


def get_least_steps(g:grid.Grid2D, block_char:str="#", start_point:point.Point2D = point.Point2D(0, 0), stop_point:point.Point2D = None):
    if stop_point == None:
        stop_point = point.Point2D(g.get_width() -1, g.get_height() -1)

    pq = [(0, start_point)] # Priority queue list, holding entries with total risk cost per point (x,y)
    #heap = heapq.heapify(pq) # Transform a populated list into a heap 
    visited = set()

    low_risk_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    low_risk_path_grid.set_symbol(start_point, 0)

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y)
        c, p = heapq.heappop(pq)        

        # Avoid revisits
        if p in visited:
            continue # Ignore already visitied points (x,y) on grid
        visited.add(p)

        # Track total risk score on (another same size) grid
        low_risk_path_grid.set_symbol(p, c)

        # Stop when reach target destination point
        if p == stop_point:
            return c
            #break

        # Process cardial point (north, south, east, west) immediate neighbours, adding combined risk
        neighbouring_points = g.get_cardinal_point_neighbours(p)
        for np in neighbouring_points:
            ns = g.get_symbol(np)
            if ns == '.':
                heapq.heappush(pq, (c + 1, np))

    return -1


def get_corruption_blocks(lines):
    cbps = [] # Corruption block points
    for l in lines:
        values = l.split(",")
        x = int(values[0])
        y = int(values[1])
        p = point.Point2D(x,y)
        cbps.append(p)
    return cbps


def place_corruption_blocks(g:grid.Grid2D, cbps, count):
    for i in range(count):
        p = cbps[i]
        g.set_symbol(p, CORRUPTION_BLOCK_CHAR) # Blocked


def solve_part1(filename:str, size:int, fallen:int) -> int:
    lines = fileutils.get_file_lines_from(filename)
    cbps = get_corruption_blocks(lines)

    g = grid.Grid2D(size, size)

    place_corruption_blocks(g, cbps, fallen)
    
    #grid.display_grid(g)

    return get_least_steps(g)


def get_block_point(g:grid.Grid2D, cbps:[point.Point2D], reachable:int=0) -> (int,int):
    size = len(cbps)
    for i in range(reachable, size):
        p = cbps[i]

        g.set_symbol(p, CORRUPTION_BLOCK_CHAR) # Blocked
            
        if get_least_steps(g) < 0:
            return (p.get_x(), p.get_y())

    return (-1,-1) # Failed

"""
def get_block_point_optimised(g, cps):
    size = len(cps)
    max_x = 0
    max_y = 0
    for i in range(size):
        p = cps[i]
        if max_x < p.get_x():
            max_x = p.get_x()
            if max_x < g.get_width() -1:
                max_x += 1
        if max_y < p.get_y():
            max_y = p.get_y()
            if max_y < g.get_height() -1:
                max_y += 1

        g.set_symbol(p, '#') # Blocked
            
        # Try to use next point, as stop point, from furthest curruption point to optimise
        if get_least_steps(g, CORRUPTION_BLOCK_CHAR, point.Point2D(0,0), point.Point2D(max_x, max_y)) < 0:
            return (p.get_x(), p.get_y())

    return (-1,-1)
"""

def solve_part2(filename:str, size:int, reachable:int) -> (int,int):
    lines = fileutils.get_file_lines_from(filename)
    cbps = get_corruption_blocks(lines)

    g = grid.Grid2D(size, size)
    place_corruption_blocks(g, cbps, reachable)

    return get_block_point(g, cbps, reachable)
    #return get_block_point(g, cps, 0)