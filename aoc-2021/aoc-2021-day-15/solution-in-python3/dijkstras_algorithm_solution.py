# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

# Local
from helpers import fileutils, grid, point

def create_low_risk_path_grid(chiton_grid):
    start_point = point.Point2D(0, 0)
    stop_point = point.Point2D(chiton_grid.get_width() -1, chiton_grid.get_height() -1)

    pq = [(0, start_point)] # Priority queue list, holding entries with total risk cost per point (x,y)
    #heap = heapq.heapify(pq) # Transform a populated list into a heap 
    visited = set()

    low_risk_path_grid = grid.Grid2D(chiton_grid.get_width(), chiton_grid.get_height())
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
            break

        # Process cardial point (north, south, east, west) immediate neighbours, adding combined risk
        neighbouring_points = chiton_grid.get_cardinal_point_neighbours(p)
        for np in neighbouring_points:
            total_risk_value = int(chiton_grid.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np))

    return low_risk_path_grid


def create_chiton_grid_from_file(filename):
    lines = fileutils.get_file_lines(filename)
    return grid.lines_to_grid(lines)


def get_grid_bottom_right_value(low_risk_path_grid):
    return int(low_risk_path_grid.get_symbol(point.Point2D(low_risk_path_grid.get_width() -1, low_risk_path_grid.get_height() -1)))


def calcuate_lowest_risk_score(filename):
    chiton_grid = create_chiton_grid_from_file(filename)
    
    low_risk_path_grid = create_low_risk_path_grid(chiton_grid)

    grid.display_grid(low_risk_path_grid)

    return get_grid_bottom_right_value(low_risk_path_grid)