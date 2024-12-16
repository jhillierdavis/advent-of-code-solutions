# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html
#
# See also AOC 2021 Day 15 for a prior Dijkstra example (which used as basis).

import heapq

# Local helper utils
from helpers import fileutils, grid, point


def calculate_change_in_direction_cost(current_direction:int, new_direction:int):
    if current_direction == new_direction:
        return 0
    
    if current_direction == int(grid.Compass.NORTH):
        if new_direction == int(grid.Compass.SOUTH):
            return 2000

    if current_direction == int(grid.Compass.SOUTH):
        if new_direction == int(grid.Compass.NORTH):
            return 2000
    
    if current_direction == int(grid.Compass.EAST):
        if new_direction == int(grid.Compass.WEST):
            return 2000

    if current_direction == int(grid.Compass.WEST):
        if new_direction == int(grid.Compass.EAST):
            return 2000
        
    return 1000


def create_low_cost_path_grid(g:grid.Grid2D):
    start_point = grid.get_single_symbol_point(g, 'S')
    stop_point = grid.get_single_symbol_point(g, 'E')

    direction = int(grid.Compass.EAST)  # Initial direction
    pq = [(0, (start_point, direction))] # Priority queue list, holding entries with total cost per point (x,y) when moving in a specific direction (NB: Cost must be first item for default comparator)
    visited = set()

    low_cost_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    low_cost_path_grid.set_symbol(start_point, 0) 

    while pq:
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
            print(f"DEBUG: Lowest cost: {c}")
            break

        # Process cardial point (north, south, east, west) immediate neighbours, adding costs

        for compass_direction in [grid.Compass.NORTH, grid.Compass.EAST, grid.Compass.SOUTH, grid.Compass.WEST]:
            np = g.get_neighbour_in_direction(p, compass_direction)
            nd = int(compass_direction)
            if np:
                additional_cost = calculate_change_in_direction_cost(d, nd)
                symbol = g.get_symbol(np)
                if symbol == '.' or symbol == 'E':  
                    cost = 1 + c + additional_cost
                    heapq.heappush(pq, (cost, (np, nd)))

    return low_cost_path_grid


def calcuate_lowest_cost_score(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    stop_point = grid.get_single_symbol_point(g, 'E')

    low_cost_path_grid = create_low_cost_path_grid(g)

    #grid.display_grid(low_cost_path_grid, " ")
    grid.display_grid_evenly_spaced(low_cost_path_grid)
    return low_cost_path_grid.get_symbol(stop_point)


def solve_part1(filename):
    return calcuate_lowest_cost_score(filename)