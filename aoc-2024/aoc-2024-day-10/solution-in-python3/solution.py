import string
from helpers import fileutils, grid, point

symbol_trailhead = '0'
symbol_trailend = '9'
symbol_marker = 'X'


def get_grid_from(filename:str) -> grid.Grid2D:
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    return g


def get_value(g:grid.Grid2D, p:point.Point2D):
    s = g.get_symbol(p)
    if s in string.digits:   
        return int(s)
    return -1


def is_trailhead(g:grid.Grid2D, cp:point.Point2D):
    cv = get_value(g, cp)
    return cv == 0


def is_trailend(g:grid.Grid2D, cp:point.Point2D):
    cv = get_value(g, cp)
    return cv == 9


def get_step_size(g:grid.Grid2D, cp:point.Point2D, np:point.Point2D):
    cv = get_value(g, cp)
    nv = get_value(g, np)
    return cv - nv


def is_stepdown(g:grid.Grid2D, cp:point.Point2D, np:point.Point2D) -> bool:
    return get_step_size(g, cp, np) == 1


def is_stepup(g:grid.Grid2D, cp:point.Point2D, np:point.Point2D) -> bool:
    return get_step_size(g, cp, np) == -1


def mark_trailheads(g:grid.Grid2D, cp:point.Point2D) -> None:
    neighbours = g.get_cardinal_point_neighbours(cp)
    for np in neighbours:
        if is_stepdown(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailhead(g, np):        
                #print(f"DBEUG: End: np={np}")
                g.set_symbol(np, symbol_marker)            
            else:
                mark_trailheads(g, np)

def populate_with_unique_trailheads(g:grid.Grid2D, cp:point.Point2D, trailheads:set) -> None:
    neighbours = g.get_cardinal_point_neighbours(cp)
    for np in neighbours:
        if is_stepdown(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailhead(g, np):        
                #print(f"DBEUG: End: np={np}")
                trailheads.add(np)           
            else:
                populate_with_unique_trailheads(g, np, trailheads)


def count_trailends(g:grid.Grid2D, cp:point.Point2D) -> int:    
    count = 0
    neighbours = g.get_cardinal_point_neighbours(cp)    
    for np in neighbours:
        if is_stepup(g, cp, np):
            #print(f"DBEUG: Step: cv={cv} nv={nv} cp={cp} np={np}")
            if is_trailend(g, np):        
                count += 1
            else:
                count += count_trailends(g, np)
    return count


def solve_part1(filename:str) -> int:
    g = get_grid_from(filename)

    end_points = g.get_matching_symbol_coords(symbol_trailend)

    count = 0    
    for ep in end_points:
        # For each ending location (trailend) count the unique starting locations (trailheads)
        gc = g.clone()
        mark_trailheads(gc, ep)
        count += gc.count_symbol(symbol_marker)
    return count


def solve_part1_alternative(filename:str) -> int:
    g = get_grid_from(filename)

    end_points = g.get_matching_symbol_coords(symbol_trailend)

    count = 0    
    for ep in end_points:
        trailheads = set()
        populate_with_unique_trailheads(g, ep, trailheads)
        count += len(trailheads)
    return count


def solve_part2(filename:str) -> int:
    g = get_grid_from(filename)
    
    start_points = g.get_matching_symbol_coords(symbol_trailhead)

    count = 0
    for sp in start_points:
        # For each starting location (trailhead) count up all the paths to the ending locations (trailends)
        count += count_trailends(g, sp)
    return count