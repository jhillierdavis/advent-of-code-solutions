from helpers import fileutils, grid, point, numutils


def calculate_sum_box_gps_coords(g:grid.Grid2D, box_symbol='[') -> int:
    boxes = g.get_matching_symbol_coords(box_symbol)

    ans = 0
    for b in boxes:
        ans += 100 * b.get_y() + b.get_x()
    return ans    


def generate_second_warehouse(filename):
    start_state_lines = fileutils.get_lines_before_empty_from_file(filename)    

    new_lines = []
    for l in start_state_lines:
        new_line = ""
        for c in l:
            if c == '#' or c == '.':
                new_line += c
                new_line += c
            elif c == 'O':
                new_line += "[]"
            elif c == '@':
                new_line += "@."        
        new_lines.append(new_line)

    #print(f"DEBUG: new_lines={new_lines}")        
    return grid.lines_to_grid(new_lines)


def get_box_at_point(g, p):
    # NB: Specific ordering of return for [] , not ][
    ps = g.get_symbol(p)
    if ps == '[':        
        n = point.Point2D(p.get_x() + 1, p.get_y())
        return (p,n)
    elif ps == ']':
        n = point.Point2D(p.get_x() - 1, p.get_y())
        return (n,p)
    raise Exception(f'No box at p={p}')


def is_empty_at_point(g:grid.Grid2D, p:point.Point2D) -> bool:
    if not p:
        return False
    symbol = g.get_symbol(p)
    return symbol == '.'


def is_box_at_point(g:grid.Grid2D, p:point.Point2D) -> bool:
    ps = g.get_symbol(p)
    if ps == '[' or ps == ']':        
        return True
    return False


def is_wall_at_point(g:grid.Grid2D, p:point.Point2D,) -> bool:
    ps = g.get_symbol(p)
    if ps == '#':
        return True
    return False    


def move_robot_to_next(g:grid.Grid2D, p:point.Point2D, n:point.Point2D) -> point.Point2D:
    ns = g.get_symbol(n)
    assert ns == '.', F"n={n}"

    ps = g.get_symbol(p)
    assert ps == '@', f"p={p}"

    g.set_symbol(n, '@')
    g.set_symbol(p, '.')

    return n


def can_box_be_moved_in_direction(g:grid.Grid2D, p:point.Point2D, box:(point.Point2D, point.Point2D), direction:grid.Compass) -> bool:
    if direction == grid.Compass.NORTH:
        #print(f"DEBUG: Todo - can move North?")
        return can_move_box_north(g, box)
    elif direction == grid.Compass.EAST:
        #print(f"DEBUG: Todo - can move East?")
        hd = horizontal_distance_to_available_space(g, p, direction)
        if hd > 0:
            return True
        return False
    elif direction == grid.Compass.SOUTH:
        return can_move_box_south(g, box)
    if direction == grid.Compass.WEST:
        #print(f"DEBUG: Todo - can move West?")
        hd = horizontal_distance_to_available_space(g, p, direction)
        if hd > 0:
            return True
        return False
    
    return False


def horizontal_distance_to_available_space(g:grid.Grid2D, p:point.Point2D, direction:grid.Compass) -> int:
    symbols = ""
    if direction == grid.Compass.EAST:
        symbols = g.get_symbols_in_direction_by_offset(p, direction, g.get_width() - p.get_x())
    elif direction == grid.Compass.WEST:
        symbols = g.get_symbols_in_direction_by_offset(p, direction, p.get_x())        
    else:
        raise Exception(f'Invalid direction={direction}')
    
    empty = find_first_occurrence(symbols, '.')
    wall = find_first_occurrence(symbols, '#')

    if empty > 0 and empty < wall:
        #grid.display_grid(g)
        #print(f"DEBUG: empty={empty} symbols={symbols} p={p} direction={direction}")
        return empty
    return 0


def find_first_occurrence(input_string, character):
    try:
        index = input_string.index(character)
        return index
    except ValueError:
        return -1
    

def get_box_points_north(g:grid.Grid2D, eb):
    bps = set()
    left, right = eb

    n = g.get_neighbour_north(left)
    if is_box_at_point(g, n):
        pb = get_box_at_point(g, n)
        if pb:
            bps.add(pb)

    n = g.get_neighbour_north(right)
    if is_box_at_point(g, n):        
        pb = get_box_at_point(g, n)
        if pb:
            bps.add(pb)

    return bps    
    

def move_box_north(g:grid.Grid2D, box) -> bool:
    #print(f"DEBUG: move_expanded_box_north: box={box}")
    if box == None:
        return 
    
    nebs = get_box_points_north(g, box)    
    for neb in nebs:
        move_box_north(g, neb)

    left, right = box
    if left and right:
        nl = g.get_neighbour_north(left)
        nr = g.get_neighbour_north(right)

        g.set_symbol(nl, '[')
        g.set_symbol(nr, ']')
        g.set_symbol(left, '.')
        g.set_symbol(right, '.')    


def is_wall_to_north(g:grid.Grid2D, p):
    n = g.get_neighbour_north(p)
    return is_wall_at_point(g, n)


def is_wall_to_south(g:grid.Grid2D, p):
    n = g.get_neighbour_south(p)
    return is_wall_at_point(g, n)


def is_empty_to_north(g:grid.Grid2D, p):
    n = g.get_neighbour_north(p)
    return is_empty_at_point(g, n)


def is_empty_north_of_box(g, expanded_box):
    left, right = expanded_box
    if is_empty_to_north(g, left) and is_empty_to_north(g, right):
        return True
    return False

def is_wall_north_of_box(g, eb):
    left, right = eb
    if is_wall_to_north(g, left) or is_wall_to_north(g, right):
        return True
    return False


def is_wall_south_of_box(g, eb):
    left, right = eb
    if is_wall_to_south(g, left) or is_wall_to_south(g, right):
        return True
    return False


def can_move_box_north(g:grid.Grid2D, eb) -> bool:
    nebs = get_box_points_north(g, eb)
    size = len(nebs)

    if is_wall_north_of_box(g, eb):
        return False

    if size <= 0:
        if not is_empty_north_of_box(g, eb):
            return False
        return True
    

    for neb in nebs:
        if not can_move_box_north(g, neb):
            return False
    return True


def get_box_points_south(g:grid.Grid2D, eb):
    bps = set()
    left, right = eb

    n = g.get_neighbour_south(left)
    if is_box_at_point(g, n):
        pb = get_box_at_point(g, n)
        if pb:
            bps.add(pb)

    n = g.get_neighbour_south(right)
    if is_box_at_point(g, n):        
        pb = get_box_at_point(g, n)
        if pb:
            bps.add(pb)

    return bps    
    

def move_box_south(g:grid.Grid2D, box) -> bool:
    #print(f"DEBUG: move_expanded_box_south: box={box}")
    if box == None:
        return 
    
    nebs = get_box_points_south(g, box)    
    for neb in nebs:
        move_box_south(g, neb)

    left, right = box
    if left and right:
        nl = g.get_neighbour_south(left)
        nr = g.get_neighbour_south(right)

        g.set_symbol(nl, '[')
        g.set_symbol(nr, ']')
        g.set_symbol(left, '.')
        g.set_symbol(right, '.')    


def is_empty_to_south(g:grid.Grid2D, p):
    n = g.get_neighbour_south(p)
    return is_empty_at_point(g, n)


def is_empty_south_of_box(g, expanded_box):
    left, right = expanded_box
    if is_empty_to_south(g, left) and is_empty_to_south(g, right):
        return True
    return False


def can_move_box_south(g:grid.Grid2D, eb) -> bool:
    if is_wall_south_of_box(g, eb):
        return False


    nebs = get_box_points_south(g, eb)
    size = len(nebs)
    if size <= 0:
        if not is_empty_south_of_box(g, eb):
            return False
        return True
    
    for neb in nebs:
        if not can_move_box_south(g, neb):
            return False
    return True


def move_robot_to_next_position(g, rp, np):
    g.set_symbol(np, '@')
    g.set_symbol(rp, '.')
    return np


def apply_second_warehouse_movements(g:grid.Grid2D, movement_lines) -> grid.Grid2D:
    rp = g.get_matching_symbol_coords('@')[0]
    #print(rp)
    #gms = g.clone()
    #width = gms.get_width()
    #height = gms.get_height()

    t = 0    
    for l in movement_lines:
        for mi in l:
            t += 1
            #print(f"t={t} m={mi}")
            #grid.display_grid(g)
            #grid.display_grid(g, "", False)
            #print('\n')

            if mi == '^':
                direction = grid.Compass.NORTH
                #print(f'DEBUG: Move {direction} (from rp={rp}) at t={t}')
                np = g.get_neighbour_north(rp)        
                if is_wall_at_point(g, np):
                    continue
                elif is_empty_at_point(g, np):
                    rp = move_robot_to_next(g, rp, np)
                elif is_box_at_point(g, np):
                    box = get_box_at_point(g, np)
                    if can_box_be_moved_in_direction(g, rp, box, direction): 
                        move_box_north(g, box)
                        rp = move_robot_to_next_position(g, rp, np)


            elif mi == '>':
                direction = grid.Compass.EAST
                #print(f'DEBUG: Move {direction} (from rp={rp}) at t={t}')
                np = g.get_neighbour_east(rp)        
                if is_wall_at_point(g, np):
                    continue
                elif is_empty_at_point(g, np):
                    rp = move_robot_to_next(g, rp, np)
                elif is_box_at_point(g, np):
                    box = get_box_at_point(g, np)
                    if can_box_be_moved_in_direction(g, rp, box, direction):
                        hd = horizontal_distance_to_available_space(g, rp, direction)
                        for i in range(1, hd):
                            p = point.Point2D(np.get_x()+i, np.get_y())
                            if numutils.is_odd(i):
                                g.set_symbol(p,'[')
                            else:
                                g.set_symbol(p,']')
                        rp = move_robot_to_next_position(g, rp, np)


            elif mi == 'v':
                direction = grid.Compass.SOUTH
                #print(f'DEBUG: Move {direction} (from rp={rp}) at t={t}')
                np = g.get_neighbour_south(rp)        
                if is_wall_at_point(g, np):
                    continue
                elif is_empty_at_point(g, np):
                    rp = move_robot_to_next(g, rp, np)
                elif is_box_at_point(g, np):
                    box = get_box_at_point(g, np)
                    if can_box_be_moved_in_direction(g, rp, box, direction):
                        #print(f'DEBUG: TODO: Move boxes {direction}')
                        move_box_south(g, box)
                        rp = move_robot_to_next_position(g, rp, np)

                        

            elif mi == '<':
                direction = grid.Compass.WEST
                #print(f'DEBUG: Move {direction} (from rp={rp}) at t={t}')
                np = g.get_neighbour_west(rp)        
                if is_wall_at_point(g, np):
                    continue
                elif is_empty_at_point(g, np):
                    rp = move_robot_to_next(g, rp, np)
                elif is_box_at_point(g, np):
                    box = get_box_at_point(g, np)
                    if can_box_be_moved_in_direction(g, rp, box, direction):
                        #print(f'DEBUG: Move boxes {direction}')
                        hd = horizontal_distance_to_available_space(g, rp, direction)
                        for i in range(1, hd):
                            p = point.Point2D(np.get_x()-i, np.get_y())
                            if numutils.is_odd(i):
                                g.set_symbol(p,']')
                            else:
                                g.set_symbol(p,'[')
                        rp = move_robot_to_next_position(g, rp, np)
                        
            else:
                raise Exception(f'Invalid movement instruction: {mi}')
            
    return g


def solve_part2(filename):
    #print(f"DEBUG filename={filename}")
    g = generate_second_warehouse(filename)

    #grid.display_grid(g, "", False)
    #print('\n')

    movement_lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: movement_lines={movement_lines}")
    g = apply_second_warehouse_movements(g, movement_lines)

    #grid.display_grid(g, "", False)

    return calculate_sum_box_gps_coords(g)