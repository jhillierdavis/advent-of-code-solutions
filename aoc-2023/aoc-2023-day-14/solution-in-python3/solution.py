from collections import defaultdict

from helpers import fileutils, grid, point



def count_rounded_rocks_from(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    return g.count_symbol('O')

def calculate_load_to_north(g):
    g = g.get_inverted_vertically()
    #grid.display_grid(g)

    total_load = 0
    coords = g.get_matching_symbol_coords('O')
    for c in  coords:
        total_load += 1 + c.get_y()
    return total_load

def calculate_load_from(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    return calculate_load_to_north(g)

def shift_rounded_rocks_north(g):
    count = 0
    for col in range(1, g.get_height()):
        for row in range(g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_north = point.Point2D(row, col-1)
                s_north =  g.get_symbol(p_north)
                if s_north == '.':
                    g.set_symbol(p_north, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_south(g):
    count = 0
    for col in range(g.get_height()-1):
        for row in range(g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_north = point.Point2D(row, col+1)
                s_north =  g.get_symbol(p_north)
                if s_north == '.':
                    g.set_symbol(p_north, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_west(g):
    count = 0
    for col in range(g.get_height()):
        for row in range(1, g.get_width()):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_next = point.Point2D(row-1, col)
                s_next =  g.get_symbol(p_next)
                if s_next == '.':
                    g.set_symbol(p_next, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def shift_rounded_rocks_east(g):
    count = 0
    for col in range(g.get_height()):
        for row in range(g.get_width()-1):
            p = point.Point2D(row, col)            
            s = g.get_symbol(p)
            if s == 'O':
                p_next = point.Point2D(row+1, col)
                s_next =  g.get_symbol(p_next)
                if s_next == '.':
                    g.set_symbol(p_next, 'O')
                    g.set_symbol(p, '.')
                    count += 1
    return count

def solve_part1(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    for i in range(g.get_height()-1):
        shift_rounded_rocks_north(g)     
    return calculate_load_to_north(g)

def get_repeating_sequence_in(L):
    '''Reduce the input list to a list of all repeated integers in the list.'''
    return [item for item in list(set(L)) if L.count(item) > 1]


def is_repeating_sequence_in(list_of_numbers):
    repeated_sequence = get_repeating_sequence_in(list_of_numbers)
    if len(repeated_sequence) > 0:
        print(f"DEBUG: repeated_set={repeated_sequence}")
        return True
    return False

def solve_part2(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    

    counts = []
    max = 1000000000
    found_repeating_sequence = False
    spin = 0
    while spin < max:
        spin += 1
        count = 0
        for i in range(g.get_height()-1):
            count += shift_rounded_rocks_north(g)     

        for i in range(g.get_width()-1):
            count += shift_rounded_rocks_west(g)     

        for i in range(g.get_height()-1):
            count += shift_rounded_rocks_south(g)     

        for i in range(g.get_width()-1):
            count += shift_rounded_rocks_east(g)     

        #print(f"DEBUG: spin={spin} count={count}")
        if not found_repeating_sequence:
            repeating_sequence = get_repeating_sequence_in(counts)
            repeating_sequence_length = len(repeating_sequence)
        
            if spin > 200 and repeating_sequence_length > 1:
                load = calculate_load_to_north(g)
                remainder = max - spin
                offset = remainder % repeating_sequence_length
                print(f"DEBUG: cycle at spin: {spin} load={load} repeating_sequence_length={repeating_sequence_length} repeating_sequence={repeating_sequence} remainder={remainder} offset={offset}")
                spin = max - offset
                print(f"DEBUG: fast forward to spin={spin}!")
                found_repeating_sequence = True

            counts.append(count)
        else:
            load = calculate_load_to_north(g)
            print(f"DEBUG: spin={spin} load={load}")


    return calculate_load_to_north(g)