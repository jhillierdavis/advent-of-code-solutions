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
    #print()
    #grid.display_grid(g)
    #print()
            

def solve_part1(filename):
    lines  = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    for i in range(g.get_height()):
        shift_rounded_rocks_north(g)     
    return calculate_load_to_north(g)
