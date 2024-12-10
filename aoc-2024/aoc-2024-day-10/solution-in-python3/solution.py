import string
from helpers import fileutils, grid

"""
def get_trailhead_paths(g, cp, value)
    cp = int(g.get_symbol(cp))
    neighbours = g.get_cardinal_point_neighbours(cp)
    for np in neighbours: 
        nv = int(g.get_symbol(cp))        
        if nv == cp + 1:            
"""

ans = 0
def count_trailhead_paths(g, sp):
    global ans
    sv = int(g.get_symbol(sp))

    if sv == 9:
        ans += 1
        return

    neighbours = g.get_cardinal_point_neighbours(sp)
    for np in neighbours:
        
        nv = int(g.get_symbol(np))        

        if nv == sv + 1:     
            count_trailhead_paths(g, np)
    return

def get_grid_from(filename):
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    return g


def count_starting_points_from(g):
    starting_points = g.get_matching_symbol_coords('0')
    return len(starting_points)

def get_value(g, p):
    s = g.get_symbol(p)
    if s in string.digits:   
        return int(s)
    return -1


def is_trailhead_step(g, cp, np):
    cv = get_value(g, cp)
    nv = get_value(g, np)
    return nv - cv == 1
        
def is_trailhead_end(g, cp):
    cv = get_value(g, cp)
    return cv == 9

def count_trailhead_paths(g, cp):
    

    count = 0
    neighbours = g.get_cardinal_point_neighbours(cp)
    for np in neighbours:
        if is_trailhead_step(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailhead_end(g, np):        
                #print(f"DBEUG: End: np={np}")
                g.set_symbol(np, 'X')            
            else:
                count += count_trailhead_paths(g, np)
    return count            
    
        
def count_trailheads_from(g):
    starting_points = g.get_matching_symbol_coords('0')

    count = 0
    for sp in starting_points:   
        print(f"DEBUG: Start sp={sp}")     
        count += count_trailhead_paths(g, sp)
    

    #grid.display_grid(g)
    return g.count_symbol('X')


def count_trailheads_startpoints(g):
    end_points = g.get_matching_symbol_coords('0')

    count = 0
    for sp in end_points:   
        count += count_trailhead_paths(g, sp)
    return g.count_symbol('X')

def is_stepdown(g, cp, np):
    cv = get_value(g, cp)
    nv = get_value(g, np)
    return cv - nv == 1
        
def is_trailhead_start(g, cp):
    cv = get_value(g, cp)
    return cv == 0

def find_trailheads(g, cp):    
    neighbours = g.get_cardinal_point_neighbours(cp)
    for np in neighbours:
        if is_stepdown(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailhead_start(g, np):        
                #print(f"DBEUG: End: np={np}")
                g.set_symbol(np, 'X')            
            else:
                find_trailheads(g, np)

def solve_part1(filename):
    g = get_grid_from(filename)
    
    end_points = g.get_matching_symbol_coords('9')

    count = 0
    for ep in end_points:
        gc = g.clone()
        find_trailheads(gc, ep)
        count += gc.count_symbol('X')
    return count

def is_stepup(g, cp, np):
    cv = get_value(g, cp)
    nv = get_value(g, np)
    return nv - cv == 1
        
def is_trailend(g, cp):
    cv = get_value(g, cp)
    return cv == 9


def find_trailend(g, cp):    
    count = 0
    neighbours = g.get_cardinal_point_neighbours(cp)    
    for np in neighbours:
        if is_stepup(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailend(g, np):        
                count += 1
            else:
                count += find_trailend(g, np)
    return count


def solve_part2(filename):
    g = get_grid_from(filename)
    
    start_points = g.get_matching_symbol_coords('0')

    count = 0
    for sp in start_points:
        count += find_trailend(g, sp)
    return count