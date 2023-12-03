from helpers import fileutils, grid, point

from collections import defaultdict

def check_value_touches_a_symbol(g, p, value):
    #print(f"DBEUG: value={value} point={p}")
    
    for i in range(len(value)):
        np = point.Point2D(p.get_x() + i, p.get_y())       
        #print(f"DBEUG: checking point={np} i={i}" ) 
        if touches_a_symbol(g,np):
            return True
    return False


def touches_a_symbol(g, p):
    neighbours = g.get_surrounding_neighbours(p)  
    for np in neighbours:
        s  = g.get_symbol(np)                
        #print(f"DBEUG: point={p} symbol={s}")
        if not s.isnumeric() and not s == '.':
            return True
    return False


def extract_number(g, p):
    value = g.get_symbol(p)

    neighbours = g.get_surrounding_neighbours(p)  
    
    next_p = point.Point2D(p.get_x() + 1, p.get_y())
    if next_p in neighbours:
        next_v = g.get_symbol(next_p)
        if next_v.isnumeric():          
            return value + extract_number(g, next_p)
    return value


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    #assert g.get_symbol(point.Point2D(3,4)) == '*'
    
    total = 0
    for y in range(g.get_height()):
        skip = 0
        for x in range(g.get_width()):
            if skip > 0:
                skip -= 1
                continue

            p = point.Point2D(x,y)

            symbol = g.get_symbol(p)
            if symbol.isnumeric():
                value =  extract_number(g,p)
                #print(f"DEBUG: value={value}")  
                skip = len(value) -1
                if value and check_value_touches_a_symbol(g, p, value):
                    #print(f"DEBUG: value={value} touches symbol")    
                    total += int(value)                       
                #number_points.append(p)

    return total


def solve_part2(filename):
    return 0