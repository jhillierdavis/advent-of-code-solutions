# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_all_beam_paths_as_display_lines_from_file(filename:str) -> list[str]:
    g = create_grid_from_file(filename)
    calculate_beam_split_count(g)
    return grid.grid_to_lines(g)


def create_grid_from_file(filename:str) -> grid.Grid2D:
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    return g


def get_starting_point(g:grid.Grid2D) -> point.Point2D:
    start_points = g.get_points_matching('S')
    assert len(start_points) == 1,f"Unexpected starting points: {start_points}"

    return start_points.pop()


def get_splitter_points(g:grid.Grid2D) -> set[point.Point2D]:
    sps = g.get_points_matching('^')
    assert len(sps) > 0
    #logger.debug(f"Splitter points: sps={sps}")
    #logger.debug(f"Splitters size: {len(sps)}")
    return sps   


def calculate_beam_split_count(g:grid.Grid2D) -> int:
    sp = get_starting_point(g)

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
        logger.debug(f"h={h} beams={beams}")       

    #print()
    #grid.display_grid(g)

    return split_count


def solve_part1(filename:str) -> int:
    g = create_grid_from_file(filename)
    return calculate_beam_split_count(g)


def is_splitter_point(g:grid.Grid2D, p:point.Point2D) -> bool:
    s = g.get_symbol(p)
    return True if s == '^' else False


def solve_part2_using_wave_front_approach(filename:str) -> int:
    """
    # Approach: 
    # 
    # Use a dictionary to keep track of number of distinct particles (or beam tips) moving downwards (like a propogating wave crest)
    # Dictionary keys are columns (x values) 
    # Dictionary values are (column specific) counts of number of distinct particles (including those following duplicate paths) as move downward in rows (increasing y) to end of grid
    """
    
    from collections import defaultdict

    g = create_grid_from_file(filename)

    sp = get_starting_point(g)

    particle_row_map = defaultdict(int)
    particle_row_map[sp.get_x()] = 1 # Single initial particle (& timeline) at row zero (position 'S')

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


def solve_part2_using_recursive_approach(filename:str) -> int:
    """
    # Approach: Based on nice (succinct & efficient) solution approach from others (Jonathan Paulson, Hyperneutrino etc.)
    #
    # E.g. see: 
    #
    # https://github.com/jonathanpaulson/AdventOfCode/blob/master/2025/7.py
    # https://github.com/hyperneutrino/advent-of-code/blob/main/2025/day-07/part-2.py
    #
    """

    g = create_grid_from_file(filename)

    from functools import cache
    @cache
    def score(current_point:point.Point2D) -> int:        
        if not current_point: # Guard against off-grid point (albeit seemingly not needed for current input data)
            return 0

        p = point.Point2D(current_point.get_x(), current_point.get_y()+1)

        if p.get_y() >= g.get_height():
            return 1

        if is_splitter_point(g,p):
            return score(g.get_neighbour_east(p)) + score(g.get_neighbour_west(p))
        else:
            return score(p)

    sp = get_starting_point(g)
    return score(sp)