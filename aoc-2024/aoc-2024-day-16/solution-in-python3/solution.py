# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html
#
# See AOC 2021 Day 15 for another Dijkstra example.

import heapq

# Local
from helpers import fileutils, grid, point


def get_single_symbol_point(g:grid.Grid2D, symbol) -> point.Point2D:
    points = g.get_points_matching(symbol)
    assert len(points) == 1
    sp = points.pop()
    #print(f"DEBUG: Start point: sp={sp}")
    return sp


def calculate_change_in_direction_cost(current_direction:int, new_direction:int):
    if current_direction == new_direction:
        return 0
    
    if current_direction == 1:
        if new_direction == 3:
            return 2000

    if current_direction == 3:
        if new_direction == 1:
            return 2000
    
    if current_direction == 4:
        if new_direction == 2:
            return 2000

    if current_direction == 2:
        if new_direction == 4:
            return 2000
        
    return 1000


def create_low_cost_path_grid(g:grid.Grid2D):
    start_point = get_single_symbol_point(g, 'S')
    stop_point = get_single_symbol_point(g, 'E')

    direction = 2 # grid.Compass.EAST # direction
    pq = [(0, (start_point, direction))] # Priority queue list, holding entries with total cost per point (x,y)
    #heap = heapq.heapify(pq) # Transform a populated list into a heap
    visited = set()

    low_cost_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    low_cost_path_grid.set_symbol(start_point, 0)
    

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y) and direction
        c, (p, d) = heapq.heappop(pq)

        # Avoid revisits
        if (p,d) in visited:
            continue # Ignore already visitied points (x,y) on grid
        visited.add((p,d))

        # Track total risk score on (another same size) grid
        low_cost_path_grid.set_symbol(p, c)

        # Stop when reach target destination point
        if p == stop_point:
            #print(f"DEBUG: Bingo!")
            break

        # Process cardial point (north, south, east, west) immediate neighbours, adding costs

        np = g.get_neighbour_north(p)
        if np:
            additional_cost = calculate_change_in_direction_cost(d, 1)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 1)))

        np = g.get_neighbour_east(p)
        if np:
            additional_cost = calculate_change_in_direction_cost(d, 2)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 2)))

        np = g.get_neighbour_south(p)
        if np:
            additional_cost = calculate_change_in_direction_cost(d, 3)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 3)))

        np = g.get_neighbour_west(p)
        if np:
            additional_cost = calculate_change_in_direction_cost(d, 4)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 4)))

    return low_cost_path_grid


def create_chiton_grid_from_file(filename):
    lines = fileutils.get_file_lines(filename)
    return grid.lines_to_integer_grid(lines)


def get_grid_bottom_right_value(low_risk_path_grid):
    return int(low_risk_path_grid.get_symbol(point.Point2D(low_risk_path_grid.get_width() -1, low_risk_path_grid.get_height() -1)))


def calcuate_lowest_risk_score(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    stop_point = get_single_symbol_point(g, 'E')

    low_cost_path_grid = create_low_cost_path_grid(g)

    #grid.display_grid(low_cost_path_grid, " ")

    return low_cost_path_grid.get_symbol(stop_point)


def solve_part1(filename):
    return calcuate_lowest_risk_score(filename)