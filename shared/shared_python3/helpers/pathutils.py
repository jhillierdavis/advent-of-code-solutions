from collections import deque

from helpers import grid, point

DEFAULT_PATH_SYMBOL = '.'

# BFS (Breadth First Search) to find (potentially one of many) a quickest (least steps) path (from start to stop point)
def get_quickest_path(g:grid.Grid2D, start_point:point.Point2D, stop_point:point.Point2D, path_synbol:str=DEFAULT_PATH_SYMBOL):
    cp = start_point

    queue = deque()
    queue.append((start_point, list()))

    visited = set()

    while queue:
        (cp, path) = queue.popleft()

        if cp == stop_point:
            path.append(cp) # Include the end-point
            return path
        
        if cp in visited:
            continue

        neighbours = g.get_cardinal_point_neighbours(cp)
        for np in neighbours:
            ns = g.get_symbol(np)
            if ns == path_synbol:  
                new_path = list(path)
                new_path.append(cp)
                queue.append((np, new_path))
        
        visited.add(cp)

    return None



def get_least_steps(g:grid.Grid2D, block_char:str="#", start_point:point.Point2D = point.Point2D(0, 0), stop_point:point.Point2D = None):
    path = get_least_steps_path(g, block_char, start_point, stop_point)
    if path != None:
        size = len(path)
        #print(f"DEBUG: size={size} start_point={start_point} stop_point={stop_point}")
        return size 
    return None


# BFS (Breadth First Search) to find (potentially one of many) least paths (from start to stop point)
def get_least_steps_path(g:grid.Grid2D, block_char:str="#", start_point:point.Point2D = point.Point2D(0, 0), stop_point:point.Point2D = None):
    cp = start_point

    queue = deque()
    queue.append((start_point, list()))

    visited = set()

    while queue:
        (cp, path) = queue.popleft()

        if cp == stop_point:
            return path
        
        if cp in visited:
            continue

        neighbours = g.get_cardinal_point_neighbours(cp)
        for np in neighbours:
            ns = g.get_symbol(np)
            if ns == PATH_SYMBOL:  
                new_path = list(path)
                new_path.append(cp)
                queue.append((np, new_path))
        
        visited.add(cp)

    return None


def get_cheat_path_ends(g:grid.Grid2D, start_point:point.Point2D, max_length:int, path_char:str="."):
    cheat_path_ends = set()
    cp = start_point

    queue = deque()
    queue.append((start_point, 0))

    visited = set()

    while queue:
        (cp, d) = queue.popleft()

        if d >= max_length or cp in visited:
            continue

        neighbours = g.get_cardinal_point_neighbours(cp)
        for np in neighbours:
            ns = g.get_symbol(np)
            if ns == PATH_SYMBOL:
                if d >= 1 and np not in visited:
                    cheat_path_ends.add((np, d))
            else:
                queue.append((np, d + 1))
        
        visited.add(cp)

    return cheat_path_ends


def get_min_cheat_path_ends(g:grid.Grid2D, start_point:point.Point2D, max_length:int, path_char:str="."):
    cheat_path_end_map = {}
    cp = start_point

    queue = deque()
    queue.append((start_point, 0))

    visited = set()

    while queue:
        (cp, d) = queue.popleft()

        if d > max_length or cp in visited:
            continue

        neighbours = g.get_cardinal_point_neighbours(cp)
        for np in neighbours:
            ns = g.get_symbol(np)
            if ns == PATH_SYMBOL:
                if d >= 1 and np not in visited:
                    #cheat_path_ends.add((np, d))
                    if np not in cheat_path_end_map or d < cheat_path_end_map[np]:
                        cheat_path_end_map[np] = d
            else:
                queue.append((np, d + 1))
        
        visited.add(cp)

    return cheat_path_end_map
