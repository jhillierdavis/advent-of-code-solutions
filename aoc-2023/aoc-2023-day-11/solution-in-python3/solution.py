from collections import defaultdict
import math

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

def get_offset_values(orig_values):
    offset_values = []
    offset = 0    
    for entry in orig_values:        
        offset_values.append(entry + offset)
        offset += 1
    return offset_values


def get_lines_with_duplicated_rows(lines, target_rows):
    new_lines = []
    index = 0
    for l in lines:
        new_lines.append(l)
        if index in target_rows: # Duplicate line
            new_lines.append(l)
        index += 1
    return new_lines

def get_lines_with_duplicated_cols(lines, target_cols):
    new_lines = []    
    for l in lines:    
        nl = ""    
        for i in range(len(l)):
            chr = l[i]
            nl += chr
            if i in target_cols: # Duplicate
                nl += chr
        #print(f"DEBUG: nl={nl} l={l}")                
        new_lines.append(nl)
    return new_lines


def get_expanded_grid_from_filename(filename):
    g = get_grid_from_filename(filename)

    lines = grid.grid_to_lines(g)
    #print(f"DEBUG: grid lines={lines}")

    empty_rows = get_rows_without_galaxies(g)
    empty_cols = get_columns_without_galaxies(g)

    #offset_rows = get_offset_values(empty_rows)
    #print(f"DEBUG: offset_rows={offset_rows}")

    new_lines = get_lines_with_duplicated_rows(lines, empty_rows)
    assert len(new_lines) == len(lines) + len(empty_rows)

    new_lines = get_lines_with_duplicated_cols(new_lines, empty_cols)        
    #print(f"DEBUG: new_lines={new_lines}")

    return grid.lines_to_grid(new_lines)


def get_galaxy_locations(g):
    locations = []
    for x in range(g.get_width()):
        for y in range(g.get_height()):
            p = point.Point2D(x,y)
            if g.get_symbol(p) == '#':
                locations.append(p)
    return locations
    
def get_galaxy_pair_shortest_distances(g):
    locations = get_galaxy_locations(g)
    distances = []

    for lp1 in locations:
        for lp2 in locations:
            if lp1 == lp2:
                break
            distance = abs(lp1.get_x() - lp2.get_x()) + abs(lp1.get_y() - lp2.get_y())
            print(f"Galaxy location={lp1} distance={distance}")
            distances.append(distance)
    return distances


def solve(filename):
    
    g = get_expanded_grid_from_filename(filename)
    
    distances = get_galaxy_pair_shortest_distances(g)
    return sum(distances)