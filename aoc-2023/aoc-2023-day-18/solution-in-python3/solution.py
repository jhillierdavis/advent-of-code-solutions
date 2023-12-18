#from collections import defaultdict
import math

from helpers import fileutils, grid, point

"""
count ← 0
 foreach side in polygon:
   if ray_intersects_segment(P,side) then
     count ← count + 1
 if is_odd(count) then
   return inside
 else
   return outside

"""
"""
def replace_column_symbols_before(g):
    height = g.get_height()
    width = g.get_width()

    for h in range(height):                   
        for w in range(width):                    
            cp = point.Point2D(w, h)
            s = g.get_symbol(cp)
            if s == '#':
                break
            g.set_symbol(cp, "*")
    
def replace_column_symbols_after(g):
    height = g.get_height()
    width = g.get_width()

    for h in range(height):                   
        for w in range(width):                    
            cp = point.Point2D(width -1 - w, h)
            s = g.get_symbol(cp)
            if s == '#':
                break
            g.set_symbol(cp, "*")

def replace_row_symbols_before(g):
    height = g.get_height()
    width = g.get_width()

    for w in range(width):            
        for h in range(height):                   
            cp = point.Point2D(w, h)
            s = g.get_symbol(cp)
            if s == '#':
                break
            g.set_symbol(cp, "*")


def replace_row_symbols_after(g):
    height = g.get_height()
    width = g.get_width()

    for w in range(width):            
        for h in range(height):                   
            cp = point.Point2D(w, height -1 - h)
            s = g.get_symbol(cp)
            if s == '#':
                break
            g.set_symbol(cp, "*")

def replace_symbols(g):
    replace_column_symbols_before(g)
    replace_column_symbols_after(g)
    replace_row_symbols_before(g)
    replace_row_symbols_after(g)
    grid.display_grid(g)



def get_contained_using_ray_casting(g:grid.Grid2D, perimeter:set):
    contained_vertically = get_contained_vertically_using_ray_casting(g, perimeter)
    contained_horizontally = get_contained_horizontally_using_ray_casting(g, perimeter)
    return contained_vertically.intersection(contained_horizontally)

def get_contained_vertically_using_ray_casting(g:grid.Grid2D, perimeter:set) -> set:
    contained = set()

    for w in range(g.get_width()):
        is_within = False
        tmp = set()        
        for h in range(g.get_height()):            
            cp = point.Point2D(w, h)

            if cp in perimeter:
                pp = point.Point2D(w, h-1)
                if h == 0 or pp not in perimeter:
                    is_within = False if is_within else True # Toggle
                if h < g.get_height() - 1:
                    continue

            if is_within:
                tmp.add(cp)

            if (h < g.get_height() - 1 or False == is_within) and len(tmp) > 0:
                contained.update(tmp)

    print(f"DEBUG: Vertically contained: {len(contained)}")
    #print(f"DEBUG: Vertically contained: {len(contained)} contained={contained}")
    return contained


def get_contained_horizontally_using_ray_casting(g:grid.Grid2D, perimeter:set) -> set:
    contained = set()

    for h in range(g.get_height()):       
        is_within = False
        tmp = set()        
        for w in range(g.get_width()):            
            cp = point.Point2D(w, h)

            if cp in perimeter:
                pp = point.Point2D(w-1, h)
                if w == 0 or pp not in perimeter:
                    is_within = False if is_within else True # Toggle
                if w < g.get_width() - 1:
                    continue

            if is_within:
                tmp.add(cp)

            if (w < g.get_width() - 1 or False == is_within) and len(tmp) > 0:
                contained.update(tmp)

    print(f"DEBUG: Horizontally contained: {len(contained)}")
    #print(f"DEBUG: Horizontally contained: {len(contained)} contained={contained}")
    return contained


def count_contents(g:grid.Grid2D):
    count = 0
    for h in range(g.get_height()):
        perimeter = 0
        row_count = 0
        for x in range(g.get_width()):
            within_walls = perimeter%2 == 1

            cp = point.Point2D(x, h)
            s = g.get_symbol(cp)
            west = g.get_neighbour_west(cp)

            if not within_walls:
                west = g.get_neighbour_west(cp)
                if '#' == s and west and '.' == g.get_symbol(west):
                    perimeter += 1
            else: # within walls
                if '.' == s:
                    row_count += 1                
                elif '#' == s and west and '.' == g.get_symbol(west):
                    perimeter += 1
        if row_count > 0 and not within_walls:
            #print(f"DEBUG: row_count={row_count}")
            count+=row_count

    return count
"""
"""
def count_enclosed(g, path):
    #print("DEBUG: count_enclosed_ground_tiles")
    count = 0
    for c in range(g.get_height()):

        is_within = False
        tmp_count = 0
        for r in range(g.get_width()):
            p = point.Point2D(r, c)            
            if p in path:
                east = g.get_neighbour_point_east(p)
                if east and g.get_symbol(east) == '#' and east in path:
                    continue                
                is_within = False if is_within else True # Toggle
                if is_within == False:
                    count += tmp_count
                    tmp_count = 0
            elif is_within and '.' == g.get_symbol(p):                
                #print(f"DEBUG: {display_point(g, p)}")
                tmp_count += 1
    return count
"""
"""
def display_point(g, p):
    return g.get_symbol(p) + "(" + str(p.get_x()) + ", " + str(p.get_y()) + ") "


def count_enclosed(g, path):
    count = 0
    for c in range(g.get_height()):

        is_within = False
        tmp_count = 0
        for r in range(g.get_width()):
            p = point.Point2D(r, c)            
            if p in path:
                east = g.get_neighbour_point_east(p)
                if east and east in path:
                    #print(f"DEBUG: Perimeter point: {display_point(g, p)}")
                    continue                
                is_within = False if is_within else True # Toggle
                if is_within == False:
                    count += tmp_count
                    tmp_count = 0
            elif is_within:                
                #print(f"DEBUG: Within perimeter: {display_point(g, p)}")
                tmp_count += 1
    return count
"""


def count_contained_grid_squares(line):
    # Use ray casting approach from AOC 2023 Day 10 Part 2
    
    is_within = False

    line = line.replace('-', '')
    line = line.replace('S', '|') # TODO: Is this a valid assumption?
    line = line.replace('LJ', '||')
    line = line.replace('L7', '|')
    line = line.replace('FJ', '|')
    line = line.replace('F7', '||')
    #print(f"DEBUG: line={line}")
    wall_count = 0
    tmp_count = 0
    total_count = 0
    for i in range(len(line)):
        chr = line[i]
        if chr in '|':
            is_within = False if is_within else True
            wall_count += 1
            if wall_count % 2 == 0:
                total_count += tmp_count
                tmp_count = 0
        elif '.' == chr and i > 0 and is_within:
            tmp_count += 1
    return total_count

def grid_with_looping_path_from(lines, grid_size, path):
    # Create a grid using format from AOC 2023 Day 10
    g = grid.Grid2D(grid_size, grid_size)
    sp = point.Point2D(grid_size // 2, grid_size // 2)    

    cp = sp
    last_move = '?'

    #path = set()
    path.add(cp)
    last_move = '?'

    for l in lines:
        m,d,c = l.split()
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



def solve_part1(filename, grid_size=100):
    lines = fileutils.get_file_lines(filename)

    #print()
    #grid.display_grid(g)
    #print()

    path = set()
    g = grid_with_looping_path_from(lines, grid_size, path)

    lines = grid.grid_to_lines(g)
    ans = 0
    for l in lines:
        ans += count_contained_grid_squares(l)
    return len(path) + ans


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


def calculate_polygon_area_from(coords:list) -> float:
    # Calculate the area from the x axis between sequential coords for polygon corners
    if coords[0] != coords[-1]:
        # First and last item in the list are the same coordinates
        coords.append(coords[0]) 
    
    total_diff = 0
    length = len(coords)
    for i in range(length-1):        
        y_diff = coords[i+1][1] + coords[i][1]
        x_diff = coords[i+1][0] - coords[i][0]
        area_diff = y_diff * x_diff
        total_diff += area_diff
    return abs(total_diff / 2.0)

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    #instructions = []
    coords = []
    x = 0
    y = 0
    coords.append((x,y))
    distance = 0
    perimeter = 0
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
        perimeter += int(distance)

    #print(f"DEBUG: perimeter={perimeter}")
    #print(f"DEBUG: coords={coords}")

    area = int(calculate_polygon_area_from(coords))
    interior_points = int(area - (perimeter / 2) + 1)               
    return perimeter + interior_points

"""
#coords = [(1,1), (4,1), (4,4), (1,4), (1,1)]
#perimeter = 12
coords = [(0,0), (4,0), (4,5), (0,5), (0,0)]
perimeter = 14
area = calculate_polygon_area_from(coords)
interior = int(area - (perimeter/2)+1) 
size = perimeter + interior
print(f"DEBUG: size={size} area={area} perimeter={perimeter} interior={interior}")
"""