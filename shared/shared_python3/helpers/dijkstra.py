# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import grid, point


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
