from helpers import fileutils, grid, point

def get_starting_point_from(g):
    sp = None
    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            if '^' == g.get_symbol(p):
                sp = p
                break
    return sp


def get_direction_when_turn_right_by_90(direction:grid.Compass) -> grid.Compass:
    if direction == grid.Compass.NORTH:
        return grid.Compass.EAST
    elif direction == grid.Compass.EAST:
        return grid.Compass.SOUTH
    elif direction == grid.Compass.SOUTH:
        return grid.Compass.WEST
    elif direction == grid.Compass.WEST:
        return grid.Compass.NORTH
    else:
        raise Exception(f"Unknown direction: {direction}")


def get_next_movement_point(g:grid.Grid2D, cp:point.Point2D, direction:grid.Compass) -> point.Point2D:
    if direction == grid.Compass.NORTH:
        return g.get_neighbour_north(cp)
    elif direction == grid.Compass.EAST:
        return g.get_neighbour_east(cp)
    elif direction == grid.Compass.SOUTH:
        return g.get_neighbour_south(cp)
    elif direction == grid.Compass.WEST:
        return g.get_neighbour_west(cp)
    else:
        raise Exception(f"Unknown direction: {direction}")


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    sp = get_starting_point_from(g)

    #print(f"DEBUG: starting point = {sp}")
    
    # Count movement steps
    direction = grid.Compass.NORTH
    np = None
    cp = sp
    gc = g.clone()
    gc.set_symbol(sp, 'X')

    while True:        
        np = get_next_movement_point(g, cp, direction)
        #print(f"DEBUG: cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            break
        
        ns = g.get_symbol(np)
        if '#' == ns: # Change direction (as movement blocked)
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step
            cp = np
            gc.set_symbol(cp, 'X')

    #grid.display_grid(gc)
    return gc.count_symbol('X')


def has_loop(g, cp, direction, np):
    visited = set()

    while True:
        np = get_next_movement_point(g, cp, direction)

        #print(f"DEBUG: i={i} cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            return False

        ns = g.get_symbol(np)
        if '#' == ns: # Change direction
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step
            if (np, direction) in visited: 
                return True
            visited.add((np, direction)) 
            cp = np


def solve_part2(filename): # Wrong answer!
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    sp = get_starting_point_from(g)
    #print(f"DEBUG: starting point = {sp}")

    # Count movement steps
    direction = grid.Compass.NORTH
    np = None
    cp = sp
    g_ans = g.clone()
    
    while True:        
        np = get_next_movement_point(g, cp, direction)
        #print(f"DEBUG: cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            break
        
        ns = g.get_symbol(np)
        if '#' == ns: # Change direction
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step
            
            gc = g.clone()
            gc.set_symbol(np, '#')
            if has_loop(gc, cp, direction, np):
                if g_ans.get_symbol(np) == '.':
                    g_ans.set_symbol(np, '0')   
            cp = np

    grid.display_grid(g_ans)
    return g_ans.count_symbol('0')


def goes_off_grid_or_loops(g, cp, direction):
    visited = set()

    while True:        
        np = get_next_movement_point(g, cp, direction)
        #print(f"DEBUG: cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            return False

        ns = g.get_symbol(np)
        if '#' == ns: # Change direction
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step
            if (np, direction) in visited: 
                return True
            visited.add((np, direction)) 
            cp = np


def brute_force(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    sp = get_starting_point_from(g)
    #print(f"DEBUG: starting point = {sp}")

    # Count movement steps
    direction = grid.Compass.NORTH
    g_ans = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            gc = g.clone()
            p = point.Point2D(w,h)
            if gc.get_symbol(p) == '.':
                gc.set_symbol(p, '#')
            
                if goes_off_grid_or_loops(gc, sp, direction):
                    g_ans.set_symbol(p, '0')

    return g_ans.count_symbol('0')