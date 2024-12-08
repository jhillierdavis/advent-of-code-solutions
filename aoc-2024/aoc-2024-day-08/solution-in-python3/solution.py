# Standard Python3 libraries
from collections import defaultdict
import string

# Own shared libraries
from helpers import fileutils, grid, point


antinode_symbol = '#'


def get_antennae_symbols():
    return list(string.ascii_uppercase + string.ascii_lowercase + string.digits)


def get_antennae_type_to_position_map(g):
    antennae_map = defaultdict(set)
    antennae_symbols = get_antennae_symbols()
    for symbol in antennae_symbols:
        ch = symbol
        smp = g.get_points_matching(ch)
        antennae_map[ch] = smp
    return antennae_map


def is_valid_antinode_position(g:grid.Grid2D, p:point.Point2D, antennae_type:chr):
    return g.contains(p) and g.get_symbol(p) != antennae_type


def get_antinode_points(g:grid.Grid2D, current:point.Point2D, next:point.Point2D, antennae_type:chr):
    x_offset = current.get_x() - next.get_x()
    y_offset = current.get_y() - next.get_y()

    potentials = set() # Set of potential antinode positions for this particular antennae type
    potentials.add( point.Point2D(current.get_x() + x_offset, current.get_y() + y_offset) )
    potentials.add( point.Point2D(current.get_x() - x_offset, current.get_y() - y_offset) )
    potentials.add( point.Point2D(next.get_x() + x_offset, next.get_y() + y_offset) )
    potentials.add( point.Point2D(next.get_x() - x_offset, next.get_y() - y_offset) )

    actuals = set()       
    for p in potentials:
        if is_valid_antinode_position(g, p, antennae_type):
            actuals.add(p)    
    return actuals


def get_extended_antinode_points(g:grid.Grid2D, current:point.Point2D, next:point.Point2D, antennae_type:chr):
    x_initial_offset = current.get_x() - next.get_x()
    y_initial_offset = current.get_y() - next.get_y()

    potentials = set() # Set of potential antinode positions for this particular antennae type
    for z in range(1, g.get_height()): # TODO: Use a smarter approach?
        x_offset = z * x_initial_offset
        y_offset = z * y_initial_offset

        potentials.add( point.Point2D(current.get_x() + x_offset, current.get_y() + y_offset) )
        potentials.add( point.Point2D(current.get_x() - x_offset, current.get_y() - y_offset) )
        potentials.add( point.Point2D(next.get_x() + x_offset, next.get_y() + y_offset) )
        potentials.add( point.Point2D(next.get_x() - x_offset, next.get_y() - y_offset) )

    actuals = set()
    for p in potentials:
        if g.contains(p):
            actuals.add(p)
    
    return actuals


def get_count_of_antinotes_from(filename:string, fnc:callable):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    # Find antenane position points for each antenane types in grid
    antennae_map = get_antennae_type_to_position_map(g)
    #print(f'DEBUG: antennae_map={antennae_map}')

    # Grid to mark unique antinode positions  (and check against examples given)
    g_ans = g.clone()

    # For each antenane type point, find distance to next and mark antinodes
    for k in antennae_map.keys():
        v = antennae_map[k]
        size = len(v)
        if size <= 1:
            continue # Ignore single antennae types
        
        #print(f'DEBUG: k={k} v={v} size={size}')
        
        for i in range(size):
            current = list(v)[i]
            for j in range(i+1,):
                next = list(v)[j]
                if current == next:
                    continue # Ignore antennae comparison to own position
                
                actuals =  fnc(g, current, next, k)   
                for a in actuals:
                    g_ans.set_symbol(a, antinode_symbol)

    #grid.display_grid(g_ans)
    return g_ans.count_symbol(antinode_symbol)


def solve_part1(filename:string):
    return get_count_of_antinotes_from(filename, get_antinode_points)


def solve_part2(filename:string):
    return get_count_of_antinotes_from(filename, get_extended_antinode_points)