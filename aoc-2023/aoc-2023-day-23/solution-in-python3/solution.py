import sys
from copy import deepcopy
from collections import defaultdict

from helpers import fileutils, grid, point

sys.setrecursionlimit(10000) # Allow greater recursion depth (than the 1K default)!


def is_valid(g, p, lp, permitted):
    if not p:
        return False
    
    if p == lp:
        return False

    s = g.get_symbol(p)
    if not (s == '.' or s == permitted):
        return False
    
    return True


def hike(g, cp, ep, steps, lp, results):
    if cp == ep:
        print(f"DEBUG: steps={steps}")
        results.add(steps)
        return steps
    
    n = g.get_neighbour_north(cp)
    if is_valid(g, n, lp, '^'):
        hike(g, n, ep, 1 + steps, cp, results)


    n = g.get_neighbour_south(cp)
    if is_valid(g, n, lp, 'v'):
        hike(g, n, ep, 1 + steps, cp, results)


    n = g.get_neighbour_east(cp)
    if is_valid(g, n, lp, '>'):
        hike(g, n, ep, 1 + steps, cp, results)

    n = g.get_neighbour_west(cp)
    if is_valid(g, n, lp, '<'):
        hike(g, n, ep, 1 + steps, cp, results)


"""
def get_first_symbol_point_in_row(g, target_symbol, row_index):
    for c in range(g.get_width()):
        p = point.Point2D(c, row_index)
        s = g.get_symbol(p)
        if s == target_symbol:
            return p
    return None
"""

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = get_first_symbol_point_in_row(g, '.', 0)
    ep = get_first_symbol_point_in_row(g, '.', g.get_height() - 1)
    #print(f"DEBUG: sp={sp} ep={ep}")

    
    results = set()
    #visited = set()
    #hike(g, sp, ep, 0, visited, results)
    hike(g, sp, ep, 0, sp, results)
    return max(results)

"""

def hike_including_slopes(g:grid.Grid2D, cp, ep, steps, visited, walls, results):
    if cp == ep:
        print(f"DEBUG: steps={steps}")
        results.add(steps)
        return steps
    
    visited.add(cp)
    neighbours = g.get_cardinal_point_neighbours(cp)
    
    choices = set()
    for n in neighbours:
        if n in visited or n in walls: # Avoid retreating or assessing known walls
            continue

        s = g.get_symbol(n)        
        if s == '#': # Ignore walls
            walls.add(n)
            continue

        choices.add(n)

    num_choices = len(choices)
    for c in choices:
        if num_choices == 1:
            v = visited       
        else:
            v = deepcopy(visited)        
        hike_including_slopes(g, c, ep, 1 + steps, v, walls, results)

#def find_next_choice(g, cp, lp, ep):
#    neighbours = g.get_cardinal_point_neighbours(cp)
#    neighbours_count =

decision_points_map = {}

def find_choice_points(g, cp, ep, visited, walls, last_dp, steps=0, total_steps=0):
    if cp == ep:
        #print(f"DEBUG: total_steps={total_steps}")
        if not last_dp in decision_points_map.keys():
            decision_points_map[last_dp] = set()
        decision_points_map[last_dp].add((ep, steps))
        return
    
    visited.add(cp)
    neighbours = g.get_cardinal_point_neighbours(cp)
    
    choices = set()
    for n in neighbours:
        if n in visited or n in walls: # Avoid retreating or assessing known walls
            continue

        s = g.get_symbol(n)        
        if s == '#': # Ignore walls
            walls.add(n)
            continue

        choices.add(n)

    num_choices = len(choices)
    if num_choices == 1:
        c = choices.pop()
        find_choice_points(g, c, ep, visited, walls, last_dp, 1 + steps, 1 + total_steps)
    elif num_choices > 1:                
        for c in choices:
            #print(f"DEBUG: last_cp={last_dp} -> cp={cp} {steps}")
            if not last_dp in decision_points_map.keys():
                decision_points_map[last_dp] = set()
            decision_points_map[last_dp].add((cp, steps))
            find_choice_points(g, c, ep, visited, walls, cp, 1, 1 + total_steps)



def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = get_first_symbol_point_in_row(g, '.', 0)
    ep = get_first_symbol_point_in_row(g, '.', g.get_height() - 1)
    #print(f"DEBUG: sp={sp} ep={ep}")

    
    results = set()
    visited = set()
    walls = set()
    #hike(g, sp, ep, 0, visited, results)
    hike_including_slopes(g, sp, ep, 0, visited, walls, results)
    return max(results)


def count_paths(children, ep):

    i = set()
    for child in children:
        if child in decision_points_map.keys():
            entries = decision_points_map[child]
            for e in entries:        
                coord = e[0]
                steps = e[1]
                if coord == ep:
                    print(f"DEBUG: At {ep} after {steps}")
                else:
                    print(f"{child} -> {coord}")
                    i.add(coord)

    if len(i) > 0:
        count_paths(i, ep)
            

def explore_paths(path, ep, steps:int = 0):
    p = path[-1]
    if p == ep:
        print(f"DEBUG: steps={steps} path={path}")    
        return

    if not p in decision_points_map.keys():
        print(f"DEBUG: Missing p={p}")
    else:
        options = decision_points_map[p]
        for o in options:   
            coords = o[0]             
            if not coords in path:
                new_path = deepcopy(path)
                new_path.append(coords)
                explore_paths(new_path, ep, steps + o[1])



def foo(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = get_first_symbol_point_in_row(g, '.', 0)
    ep = get_first_symbol_point_in_row(g, '.', g.get_height() - 1)
    print(f"DEBUG: sp={sp} ep={ep}")
    
    visited = set()
    walls = set()
    find_choice_points(g, sp, ep, visited, walls, sp)
    print(f"DEBUG: decision_points_map={decision_points_map}")

    #children = set()
    #children.add(sp)
    #count_paths(children, ep)
    explore_paths([sp], ep)
    
foo('puzzle-input-example.txt')
#foo('puzzle-input-full.txt')
"""

def get_first_symbol_point_in_row(g, target_symbol, row_index):
    for c in range(g.get_width()):
        p = point.Point2D(c, row_index)
        s = g.get_symbol(p)
        if s == target_symbol:
            return p
    return None

def get_path_neighbours(g, p):
    neighbours = g.get_cardinal_point_neighbours(p)
    valid = set()
    for n in neighbours:
        ns = g.get_symbol(n)
        if ns != '#':
            valid.add(n)
    return valid


def get_decision_points(g):
    decision_points = set()

    for r in range(g.get_height()-1):
        for c in range(g.get_width()-1):
            p = point.Point2D(c,r)
            s = g.get_symbol(p)
            if '#' == s:
                continue

            path_neighbours = get_path_neighbours(g, p)        
            count = len(path_neighbours)
            if count > 2:
                decision_points.add(p)
    return decision_points

def get_distance(g, decision_points, start, ignore_point=None):
    #print(f"DEBUG: get_distance() start={start} ignore_point={ignore_point}")
    visited = set()
    if ignore_point:
        visited.add(ignore_point)
    current = start
    steps = 0

    while current not in decision_points:
        visited.add(current)
        #print(f"DEBUG: get_distance(): current={current}")
        neighbours = get_path_neighbours(g, current)

        count = len(neighbours)
        if count != 2:
            break

        for n in neighbours:
            if n in visited:
                continue
            else:
                steps += 1
                current = n
                break
    return current, 1 + steps




                    
def get_adjacent_distances_to_next_decision_point(g, decision_points, source):
    path_neighbours = get_path_neighbours(g, source) 
    count = len(path_neighbours)
    assert count > 2

    for pn in path_neighbours:
        next, steps = get_distance(g, decision_points, pn)
        print(f"DEBUG: {steps} {source} -> {next}")


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = get_first_symbol_point_in_row(g, '.', 0)
    ep = get_first_symbol_point_in_row(g, '.', g.get_height() - 1)
    print(f"DEBUG: sp={sp} ep={ep}")

    decision_points = get_decision_points(g)
    #print(f"DEBUG: {len(decision_points)} decision_points={decision_points}")

    #for dp in decision_points:
    #    get_adjacent_distances_to_next_decision_point(g, decision_points, dp)
    
    
    """
    visited = set()
    walls = set()
    find_choice_points(g, sp, ep, visited, walls, sp)
    print(f"DEBUG: decision_points_map={decision_points_map}")

    #children = set()
    #children.add(sp)
    #count_paths(children, ep)
    explore_paths([sp], ep)
    """

    distance_map = defaultdict(int)
    spurs = get_path_neighbours(g, sp)
    distance_map[sp] = [ get_distance(g, decision_points, spurs.pop(), sp) ]
    spurs = get_path_neighbours(g, ep)
    distance_map[ep] = [ get_distance(g, decision_points, spurs.pop(), ep) ]

    for dp in decision_points:
        spurs = get_path_neighbours(g, dp)
        values = []
        for s in spurs:
            #print(f"DEBUG: dp={dp} spur={s}")            
            values.append( get_distance(g, decision_points, s, dp) )
        distance_map[dp] = values
    #print(f"DEBUG: distance_map={distance_map}")
            
    visited = set()
    values = set()
    get_next(distance_map, sp, visited, ep, values)
    return max(values)


def get_next(distance_map, current, visited, target, values, count=0):
    if current == target:
        #print(f"DEBUG: current={current} count={count}")
        values.add(count)
        return

    entries = distance_map[current]
    visited.add(current)
    for e in entries:
        next = e[0]
        if next in visited:
            #print(f"DEBUG: Already visited={next}")
            continue
        steps = e[1]
        get_next(distance_map, next, deepcopy(visited), target, values, count + steps)