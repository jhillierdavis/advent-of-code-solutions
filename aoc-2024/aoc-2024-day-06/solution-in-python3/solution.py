from helpers import fileutils, grid, point


# Grid positions character symbols
EMPTY_POSITION = '.'
STARTING_POSITION = '^'
EXISTING_OBSTRUCTION = '#'
VISITED_POSITION = 'X'
PLACED_OBSTRUCTION = 'O'


def get_starting_point_from(g):
    starting_points = g.get_points_matching(STARTING_POSITION)
    assert len(starting_points) == 1
    return starting_points.pop()


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


def get_traversed_path_points(g, sp):
    direction = grid.Compass.NORTH
    gc = g.clone()
    gc.set_symbol(sp, VISITED_POSITION)
    cp = sp

    while True:        
        np = get_next_movement_point(g, cp, direction)
        #print(f"DEBUG: cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            break
        
        ns = g.get_symbol(np)
        if EXISTING_OBSTRUCTION == ns: # Change direction (as movement blocked)
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step (and record current point as visited)
            cp = np
            gc.set_symbol(cp, VISITED_POSITION)

    #grid.display_grid(gc)
    return gc.get_points_matching(VISITED_POSITION)


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    sp = get_starting_point_from(g)
    #print(f"DEBUG: starting point = {sp}")

    traversed_path_points = get_traversed_path_points(g, sp)    
    return len(traversed_path_points)


def goes_off_grid_or_loops(g, cp, direction):
    visited = set()

    while True:        
        np = get_next_movement_point(g, cp, direction)
        #print(f"DEBUG: cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            return False

        ns = g.get_symbol(np)
        if EXISTING_OBSTRUCTION == ns: # Change direction
            direction = get_direction_when_turn_right_by_90(direction)
        else: # Move a step
            if (np, direction) in visited: 
                return True # Loop detected (as point visited with same direction)
            visited.add((np, direction)) 
            cp = np


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    sp = get_starting_point_from(g)

    traversed_path_points = get_traversed_path_points(g, sp)    

    # Count movement steps
    direction = grid.Compass.NORTH
    g_ans = g.clone()

    for p in traversed_path_points:
        gc = g.clone()
        gc.set_symbol(p, EXISTING_OBSTRUCTION)
    
        if goes_off_grid_or_loops(gc, sp, direction):
            g_ans.set_symbol(p, PLACED_OBSTRUCTION)

    return g_ans.count_symbol(PLACED_OBSTRUCTION)