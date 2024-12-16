# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )
#
# NB: Use Heap queue algorithm in Python3: https://docs.python.org/3/library/heapq.html
#
# See AOC 2021 Day 15 for another Dijkstra example.

import heapq, math
from collections import defaultdict, deque

# Local
from helpers import fileutils, grid, point

import solution


def get_count_of_all_best_cost_points(g:grid.Grid2D):
    start_point = grid.get_single_symbol_point(g, 'S')
    stop_point = grid.get_single_symbol_point(g, 'E')

    direction = 2 # grid.Compass.EAST # direction
    pq = [(0, (start_point, direction, None, None))] # Priority queue list, holding entries with total cost per point (x,y)
    #heap = heapq.heapify(pq) # Transform a populated list into a heap
    visited = set()

    #ow_cost_path_grid = grid.Grid2D(g.get_width(), g.get_height())
    #low_cost_path_grid.set_symbol(start_point, 0)

    lowest_cost_map = {(start_point, direction): 0}
    backtrack_map = {}
    #best_cost = float("inf")
    best_cost = math.inf
    end_states = set()
    

    while len(pq) > 0:
        # Get next lowest total risk cost point (x,y) and direction
        c, (p, d, lp, ld) = heapq.heappop(pq)

        #if (p,d) in lowest_cost_map.keys() and c > lowest_cost_map[(p,d)]:
        if c > lowest_cost_map.get((p,d), math.inf):
            continue
        lowest_cost_map[(p,d)] = c 

        # Avoid revisits
        if (p,d) in visited:
            continue # Ignore already visitied points (x,y) on grid
        visited.add((p,d))

        # Track total risk score on (another same size) grid
        #low_cost_path_grid.set_symbol(p, c)

        # Stop when reach target destination point
        if p == stop_point:
            #print(f"DEBUG: Lowest cost: {c}")
            if c > best_cost:
                print(f"DEBUG: Best cost={best_cost}")
                break
            best_cost = c
            end_states.add((p,d))


        # Keep a backtrack record (of visited locations with the direction at the time)
        if (p,d) not in backtrack_map:
            backtrack_map[(p,d)] = set()
        backtrack_map[(p,d)].add((lp, ld))

        # Process cardial point (north, south, east, west) immediate neighbours, adding costs

        np = g.get_neighbour_north(p)
        if np:
            additional_cost =  solution.calculate_change_in_direction_cost(d, 1)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 1, p, d)))

        np = g.get_neighbour_east(p)
        if np:
            additional_cost =  solution.calculate_change_in_direction_cost(d, 2)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 2, p, d)))

        np = g.get_neighbour_south(p)
        if np:
            additional_cost =  solution.calculate_change_in_direction_cost(d, 3)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 3, p, d)))

        np = g.get_neighbour_west(p)
        if np:
            additional_cost = solution.calculate_change_in_direction_cost(d, 4)
            symbol = g.get_symbol(np)
            if symbol == '.' or symbol == 'E':  
                cost = 1 + c + additional_cost
                heapq.heappush(pq, (cost, (np, 4, p, d)))

    states = deque(end_states)
    seen = set(end_states)

    while states:
        key = states.popleft()
        for last in backtrack_map.get(key, []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    #print(seen)

    #points = set((p.get_x(),p.get_y()) for p, _ in seen if p is not None)
    points = set(p for p, _ in seen if p is not None)
    #print(points)
    size = len(points)
    print(size)

    return size




def count_path_points(g:grid.Grid2D, cp, fp, path):
    if cp == fp:
        #print(f"DEBUG: path={path}")
        print(f"DEBUG: size={len(path)}")
        return 1 + len(path)
    
    cs = g.get_symbol(cp)

    path.add(cp)
    neighbours = g.get_cardinal_point_neighbours(cp)

    counts = set()
    for np in neighbours:
        #if np in path:
        #    continue

        ns = g.get_symbol(np)
        if ns == '.':
            continue  

        if ns > cs:
            print(f"DEBUG: {cs}->{ns}")
            new_path = set(path)
            new_path.add(np)
            c = count_path_points(g, np, fp, new_path)
            counts.add(c)

    if len(counts) > 0:
        return max(counts)    
    return 0


def old_solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    return get_count_of_all_best_cost_points(g)


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    start_point = grid.get_single_symbol_point(g, 'S')
    end_point = grid.get_single_symbol_point(g, 'E')
    sx = start_point.get_x()
    sy = start_point.get_y()

    pq = [(0, sx, sy, 0, 1)] # Priority queue list, holding entries with total cost per point (x,y)
    lowest_cost = {(sx, sy, 0, 1): 0}
    backtrack_map = defaultdict(set)
    best_cost = math.inf
    end_states = set()

    while pq:
        cost, x, y, dx, dy = heapq.heappop(pq)
        if cost > lowest_cost.get((x, y, dx, dy), math.inf): 
            continue

        if point.Point2D(x,y) == end_point:
            if cost > best_cost: 
                break
            best_cost = cost
            end_states.add((x, y, dx, dy))

        for new_cost, nx, ny, ndx, ndy in [(cost + 1, x + dx, y + dy, dx, dy), (cost + 1000, x, y, dx, -dy), (cost + 1000, x, y, -dy, dx)]:
            if g.get_symbol(point.Point2D(nx,ny)) == "#": # Ignore walls
                continue

            lowest = lowest_cost.get((nx, ny, ndx, ndy), math.inf)
            
            if new_cost > lowest: 
                continue
            
            if new_cost < lowest:
                backtrack_map[(nx, ny, ndx, ndy)] = set()
                lowest_cost[(nx, ny, ndx, ndy)] = new_cost
            backtrack_map[(nx, ny, ndx, ndy)].add((x, y, dx, dy))
            
            heapq.heappush(pq, (new_cost, nx, ny, ndx, ndy))

    return count_unique_path_points(end_states, backtrack_map)   


def count_unique_path_points(end_states, backtrack_map):
    states = deque(end_states)
    seen = set(end_states)

    while states:
        key = states.popleft()
        for last in backtrack_map.get(key, set()):
            if last in seen: 
                continue
            seen.add(last)
            states.append(last)

    count = len({(r, c) for r, c, _, _ in seen})
    return count    