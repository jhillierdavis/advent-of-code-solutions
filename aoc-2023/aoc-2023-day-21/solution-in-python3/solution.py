from collections import defaultdict, deque

from helpers import fileutils, grid



def count_neighbours(g, cp):
    #print(f"DEBUG: cp={cp}")
    neighbours = g.get_cardinal_point_neighbours(cp)
    #print(f"DEBUG: neighbours={neighbours}")

    count = 0
    for n in neighbours:
        if g.get_symbol(n) != '#':
            count += 1
    return count

def get_cardinal_point_neighbours_at_distance(g, cp, d, coords, visited):
    #print(f"DEBUG: d={d} {cp}")
    if d == 0:
        coords.add(cp)
        return
    
    neighbours = g.get_cardinal_point_neighbours(cp)
    for n in neighbours:
        if (n,d) in visited:
            continue
        else:
            visited.add((n,d))

        if g.get_symbol(n) != '#':    
            #coords.add(n)        
            get_cardinal_point_neighbours_at_distance(g, n, d -1, coords, visited)            
    return
        
    


def solve_part1(filename, steps):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    matches = g.get_matching_symbol_coords('S')
    cp = matches[0]
#    print(f"DEBUG: cp={cp}")
#    neighbours = g.get_cardinal_point_neighbours(cp)
#    print(f"DEBUG: neighbours={neighbours}")

 
#    for n in neighbours:
#        if g.get_symbol(n) != '#':
#            count += 1
    
    coords = set()
    visited = set()
    get_cardinal_point_neighbours_at_distance(g, cp, steps, coords, visited)
    print(f"DEBUG: coords={coords}")
    count = len(coords)
    return count


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

