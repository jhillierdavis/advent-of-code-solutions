from collections import defaultdict

from helpers import fileutils, grid, point


def get_rows_without_galaxies(g):
    empty_rows = []
    for y in range(g.get_height()):
        is_empty = True
        for x in range(g.get_width()):
            s = g.get_symbol(point.Point2D(x, y))
            if s == '#':
                is_empty = False
                break
        if is_empty:
            empty_rows.append(y)
    return empty_rows
    
def get_columns_without_galaxies(g):
    empty_cols = []
    for x in range(g.get_width()):
        is_empty = True
        for y in range(g.get_height()):
            s = g.get_symbol(point.Point2D(x, y))
            if s == '#':
                is_empty = False
                break
        if is_empty:
            empty_cols.append(x)
    return empty_cols


def get_grid_from_filename(filename):
    lines = fileutils.get_file_lines(filename)
    #print(f"DEBUG: lines={lines}")

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    return g

def get_empty_rows_from_filename(filename):
    g = get_grid_from_filename(filename)    
    empty_rows = get_rows_without_galaxies(g)
    print(f"DEBUG: empty_rows={empty_rows}")
    return empty_rows

def get_empty_columns_from_filename(filename):
    g = get_grid_from_filename(filename)    
    empty_cols = get_columns_without_galaxies(g)
    print(f"DEBUG: empty_cols={empty_cols}")
    return empty_cols


def solve(filename):
    g = get_grid_from_filename(filename)
    
    return 0 # TODO
