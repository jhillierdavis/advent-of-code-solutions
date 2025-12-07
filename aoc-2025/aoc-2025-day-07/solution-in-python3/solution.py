# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_all_beam_paths_as_display_lines_from_file(filename):
    g = create_grid_from_file(filename)
    calculate_beam_split_count(g)
    return grid.grid_to_lines(g)


def create_grid_from_file(filename):
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    return g


def get_starting_point(g):
    start_points = g.get_points_matching('S')
    assert len(start_points) == 1

    return start_points.pop()


def get_splitter_points(g):
    sps = g.get_points_matching('^')
    assert len(sps) > 0
    #logger.debug(f"Splitter points: sps={sps}")
    #logger.debug(f"Splitters size: {len(sps)}")
    return sps   


def calculate_beam_split_count(g):
    sp = get_starting_point(g)
    #logger.debug(f"Current point: cp={cp}")
    #g.set_symbol(sp, '|')

    splitters = get_splitter_points(g)

    height = g.get_height()    
    beams = {sp}

    split_count = 0
    for h in range(height-1):
        next_beams = set()
        for bp in beams:
            x = bp.get_x()
            y = bp.get_y() 

            np = point.Point2D(x,y+1)
            if np in splitters:
                npe = g.get_neighbour_east(np)
                if npe:
                    g.set_symbol(npe, '|')
                    next_beams.add(npe)
                npw = g.get_neighbour_west(np)
                if npw:
                    g.set_symbol(npw, '|')
                    next_beams.add(npw)
                split_count += 1
            else:
                g.set_symbol(np, '|')
                next_beams.add(np)
        
        beams = next_beams     
        #logger.debug(f"h={h} beams={beams}")       

    #print()
    #grid.display_grid(g)

    return split_count


def solve_part1(filename):
    g = create_grid_from_file(filename)
    return calculate_beam_split_count(g)


def is_splitter_point(g, p):    
    s = g.get_symbol(p)
    return True if s == '^' else False


def solve_part2(filename):
    from collections import defaultdict

    g = create_grid_from_file(filename)

    sp = get_starting_point(g)

    particle_row_map = dict()
    particle_row_map[sp.get_x()] = 1 # Single initial particle (& timeline)

    for y in range(1, g.get_height()):
        next_row_particles_map = defaultdict(int)

        for x in particle_row_map.keys():
            current_x_of_p = particle_row_map[x]

            pp = point.Point2D(x, y)
            if is_splitter_point(g, pp):
                # Split right (if within grid)
                npe = g.get_neighbour_east(pp)                
                if npe:
                    next_row_particles_map[npe.get_x()] += current_x_of_p

                # Split left (if within grid)
                npw = g.get_neighbour_west(pp)
                if npw:
                    next_row_particles_map[npw.get_x()] += current_x_of_p

            else:
                next_row_particles_map[x] += current_x_of_p

        particle_row_map = next_row_particles_map


    total_particles_at_last_row = sum(particle_row_map.values())
    ordered_particle_x_location_map = dict(sorted(particle_row_map.items()))
    logger.debug(f"total_particles_at_last_row={total_particles_at_last_row} ordered_particle_x_location_map={ordered_particle_x_location_map}")
    
    return total_particles_at_last_row # Equals number of timelines (of possible paths)