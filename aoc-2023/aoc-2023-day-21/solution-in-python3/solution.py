from collections import defaultdict, deque
from collections.abc import Iterable
from itertools import starmap
from operator import add

from helpers import fileutils, grid

def get_cardinal_point_neighbours_at_distance(g, cp, d, coords, visited, wrapping:bool=False):
    #print(f"DEBUG: d={d} {cp}")
    if d == 0:
        coords.add(cp)
        return
    
    neighbours = g.get_cardinal_point_neighbours(cp, wrapping)
    for n in neighbours:
        if (n,d) in visited:
            continue
        else:
            visited.add((n,d))

        if wrapping:
            u = g.get_unwrapped_coord(n)
            #print(f"DEBUG: n={n} u={u}")
            s = g.get_symbol(u)
        else:
            s = g.get_symbol(n)    

        if s != '#':    
            #coords.add(n)        
            get_cardinal_point_neighbours_at_distance(g, n, d -1, coords, visited, wrapping)            
    return


def get_count(g, cp, d, cache):
    if d == 0:

        return 1
    
    count = 0
    neighbours = g.get_cardinal_point_neighbours(cp, True)
    for n in neighbours:
        s = g.get_symbol(n)
        if s != '#':
            count += get_count(g, n, d - 1, cache)
    return count


def new_get_cardinal_point_neighbours_at_distance(g, cp, d, coords_map, visited):
    #print(f"DEBUG: d={d} {cp}")
    if d == 0:
        coords_map[cp] += 1
        return
    
    neighbours = g.get_cardinal_point_neighbours(cp, True)
    for n in neighbours:
        if (n,d) in visited:
            continue
        else:
            visited.add((n,d))

        u = g.get_unwrapped_coord(n)
        #print(f"DEBUG: n={n} u={u}")
        s = g.get_symbol(u)

        if s != '#':    
            new_get_cardinal_point_neighbours_at_distance(g, u, d -1, coords_map, visited)            
    return


def solve_part1(filename, steps):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    matches = g.get_matching_symbol_coords('S')
    cp = matches[0]
    coords = set()
    visited = set()
    get_cardinal_point_neighbours_at_distance(g, cp, steps, coords, visited)
    #print(f"DEBUG: coords={coords}")
    count = len(coords)
    return count


Vector = tuple[int, ...]

def count_paths(
        src_node: Vector,
        path_length: int,
        grid: list[str],
) -> int:
    """
    Count the number of paths with a length of `path_length` from
    `src_node` in a grid of tiles. The paths are allowed to double back
    on themselves.
    """
    result = 0

    height = len(grid)
    width = len(grid[0])

    visited: set[Vector] = set()
    # This is basically a standard breadth-first search
    queue: deque[tuple[int, Vector]] = deque([(0, src_node)])
    while queue:
        cost, node = queue.popleft()

        # If node has been visited before
        if node in visited:
            # Don't explore this path any further
            continue
        visited.add(node)

        # If the current path's parity is the same as the parity of the specified path length
        if cost % 2 == path_length % 2:
            # This path can be reached in the specified number of steps
            result += 1
            # NOTE: We can do this because all paths between any two tiles will have the same parity.
        # If path becomes longer than specified path length
        if cost >= path_length:
            # Don't explore this path any further
            continue

        for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            # Get coordinates at offset
            next_row, next_col = starmap(add, zip(node, offset))
            # If this plot of land is not empty
            if grid[next_row % height][next_col % width] == "#":
                # This neighbour is not valid
                continue
            # Append this neighbour to the queue
            queue.append((cost + 1, (next_row, next_col)))

    return result

def solve_part2(filename:str, steps:int) -> int:
    lines = fileutils.get_file_lines(filename)

    grid = list(lines)
    height = len(grid)
    width = len(grid[0])
    n = steps // width

    # The elf starts in the center of the grid
    a, b, c = (
        count_paths((height // 2, width // 2), s * width + (width // 2), grid)
        for s in range(3)
    )
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
