from collections import defaultdict
import math

from helpers import fileutils, grid

GALAXY_SYMBOL = '#' # Should be '@'! ;-)
SPACE_SYMBOL = '.'


def get_grid_from_filename(filename):
    lines = fileutils.get_file_lines(filename)
    #print(f"DEBUG: lines={lines}")

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    return g


def get_all_empty_rows_in_grid(g):
    return g.get_rows_where_only_symbol(SPACE_SYMBOL)    


def get_all_empty_columns_in_grid(g):
    return g.get_columns_where_only_symbol(SPACE_SYMBOL)    


def get_galaxy_locations(g):
    return g.get_matching_symbol_coords(GALAXY_SYMBOL)


def get_empty_rows_from_filename(filename):
    g = get_grid_from_filename(filename)
    return get_all_empty_rows_in_grid(g)


def get_empty_columns_from_filename(filename):
    g = get_grid_from_filename(filename)    
    return get_all_empty_columns_in_grid(g)


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
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)
    empty_rows = get_all_empty_rows_in_grid(g)
    empty_cols = get_all_empty_columns_in_grid(g)

    new_lines = get_lines_with_duplicated_rows(lines, empty_rows)
    assert len(new_lines) == len(lines) + len(empty_rows)

    new_lines = get_lines_with_duplicated_cols(new_lines, empty_cols)        
    #print(f"DEBUG: new_lines={new_lines}")

    return grid.lines_to_grid(new_lines)



def get_galaxy_pair_shortest_distances(g):
    locations = get_galaxy_locations(g)
    distances = []

    for lp1 in locations:
        for lp2 in locations:
            if lp1 == lp2:
                break
            distance = lp1.get_manhatten_distance_to(lp2)
            #print(f"Galaxy location={lp1} distance={distance}")
            distances.append(distance)
    return distances


def get_x_distance(gp1, gp2, empty_cols, expansion_size):
    min_x = min(gp1.get_x(), gp2.get_x())
    max_x = max(gp1.get_x(), gp2.get_x())

    adjustment = 0
    for e in empty_cols:
        if e > min_x and e < max_x:
            adjustment += 1

    distance = max_x - min_x + (adjustment * expansion_size)
    #print(f"DEBUG: distance={distance} min_x={min_x} max_x={max_x} adjustment={adjustment} empty_rows={empty_rows}")
    return distance


def get_y_distance(gp1, gp2, empty_rows, expansion_size):
    min_y = min(gp1.get_y(), gp2.get_y())
    max_y = max(gp1.get_y(), gp2.get_y())

    adjustment = 0
    for e in empty_rows:
        if e > min_y and e < max_y:
            adjustment += 1

    distance = max_y - min_y + (adjustment * expansion_size)
    #print(f"DEBUG: distance={distance} min_y={min_y} max_y={max_y} adjustment={adjustment} empty_cols={empty_cols}")
    return distance


def get_galaxy_pair_shortest_distances_with_calculated_expansion(g, expansion_size):
    locations = get_galaxy_locations(g)
    #print(f"DEBUG: locations={locations}")

    empty_rows = g.get_rows_where_only_symbol(SPACE_SYMBOL)
    empty_cols = g.get_columns_where_only_symbol(SPACE_SYMBOL)
    
    distances = [] # List of distances between pairs of galaxies
    for lp1 in locations:
        for lp2 in locations:
            if lp1 == lp2:
                break
            distance = get_x_distance(lp1, lp2, empty_cols, expansion_size) + get_y_distance(lp1, lp2, empty_rows, expansion_size)
            #print(f"Galaxy distance={distance} lp1={lp1}, lp2={lp2}")
            distances.append(distance)
    return distances


def solve_part1(filename):    
    g = get_expanded_grid_from_filename(filename)
    distances = get_galaxy_pair_shortest_distances(g)
    return sum(distances)


def solve_part2(filename, expansion_ratio):
    g = get_grid_from_filename(filename)

    expansion_size = expansion_ratio - 1 
    distances = get_galaxy_pair_shortest_distances_with_calculated_expansion(g, expansion_size)
    return sum(distances)