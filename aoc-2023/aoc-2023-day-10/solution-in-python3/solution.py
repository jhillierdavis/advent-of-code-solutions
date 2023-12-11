import sys
from collections import defaultdict

from helpers import fileutils, grid, point

def can_move_east(current, next):
    #print(f"DEBUG: current={current} next={next}")
    if current == next and current == 'S':
        return False
    if current in 'S-FL' and next in 'S-7J': # right -> right, down, up
        return True
    return False

def can_move_west(current, next):
    if current == next and current == 'S':
        return False
    if current in 'S-7J' and next in 'S-FL': # left -> left, up, down
        return True
    return False


def can_move_south(current, next):
    if current == next and current == 'S':
        return False
    if current in 'S|7F' and next in 'S|JL': # down -> down, right, left
        return True
    return False

def can_move_north(current, next):
    if current == next and current == 'S':
        return False
    if current in 'S|JL' and next in 'S|7F': # up -> up, right, left
        return True
    return False


def has_valid_neighbours(g, p, s):
    count = 0
    east = g.get_neighbour_point_east(p)
    if east and can_move_east(s, g.get_symbol(east)):
        count += 1

    west = g.get_neighbour_point_west(p)
    if west and can_move_west(s, g.get_symbol(west)):
        count += 1

    north = g.get_neighbour_point_north(p)
    if north and can_move_north(s, g.get_symbol(north)):
        count += 1

    south = g.get_neighbour_point_south(p)
    if south and can_move_south(s, g.get_symbol(south)):
        count += 1

    return True if count > 1 else False


def remove_invalid_pipes(g):
    modifications = 0
    for r in range(g.get_width()):
        for c in range(g.get_height()):

            p = point.Point2D(r,c)
            s = g.get_symbol(p)

            #print(f"DEBUG: p={p} s={s}")
            if not has_valid_neighbours(g,p,s):
                g.set_symbol(p, '.')    
                modifications += 1

    return g


def show_grid(g):
    for c in range(g.get_height()):
        v = ""
        for r in range(g.get_width()):
            p = point.Point2D(r,c)
            s = g.get_symbol(p)
            v += s
        print(v)
    print()



def get_cleansed_grid(filename, max=0):
    lines = fileutils.get_file_lines(filename)


    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    #show_grid(g)

    for i in range(0,max):
        remove_invalid_pipes(g)
    #show_grid(g)
    return g

def get_starting_position_from_grid(g):  
    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            if g.get_symbol(p) == 'S':
                return p

    raise ValueError("No starting point 'S' in grid={g}!")

def get_pipe_points(g, cp, lp=None):
    pipe_points = []
    cps = g.get_symbol(cp)

    east = g.get_neighbour_point_east(cp)
    if east and can_move_east(cps, g.get_symbol(east)):
        #print(f"DEBUG: {display_point(g, cp)} -> east={display_point(g, east)}")
        pipe_points.append(east)
    
    north = g.get_neighbour_point_north(cp)
    if north and can_move_north(cps, g.get_symbol(north)):
        #print(f"DEBUG: {display_point(g, cp)} -> north={display_point(g, north)}")
        pipe_points.append(north)

    south = g.get_neighbour_point_south(cp)
    if south and can_move_south(cps, g.get_symbol(south)):
        #print(f"DEBUG: {display_point(g, cp)} -> south={display_point(g, south)}")
        pipe_points.append(south)

    west = g.get_neighbour_point_west(cp)
    if west and can_move_west(cps, g.get_symbol(west)):
        #print(f"DEBUG: {display_point(g, cp)} -> west={display_point(g, west)}")
        pipe_points.append(west)

    if lp:
        pipe_points.remove(lp)
    return pipe_points

def display_point(g, p):
    return g.get_symbol(p) + "(" + str(p.get_x()) + ", " + str(p.get_y()) + ") "

def display_pipe_points(g, pipe_points):
    line = ""
    for pp in pipe_points:
        line += display_point(g, pp) + " "

    print(line)
    

def get_loop_path_length(g, sp):
    next_pipes = get_pipe_points(g, sp)
    #display_pipe_points(g, next_pipes)
    np = next_pipes[0]
    
    count = 1
    while g.get_symbol(np) != 'S':
        next_pipes = get_pipe_points(g, np, sp)
        #display_pipe_points(g, next_pipes)
        sp = np
        np = next_pipes[0]
        count += 1

    return count

def get_loop_path(g, sp):
    path = [sp]

    next_pipes = get_pipe_points(g, sp)
    #display_pipe_points(g, next_pipes)
    np = next_pipes[0]
    
    
    while g.get_symbol(np) != 'S':
        next_pipes = get_pipe_points(g, np, sp)
        #display_pipe_points(g, next_pipes)
        sp = np
        np = next_pipes[0]
        path.append(np)

    return path

def solve_part1(filename):
    g = get_cleansed_grid(filename)
    sp = get_starting_position_from_grid(g)    
    length = get_loop_path_length(g, sp)
    return length // 2

def count_enclosed_ground_tiles(g, path):
    #print("DEBUG: count_enclosed_ground_tiles")
    count = 0
    for c in range(g.get_height()):

        is_within = False
        tmp_count = 0
        for r in range(g.get_width()):
            p = point.Point2D(r, c)            
            if p in path:
                east = g.get_neighbour_point_east(p)
                if east and east in path and g.get_symbol(east) in '-7J':
                    continue                
                is_within = False if is_within else True # Toggle
                if is_within == False:
                    count += tmp_count
                    tmp_count = 0
            elif is_within and '.' == g.get_symbol(p):                
                #print(f"DEBUG: {display_point(g, p)}")
                tmp_count += 1
    return count


def solve_part2(filename):
    g = get_cleansed_grid(filename, 3)
    sp = get_starting_position_from_grid(g)    
    path = get_loop_path(g, sp)
    show_grid(g)
    return count_enclosed_ground_tiles(g, path)
