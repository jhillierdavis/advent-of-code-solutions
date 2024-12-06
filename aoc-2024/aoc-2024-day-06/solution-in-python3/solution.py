from helpers import fileutils, grid, point

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)

    grid.display_grid(g)

    sp = None
    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            if '^' == g.get_symbol(p):
                sp = p
                break

    print(f"DEBUG: starting point = {sp}")

    ans = 0

    # Count movement steps
    direction = grid.Compass.NORTH
    np = None
    cp = sp
    gc = g.clone()
    gc.set_symbol(sp, 'X')

    for i in range(10000):
        
        if direction == grid.Compass.NORTH:
            np = g.get_neighbour_north(cp)
        elif direction == grid.Compass.EAST:
            np = g.get_neighbour_east(cp)
        elif direction == grid.Compass.SOUTH:
            np = g.get_neighbour_south(cp)
        elif direction == grid.Compass.WEST:
            np = g.get_neighbour_west(cp)

        print(f"DEBUG: i={i} cp={cp} np={np} direction={direction}")
        
        if None == np or not g.contains(np): # Off grid
            break
        
        ns = g.get_symbol(np)
        if '#' == ns: # Change direction
            if direction == grid.Compass.NORTH:
                direction = grid.Compass.EAST
            elif direction == grid.Compass.EAST:
                direction = grid.Compass.SOUTH
            elif direction == grid.Compass.SOUTH:
                direction = grid.Compass.WEST
            elif direction == grid.Compass.WEST:
                direction = grid.Compass.NORTH
        else: # Move a step
            cp = np
            ans += 1
            gc.set_symbol(cp, 'X')

    #grid.display_grid(gc)
    return gc.count_symbol('X')

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"