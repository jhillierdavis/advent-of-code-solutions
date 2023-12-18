#from collections import defaultdict
from helpers import fileutils, grid, point, fjl7gridutils
from helpers.polygonutils import calculate_polygon_area_from

def to_fjl7_grid(lines:[], grid_size:int, path:set) -> grid.Grid2D:
    # Create a grid using format from AOC 2023 Day 10
    g = grid.Grid2D(grid_size, grid_size)

    sp = point.Point2D(grid_size // 2, grid_size // 2)    
    cp = sp
    path.add(cp)
    last_move = '?'

    for l in lines:
        m,d,_ = l.split()
        d = int(d)        
        #print(f"DEBUG: m={m} d={d}, c={c} l={l} cp={cp}")
        for _ in range(d):            
            if m == 'R':                            
                if last_move == 'D':
                    g.set_symbol(cp, 'L')
                elif last_move == 'U':
                    g.set_symbol(cp, 'F')
                else:
                    g.set_symbol(cp, '-')
                cp = point.Point2D(cp.get_x()+1, cp.get_y())                    
            elif m == 'L':
                if last_move == 'D':
                    g.set_symbol(cp, 'J')
                elif last_move == 'U':
                    g.set_symbol(cp, '7')
                else:
                    g.set_symbol(cp, '-')
                cp = point.Point2D(cp.get_x()-1, cp.get_y())                    
            elif m == 'D':
                
                if last_move == 'R':
                    g.set_symbol(cp, '7')
                elif last_move == 'L':
                    g.set_symbol(cp, 'F')
                else:
                    g.set_symbol(cp, '|')
                cp = point.Point2D(cp.get_x(), cp.get_y()+1)                    
            elif m == 'U':
                
                if last_move == 'R':
                    g.set_symbol(cp, 'J')
                elif last_move == 'L':
                    g.set_symbol(cp, 'L')
                else:                    
                    g.set_symbol(cp, '|')            
                cp = point.Point2D(cp.get_x(), cp.get_y()-1)
                
            path.add(cp)
            last_move = m

    g.set_symbol(sp, 'S')
    return g

def solve_using_fjl7_grid_from(filename, grid_size=100):
    lines = fileutils.get_file_lines(filename)

    path = set()
    g = to_fjl7_grid(lines, grid_size, path)

    count_perimeter = len(path)
    count_interior = fjl7gridutils.count_contained_squares_from_fjl7_grid(g)
    return count_perimeter + count_interior

"""
def solve_part1_using_area_calculation_from(filename):
    lines = fileutils.get_file_lines(filename)

    coords = []
    x:int = 0; y:int = 0
    coords.append((x,y))
    perimeter:int = 0
    for l in lines:
        direction, distance, _ = l.split()
        distance = int(distance)            
        if direction == 'R':
            x += distance
        if direction == 'L':
            x -= distance
        if direction == 'D':
            y += distance
        if direction == 'U':
            y -= distance
        coords.append((x,y))
        perimeter += distance

    area = int(calculate_polygon_area_from(coords))
    interior_points = int(area - (perimeter / 2) + 1) # Adjust for perimeter (for size 1)
    return perimeter + interior_points
"""

def solve_part1(filename, grid_size=100):
    return solve_using_fjl7_grid_from(filename, grid_size)
    #return solve_part1_using_area_calculation_from(filename)

"""
def get_direction_and_distance_from(hexcode):
    hex_distance = "0x" + hexcode[2:-2]
    hex_direction = int(hexcode[-2:-1])
    #print(f"DEBUG: {hexcode} {hex_distance} {hex_direction}")

    direction = '?'
    if hex_direction == 0:
        direction = 'R'
    elif hex_direction == 1:
        direction = 'D'
    elif hex_direction == 2:
        direction = 'L'
    elif hex_direction == 3:
        direction = 'U'

    return (direction, int(hex_distance, 16))


def to_grid_coords_and_perimeter_size_from(filename):
    lines = fileutils.get_file_lines(filename)

    coords = []
    x:int = 0; y:int = 0
    coords.append((x,y))
    perimeter:int = 0
    for l in lines:
        _,_,c = l.split()
        direction, distance = get_direction_and_distance_from(c)
        if direction == 'R':
            x += distance
        if direction == 'L':
            x -= distance
        if direction == 'D':
            y += distance
        if direction == 'U':
            y -= distance
        coords.append((x,y))
        perimeter += distance
    return coords, perimeter


def solve_part2(filename):
    coords, perimeter = to_grid_coords_and_perimeter_size_from(filename)
    #print(f"DEBUG: perimeter={perimeter}")
    #print(f"DEBUG: coords={coords}")
    
    area = int(calculate_polygon_area_from(coords))
    interior_points = int(area - (perimeter / 2) + 1) # Adjust for perimeter (for size 1)
    return perimeter + interior_points
"""