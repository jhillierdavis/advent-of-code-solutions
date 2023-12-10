from helpers import fileutils, grid, point

from collections import defaultdict

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

def can_move_right(current, next):
    if (current == 'S' or current == '-' or current == 'L' or current == 'F') and next in ['-', '7', 'J']: # right -> right, down, up
        return True
    return False

def can_move_down(current, next):
    if (current == 'S' or current == '|' or current == 'F' or current == '7') and next in ['|', 'L', 'J' ]: # down -> down, right, left
        return True
    return False

def can_move_up(current, next):
    if (current == 'S' or  current == '|' or current == 'J' or current == 'L') and next in ['|', 'F' , '7']: # up -> up, right, left
        return True
    return False

def can_move_left(current, next):
    if (current == 'S' or current == '-' or current == 'J' or current == '7') and next in ['-', 'L', 'F']: # left -> left, up, down
        return True
    return False

def can_move_from_to(current, next):
    if next == 'S':
        return True

    if current == 'S':
        return next in ['-', '|']

    if can_move_right(current, next) or can_move_left(current, next) or can_move_down(current, next) or can_move_up(current, next):
        return True
    return False

def can_move_from_point_to_point(g, cp, np):
    cps = g.get_symbol(cp)
    nps = g.get_symbol(np)

    print(f"DEBUG: cps={cps} nps={nps} cp={cp} nps={nps}")

    if nps == 'S':
        return True

    if cp.get_x() - np.get_x() == 1:  # Moving left
        return can_move_left(cps, nps)

    if cp.get_x() - np.get_x() == -1:  # Moving right
        return can_move_right(cps, nps)
    
    if cp.get_y() - np.get_y() == 1:  # Moving up
        return can_move_up(cps, nps)

    if cp.get_y() - np.get_y() == -1:  # Moving down
        return can_move_down(cps, nps)
    
    return False


def get_max_loop_distance(g, sp):
    sp_symbol = g.get_symbol(sp)

    distance_set = set()
    n_set = g.get_cardinal_point_neighbours(sp)
    for n in n_set:
        if can_move_from_point_to_point(g, sp, n):
            n_symbol = g.get_symbol(n)
            print(f"DEBUG: Can move: {sp_symbol} -> {n_symbol}")

            count = get_count_loop_length(g,sp,n,[])
            distance_set.add((1 + count) / 2)
    return max(distance_set) if len(distance_set) > 0 else 0

def get_count_loop_length(g, fp, cp, path):
    #print(f"DEBUG: current_point={cp} path={path}")

    if cp == fp:
        count = len(path)
        #print(f"DEBUG: At finish point after count={count}")
        #print(f"DEBUG: Start to finish path={path}")
        return count

    cp_symbol = g.get_symbol(cp)

    count_list = []
    n_set = g.get_cardinal_point_neighbours(cp)
    for n in n_set:
        n_symbol = g.get_symbol(n)
        if n_symbol == '.': # Ground
            continue

        if n in path:
            continue

        if not can_move_from_point_to_point(g, cp, n):
            print(f"DEBUG: Cannot move from current={cp_symbol} to next={n_symbol} !")
            continue

        #print(f"DEBUG: Can move: {cp_symbol} -> {n_symbol}")

        # Store the current path (if not already done)    
        if not cp in path:
            path.append(cp)   

        count = get_count_loop_length(g, fp, n, path)  
        count_list.append(count)
        
    return max(count_list) if len(count_list) > 0 else 0

def find_starting_position(g):
    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            if g.get_symbol(p) == 'S':
                print(f"DEBUG: Starting point: {p}")
                return p

    raise ValueError("No starting point 'S' in grid={g}!")

def solve(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
     
    sp = find_starting_position(g)    
    return get_max_loop_distance(g, sp)
