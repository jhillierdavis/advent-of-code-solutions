# Shared helper libraries
from helpers import fileutils, point, grid

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_initial_active_set_from_file(filename:str) -> set[point.Point3D]:
    lines = fileutils.get_file_lines_from(filename)

    initial_grid_at_z0 = grid.lines_to_grid(lines)

    grid.display_grid(initial_grid_at_z0)

    active_set = set()
    for h in range(initial_grid_at_z0.get_height()):
        for w in range(initial_grid_at_z0.get_width()):
            p2d = point.Point2D(w, h)
            s =  initial_grid_at_z0.get_symbol(p2d)
            if s == '#':
                p3d = point.Point3D(w, h, 0)
                active_set.add(p3d)
    return active_set


def get_active_neighbours(a, active_set):
    neighbours = a.get_closest_neighbours()    
    return neighbours.intersection(active_set)


def get_inactive_neighbours(a, active_neighbour_set):
    neighbours = a.get_closest_neighbours()   
    return neighbours.difference(active_neighbour_set)


def evolve_active_set(active_set:set) -> set:
    next_active_set = set()

    for a in active_set:
        active_neighbours = get_active_neighbours(a, active_set)

        if a not in next_active_set:            
            active_neighbour_count = len(active_neighbours)
            if active_neighbour_count == 2 or active_neighbour_count == 3:
                # Remains active
                next_active_set.add(a)
        
        inactive_neighbours = get_inactive_neighbours(a, active_neighbours)
        for i in inactive_neighbours:
            active_neighbours = get_active_neighbours(i, active_set)
            active_neighbour_count = len(active_neighbours)
            if active_neighbour_count == 3:
                # Becomes active
                next_active_set.add(i)
    
    return next_active_set


def solve_part1(filename:str, cycles:int) -> int:
    active_set = get_initial_active_set_from_file(filename)            

    for _ in range(cycles):
        active_set = evolve_active_set(active_set)

    active_count = len(active_set)
    return active_count


def get_initial_active_hypercube_set_from_file(filename:str) -> set[point.Point4D]:
    active_set = get_initial_active_set_from_file(filename)

    active_4d_set = set()
    for a in active_set:
        p4d = point.Point4D(a.get_x(), a.get_y(), a.get_z(), 0)
        active_4d_set.add(p4d)
    
    return active_4d_set


def solve_part2(filename:str, cycles:int) -> int:
    active_set = get_initial_active_hypercube_set_from_file(filename)

    for _ in range(cycles):
        active_set = evolve_active_set(active_set)

    active_count = len(active_set)
    return active_count
