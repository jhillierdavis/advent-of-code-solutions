from helpers import fileutils, grid, point


def has_moved_into_space(g:grid.Grid2D, p:point.Point2D, n:point.Point2D, target_symbol:str='O') -> point.Point2D:
    if n == None:
        return False

    ns = g.get_symbol(n)
    if ns != '#':
        g.set_symbol(n, '@')
        g.set_symbol(p, '.')

        #grid.display_grid(g)
        #print('\n')
        return True
    return False


def has_moved_boxes(g:grid.Grid2D, p:point.Point2D, n:point.Point2D) -> point.Point2D:
    if n == None:
        return False

    ps = g.get_symbol(p)
    ns = g.get_symbol(n)
    if ns ==  'O':
        g.set_symbol(n, ps)
        g.set_symbol(p, ns)

        #grid.display_grid(g)
        #print('\n')
        return True
    return False


def find_first_occurrence(input_string, character):
    try:
        index = input_string.index(character)
        return index
    except ValueError:
        return -1


def apply_movements(gss:grid.Grid2D, movement_lines:str) -> grid.Grid2D:
    rp = gss.get_matching_symbol_coords('@')[0]
    #print(rp)
    gms = gss.clone()
    width = gms.get_width()
    height = gms.get_height()
    for l in movement_lines:
        for mi in l:
            if mi == '^':
                print(f'Move North')
                np = gms.get_neighbour_north(rp)
                ns = gms.get_symbol(np)
                if '.' == ns:
                    if has_moved_into_space(gms, rp, np, '.'):
                        rp = np
                elif 'O' == ns:
                    offset = rp.get_y()
                    symbols = gms.get_symbols_in_direction_by_offset(rp, grid.Compass.NORTH, offset)
                    if '.' in symbols: # Can move
                        offset = find_first_occurrence(symbols, '.')
                        wall = find_first_occurrence(symbols, '#')
                        if wall == -1 or offset < wall:
                            op = point.Point2D(rp.get_x(), rp.get_y() - offset)
                            ops = gms.get_symbol(op)
                            assert ops == '.', f"ops={ops} op={op} offset={offset} symbols={symbols}"
                            gms.set_symbol(op, 'O')
                            if has_moved_into_space(gms, rp, np, 'O'):
                                rp = np


            elif mi == 'v':
                print(f'Move South')
                np = gms.get_neighbour_south(rp)

                ns = gms.get_symbol(np)
                if '.' == ns:
                    if has_moved_into_space(gms, rp, np, '.'):
                        rp = np
                elif 'O' == ns:
                    offset = height - rp.get_y()
                    symbols = gms.get_symbols_in_direction_by_offset(rp, grid.Compass.SOUTH, offset)
                    if '.' in symbols: # Can move
                        offset = find_first_occurrence(symbols, '.')
                        wall = find_first_occurrence(symbols, '#')
                        if wall == -1 or offset < wall:
                            op = point.Point2D(rp.get_x(), rp.get_y() + offset)
                            ops = gms.get_symbol(op)
                            assert ops == '.', f"ops={ops} op={op} offset={offset} symbols={symbols}"
                            gms.set_symbol(op, 'O')
                            if has_moved_into_space(gms, rp, np, 'O'):
                                rp = np

            elif mi == '<':
                print(f'Move West')
                np = gms.get_neighbour_west(rp)
                ns = gms.get_symbol(np)
                
                if '.' == ns:
                    if has_moved_into_space(gms, rp, np, '.'):
                        rp = np
                elif 'O' == ns:
                    offset = rp.get_x()
                    symbols = gms.get_symbols_in_direction_by_offset(rp, grid.Compass.WEST, offset)
                    if '.' in symbols: # Can move
                        offset = find_first_occurrence(symbols, '.')
                        wall = find_first_occurrence(symbols, '#')
                        #print(f"DEBUG: offset={offset} wall={wall} symbols={symbols} ns={ns} np={np} rp={rp}")
                        if wall == -1 or offset < wall:
                            op = point.Point2D(rp.get_x() - offset, rp.get_y())
                            ops = gms.get_symbol(op)
                            assert ops == '.', f"ops={ops} op={op} offset={offset} symbols={symbols}"
                            gms.set_symbol(op, 'O')
                            if has_moved_into_space(gms, rp, np, 'O'):
                                rp = np

                

            elif mi == '>':
                print(f'Move East')
                np = gms.get_neighbour_east(rp)   

                ns = gms.get_symbol(np)
                if '.' == ns:
                    if has_moved_into_space(gms, rp, np, '.'):
                        rp = np
                elif 'O' == ns:
                    offset = width - rp.get_x()
                    symbols = gms.get_symbols_in_direction_by_offset(rp, grid.Compass.EAST, offset)
                    if '.' in symbols: # Can move
                        offset = find_first_occurrence(symbols, '.')
                        wall = find_first_occurrence(symbols, '#')
                        if wall == -1 or offset < wall:
                            op = point.Point2D(rp.get_x() + offset, rp.get_y())
                            ops = gms.get_symbol(op)
                            assert ops == '.', f"ops={ops} op={op} offset={offset} symbols={symbols}"
                            gms.set_symbol(op, 'O')
                            if has_moved_into_space(gms, rp, np, 'O'):
                                rp = np

            else:
                print(f'Move invalid {mi}')
                raise Exception(f'Invalid movement instruction: {mi}')
    return gms


def end_state(filename_instructions, filename_end_state) -> bool:
    start_state_lines = fileutils.get_lines_before_empty_from_file(filename_instructions)
    
    print(f"DEBUG: {start_state_lines}")    
    gss = grid.lines_to_grid(start_state_lines)
    #print('Start grid:')
    #grid.display_grid(gss)
    #print('\n')

    movement_lines = fileutils.get_lines_after_empty_from_file(filename_instructions)
    print(f'Movement lines: {movement_lines}\n')

    end_state_lines = fileutils.get_file_lines(filename_end_state)
    ges = grid.lines_to_grid(end_state_lines)
    """
    print('Target end grid:')
    grid.display_grid(ges)
    print('\n')
    """

    gms = apply_movements(gss, movement_lines)

    count_boxes_start = len(gss.get_matching_symbol_coords('O'))
    count_boxes_end = len(gms.get_matching_symbol_coords('O'))
    assert count_boxes_start == count_boxes_end
    print(f"DEBUG: boxes = {count_boxes_end}")

    count_walls_start = len(gss.get_matching_symbol_coords('#'))
    count_walls_end = len(gms.get_matching_symbol_coords('#'))
    assert count_walls_start == count_walls_end

    print('\n')
    print('End grid:')
    grid.display_grid(gms)
    print('\n')

    print('Target end grid:')
    grid.display_grid(ges)

    return ges.__eq__(gms)


def calculate_sum_box_gps_coords(g:grid.Grid2D, box_symbol='O') -> int:
    boxes = g.get_matching_symbol_coords(box_symbol)

    ans = 0
    for b in boxes:
        ans += 100 * b.get_y() + b.get_x()
    return ans    


def solve_part1(filename):
    start_state_lines = fileutils.get_lines_before_empty_from_file(filename)
    
    #print(f"DEBUG: {start_state_lines}")    
    gss = grid.lines_to_grid(start_state_lines)
    #print('Start grid:')
    #grid.display_grid(gss)
    #print('\n')

    movement_lines = fileutils.get_lines_after_empty_from_file(filename)
    gms = apply_movements(gss, movement_lines)
    return calculate_sum_box_gps_coords(gms)