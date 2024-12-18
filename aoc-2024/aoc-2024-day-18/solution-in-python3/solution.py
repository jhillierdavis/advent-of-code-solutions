# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import fileutils, grid, point


def create_low_risk_path_grid(g):
    start_point = point.Point2D(0, 0)
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


def get_corruption_points(lines):
    cps = [] # Corruption points
    for l in lines:
        values = l.split(",")
        x = int(values[0])
        y = int(values[1])
        p = point.Point2D(x,y)
        cps.append(p)
    return cps


def solve_part1(filename, fallen, size):
    lines = fileutils.get_file_lines_from(filename)
    cps = get_corruption_points(lines)

    g = grid.Grid2D(size, size)

    for i in range(fallen):
        p = cps[i]
        g.set_symbol(p, '#')
    
    #grid.display_grid(g)

    return create_low_risk_path_grid(g)


def solve_part2(filename, size):
    lines = fileutils.get_file_lines_from(filename)
    cps = get_corruption_points(lines)

    g = grid.Grid2D(size, size)

    size = len(cps)
    for i in range(size):
        p = cps[i]
        g.set_symbol(p, '#')
        if create_low_risk_path_grid(g) < 0:
            return (p.get_x(), p.get_y())

    return (-1,-1)