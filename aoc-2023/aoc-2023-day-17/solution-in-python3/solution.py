from collections import defaultdict

# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import fileutils, grid, point

def create_low_risk_path_grid(g:grid.Grid2D):
    start_point = point.Point2D(0, 0)
    direction:chr = '>'
    direction_count:0 = 0    
    stop_point = point.Point2D(g.get_width() -1, g.get_height() -1)

    pq = [(0, start_point, direction, direction_count)] # Priority queue list, holding entries with total risk cost per point (x,y)
    #heap = heapq.heapify(pq) # Transform a populated list into a heap 
    visited = set()

    low_risk_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    #low_risk_path_grid.set_symbol(start_point, 0)

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y)
        c, p, direction, direction_count = heapq.heappop(pq)        

        # Avoid revisits
        if p in visited:
            continue # Ignore already visitied points (x,y) on grid
        visited.add(p)

        # Track total risk score on (another same size) grid
        low_risk_path_grid.set_symbol(p, c)
        #low_risk_path_grid.set_symbol(p, direction)

        # Stop when reach target destination point
        if p == stop_point:
            s = g.get_symbol(p)
            print(f"DEBUG: Reached stop point c={c} s={s}")
            break

        # Process cardial point (north, south, east, west) immediate neighbours, adding combined risk
        """
        neighbouring_points = g.get_cardinal_point_neighbours(p)
        for np in neighbouring_points:
            total_risk_value = int(g.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np))
        """

        np = g.get_neighbour_east(p)
        if np and direction != '<' and not (direction_count > 2 and direction == '>'):
            total_risk_value = int(g.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np, '>', 1 + direction_count if direction == '>' else 0))

        np = g.get_neighbour_west(p)
        if np and direction != '>' and not (direction_count > 2 and direction == '<'):
            total_risk_value = int(g.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np, '<', 1 + direction_count if direction == '<' else 0))

        np = g.get_neighbour_north(p)
        if np and direction != 'v' and not (direction_count > 2 and direction == '^'):
            total_risk_value = int(g.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np, '^', 1 + direction_count if direction == '^' else 0))

        np = g.get_neighbour_south(p)
        if np and direction != '^' and not (direction_count > 2 and direction == 'v') :
            total_risk_value = int(g.get_symbol(np)) + c
            heapq.heappush(pq, (total_risk_value, np, 'v', 1 + direction_count if direction == 'v' else 0))            

    return low_risk_path_grid


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    grid.display_grid(g)

    pg = create_low_risk_path_grid(g)
    grid.display_grid(pg, " ")
    return int(pg.get_symbol(point.Point2D(pg.get_width()-1, pg.get_height()-1)))

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

