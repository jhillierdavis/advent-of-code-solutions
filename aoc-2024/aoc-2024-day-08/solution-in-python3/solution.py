from helpers import fileutils, grid, point

from collections import defaultdict

import string

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


def is_valid_antinode_position(g, p, k):
    return g.contains(p) and g.get_symbol(p) != k
        

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    # Find antenane position points for each antenane types in grid
    antennae_map = get_antennae_type_to_position_map(g)

    # For each antenane type point, find distance to next and mark antinodes
    #print(f'DEBUG: antennae_map={antennae_map}')
    count = 0
    g_ans = g.clone()
    for k in antennae_map.keys():
        v = antennae_map[k]
        size = len(v)
        if size <= 1:
            continue
        
        #print(f'DEBUG: k={k} v={v} size={size}')
        
        for i in range(size):
            current = list(v)[i]
            for j in range(i+1,):
                next = list(v)[j]
                if current == next:
                    continue
                
                x_offset = current.get_x() - next.get_x()
                y_offset = current.get_y() - next.get_y()

                #print(f"DEBUG: compare {current} with {next} :  {x_offset} {y_offset}")
                next_ap = point.Point2D(current.get_x() + x_offset, current.get_y() + y_offset)
                if is_valid_antinode_position(g, next_ap, k):
                    g_ans.set_symbol(next_ap, '#')
                    count += 1

                next_ap = point.Point2D(current.get_x() - x_offset, current.get_y() - y_offset)
                if is_valid_antinode_position(g, next_ap, k):
                    g_ans.set_symbol(next_ap, '#')
                    count += 1

                next_ap = point.Point2D(next.get_x() + x_offset, next.get_y() + y_offset)
                if is_valid_antinode_position(g, next_ap, k):
                    g_ans.set_symbol(next_ap, '#')
                    count += 1

                next_ap = point.Point2D(next.get_x() - x_offset, next.get_y() - y_offset)
                if is_valid_antinode_position(g, next_ap, k):
                    g_ans.set_symbol(next_ap, '#')
                    count += 1

    #grid.display_grid(g_ans)
    return g_ans.count_symbol('#')
    #return count

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    # Find antenane position points for each antenane types in grid
    antennae_map = get_antennae_type_to_position_map(g)

    # For each antenane type point, find distance to next and mark antinodes
    #print(f'DEBUG: antennae_map={antennae_map}')
    count = 0
    g_ans = g.clone()
    for k in antennae_map.keys():
        v = antennae_map[k]
        size = len(v)
        if size <= 1:
            continue
        
        #print(f'DEBUG: k={k} v={v} size={size}')
        
        for i in range(size):
            current = list(v)[i]
            for j in range(i+1,):
                next = list(v)[j]
                if current == next:
                    continue
                
                x_initial_offset = current.get_x() - next.get_x()
                y_intial_offset = current.get_y() - next.get_y()

                #print(f"DEBUG: compare {current} with {next} :  {x_offset} {y_offset}")
                for z in range(1,g.get_height()):
                    x_offset = z * x_initial_offset
                    y_offset = z * y_intial_offset

                    next_ap = point.Point2D(current.get_x() + x_offset, current.get_y() + y_offset)
                    if g.contains(next_ap):
                        g_ans.set_symbol(next_ap, '#')
                        count += 1

                    next_ap = point.Point2D(current.get_x() - x_offset, current.get_y() - y_offset)
                    if g.contains(next_ap):
                        g_ans.set_symbol(next_ap, '#')
                        count += 1

                    next_ap = point.Point2D(next.get_x() + x_offset, next.get_y() + y_offset)
                    if g.contains(next_ap):
                        g_ans.set_symbol(next_ap, '#')
                        count += 1

                    next_ap = point.Point2D(next.get_x() - x_offset, next.get_y() - y_offset)
                    if g.contains(next_ap):
                        g_ans.set_symbol(next_ap, '#')
                        count += 1

    #grid.display_grid(g_ans)
    return g_ans.count_symbol('#')
