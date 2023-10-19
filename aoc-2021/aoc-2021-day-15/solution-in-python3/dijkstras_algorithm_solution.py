# TODO
# Ref.s:
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 

# Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import fileutils, grid, point

def create_low_risk_path_grid(chiton_grid):

    pq = [(0, 0, 0)] # Priority queue list, holding entries with total risk cost per point (x,y)
    heapq.heapify(pq)
    visited = set()

    low_risk_path_grid = grid.Grid2D(chiton_grid.get_width(), chiton_grid.get_height())
    low_risk_path_grid.set_symbol(point.Point2D(0,0), 0)

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y)
        c, x, y = heapq.heappop(pq)
        p = point.Point2D(x,y)

        # Avoid revisits
        if p in visited:
            continue # Ignore already visitied points (x,y) on grid
        visited.add(p)

        low_risk_path_grid.set_symbol(p, c)

        # Stop when reach target destination point
        if p.get_x() == chiton_grid.get_width() -1 and p.get_y() == chiton_grid.get_height() -1:
            break

        neighbouring_points = chiton_grid.get_cardinal_point_neighbours(p)
        for np in neighbouring_points:
            total_risk_value = int(chiton_grid.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np.get_x(), np.get_y()))

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