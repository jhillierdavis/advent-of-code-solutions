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

    cp = get_starting_point(g)
    #logger.debug(f"Current point: cp={cp}")
    #g.set_symbol(cp, '|')

    splitters = get_splitter_points(g)

    height = g.get_height()    
    beams = {cp}

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

    grid.display_grid(g)

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


def solve_part1(filename):
    g = create_grid_from_file(filename)

    cp = get_starting_point(g)
    #logger.debug(f"Current point: cp={cp}")
    g.set_symbol(cp, '|')

    splitters = get_splitter_points(g)

    height = g.get_height()    
    beams = {cp}

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


def solve_part2(filename):
    from collections import defaultdict

    g = create_grid_from_file(filename)

    sp = get_starting_point(g)
    beams = {sp}

    splitters = get_splitter_points(g)

    height = g.get_height()    
    particle_counter = defaultdict(int)
    particle_counter[sp.get_x()] = 1 # Single initial particle (& timeline)
    
    # Iterate downward through rows, propogating beam tips (particles) & keeping count as go
    for h in range(1, height-1):   
        next_beams = set()     
        beam_tip_counter = defaultdict(int)

        for bp in beams:
            x = bp.get_x()
            y = bp.get_y() 

            np = point.Point2D(x,y+1)
            value = particle_counter[x]
            if np in splitters:
                # Split east / right
                npe = g.get_neighbour_east(np)                
                if npe:
                    #g.set_symbol(npe, '|')
                    next_beams.add(npe)
                    beam_tip_counter[npe.get_x()] += value

                # Split west / left
                npw = g.get_neighbour_west(np)
                if npw:
                    #g.set_symbol(npw, '|')
                    next_beams.add(npw)
                    beam_tip_counter[npw.get_x()] += value
            else:
                next_beams.add(np)
                beam_tip_counter[x] += value
            
        beams = next_beams     
        particle_counter = beam_tip_counter
            
        #logger.debug(f"h={h} beams={beams}")       

    #logger.debug(dict(sorted(particle_counter.items())))
    #logger.debug(sum(particle_counter.values()))
    return sum(particle_counter.values()) # Number of particles == timelines
