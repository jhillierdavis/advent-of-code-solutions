from collections import defaultdict

# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html

import heapq

from helpers import fileutils, grid, point

def is_valid_point(p:point.Point2D, stop_point:point.Point2D, min_consecutive:int=0) -> bool:
    if not p:
        return False
    
    if min_consecutive == 0:
        return True
    
    if p == stop_point:
        return True
    
    if stop_point.get_x() - p.get_x() < min_consecutive and stop_point.get_y() - p.get_y() < min_consecutive:
        return p.get_y() == stop_point.get_y() or p.get_x() == stop_point.get_x()

    return True

    

def create_low_risk_path_grid(g:grid.Grid2D, min_consecutive:int=0, max_consecutive:int=3):
    start_point = point.Point2D(0, 0)
    stop_point = point.Point2D(g.get_width() -1, g.get_height() -1)

    pq = [(0, start_point, '?', 0)] # Priority queue list, holding entries with total risk cost per point (x,y), current position, direction, direction count
    #heap = heapq.heapify(pq) # Transform a populated list into a heap 
    visited = set()

    low_risk_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    #low_risk_path_grid.set_symbol(start_point, 0)    

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y)
        c, p, direction, direction_count = heapq.heappop(pq)        

        # Avoid revisits
        state = (p,direction, direction_count)
        if state in visited:
            continue # Ignore prior state
        visited.add(state)

        # Track total risk score on (another same size) grid
        low_risk_path_grid.set_symbol(p, c)
        #low_risk_path_grid.set_symbol(p, direction)

        # Stop when reach target destination point
        if p == stop_point:
            #s = g.get_symbol(p)
            #print(f"DEBUG: Reached stop point c={c} s={s}")
            break

        # Process cardial point (north, south, east, west) immediate neighbours, adding combined risk
        np = g.get_neighbour_east(p)
        if is_valid_point(np, stop_point, min_consecutive) and direction != '<':
            if direction == '?' or (direction in '^v' and direction_count >= min_consecutive) or (direction == '>' and direction_count < max_consecutive):
                value = int(g.get_symbol(np))
                heapq.heappush(pq, (c + value, np, '>', 1 + direction_count if direction == '>' else 1))

        np = g.get_neighbour_west(p)
        if is_valid_point(np, stop_point, min_consecutive) and direction != '>':
            if direction == '?' or (direction in '^v' and direction_count >= min_consecutive) or (direction == '<' and direction_count < max_consecutive):
                value = int(g.get_symbol(np))
                heapq.heappush(pq, (c + value, np, '<', 1 + direction_count if direction == '<' else 1))

        np = g.get_neighbour_north(p)
        if is_valid_point(np, stop_point, min_consecutive) and direction != 'v':
            if direction == '?' or (direction in '<>' and direction_count >= min_consecutive) or (direction == '^' and direction_count < max_consecutive):
                value = int(g.get_symbol(np))
                heapq.heappush(pq, (c + value, np, '^', 1 + direction_count if direction == '^' else 1))

        np = g.get_neighbour_south(p)
        if is_valid_point(np, stop_point, min_consecutive) and direction != '^':
            if direction == '?' or (direction in '<>' and direction_count >= min_consecutive) or (direction == 'v' and direction_count < max_consecutive):
                value = int(g.get_symbol(np))
                heapq.heappush(pq, (c + value, np, 'v', 1 + direction_count if direction == 'v' else 1))            

    return low_risk_path_grid


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    pg = create_low_risk_path_grid(g)
    #grid.display_grid(pg, " ")
    return int(pg.get_symbol(point.Point2D(pg.get_width()-1, pg.get_height()-1)))

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    pg = create_low_risk_path_grid(g, 4, 10)
    ##grid.display_grid(pg, " ")
    return int(pg.get_symbol(point.Point2D(pg.get_width()-1, pg.get_height()-1)))

