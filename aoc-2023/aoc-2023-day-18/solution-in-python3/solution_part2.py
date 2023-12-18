from helpers import fileutils
from helpers.polygonutils import calculate_polygon_area_from

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