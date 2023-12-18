from collections import defaultdict

from helpers import fileutils, grid, point

def count_contents(g:grid.Grid2D):
    count = 0
    for h in range(g.get_height()):
        perimeter = 0
        row_count = 0
        for x in range(g.get_width()):
            within_walls = perimeter%2 == 1

            cp = point.Point2D(x, h)
            s = g.get_symbol(cp)

            if not within_walls:
                if '#' == s and '.' == g.get_symbol(g.get_neighbour_west(cp)):
                    perimeter += 1
            else: # within walls
                if '.' == s:
                    row_count += 1                
                elif '#' == s and '.' == g.get_symbol(g.get_neighbour_west(cp)):
                    perimeter += 1
        if row_count > 0 and not within_walls:
            #print(f"DEBUG: row_count={row_count}")
            count+=row_count

    return count
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
                    continue                
                is_within = False if is_within else True # Toggle
                if is_within == False:
                    count += tmp_count
                    tmp_count = 0
            elif is_within:                
                #print(f"DEBUG: {display_point(g, p)}")
                tmp_count += 1
    return count

        


def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.Grid2D(500, 500)
    cp = point.Point2D(200,400)
    g.set_symbol(cp, '#')

    path = set()
    path.add(cp)

    for l in lines:
        m,d,c = l.split()
        d = int(d)
        print(f"DEBUG: m={m} d={d}, c={c} l={l} cp={cp}")
        for _ in range(d):
            if m == 'R':            
                cp = point.Point2D(cp.get_x()+1, cp.get_y())
            elif m == 'L':
                cp = point.Point2D(cp.get_x()-1, cp.get_y())
            elif m == 'D':
                cp = point.Point2D(cp.get_x(), cp.get_y()+1)
            elif m == 'U':
                cp = point.Point2D(cp.get_x(), cp.get_y()-1)
            g.set_symbol(cp, '#')
            path.add(cp)

    #print()
    #grid.display_grid(g)
    #print()

    perimeter_count = g.count_symbol('#')
    assert perimeter_count == len(path), f"perimeter_count={perimeter_count} path_length={len(path)}"
    #content_count = count_contents(g)
    content_count = count_enclosed(g, path)
    print(f"DEBUG: perimeter_count={perimeter_count} content_count={content_count}")

    return perimeter_count + content_count

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

