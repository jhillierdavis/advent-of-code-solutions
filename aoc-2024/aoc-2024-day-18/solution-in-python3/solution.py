# Solution implementation using Dijkstra's_algorithm (see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm )

from helpers import fileutils, grid, point, dijkstra


CORRUPTION_BLOCK_CHAR = '#'


def get_corruption_blocks(lines):
    cbps = [] # Corruption block points
    for l in lines:
        values = l.split(",")
        x = int(values[0])
        y = int(values[1])
        p = point.Point2D(x,y)
        cbps.append(p)
    return cbps


def place_corruption_blocks(g:grid.Grid2D, cbps, count):
    for i in range(count):
        p = cbps[i]
        g.set_symbol(p, CORRUPTION_BLOCK_CHAR) # Blocked


def solve_part1(filename:str, size:int, fallen:int) -> int:
    lines = fileutils.get_file_lines_from(filename)
    cbps = get_corruption_blocks(lines)

    g = grid.Grid2D(size, size)
    place_corruption_blocks(g, cbps, fallen)
    #grid.display_grid(g)    
   
    # Determine the least number of steps in optimum path from top left to bottom right of grid (with blocked corruption points)
    return  dijkstra.get_least_steps(g)


def get_blocked_path_point(g:grid.Grid2D, cbps:[point.Point2D], reachable:int=0) -> (int,int):
    size = len(cbps)
    for i in range(reachable, size):
        p = cbps[i]

        g.set_symbol(p, CORRUPTION_BLOCK_CHAR) # Blocked
            
        # Check whether impassable (based on min. number of steps from start to finish point)    
        if  dijkstra.get_least_steps(g) <= 0: 
            return (p.get_x(), p.get_y())

    return (-1,-1) # Failed


def solve_part2(filename:str, size:int, reachable:int) -> (int,int):
    lines = fileutils.get_file_lines_from(filename)
    cbps = get_corruption_blocks(lines)


    g = grid.Grid2D(size, size)
    # NB: We know (from Part 1) the 'reachable' block points (i.e. those that do not make an impassable path), 
    # # so place those on the grid
    place_corruption_blocks(g, cbps, reachable)

    # Determine the point when addition of another blocked corruption point causes the traversal path to become impassable    
    return get_blocked_path_point(g, cbps, reachable)