# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def solve_part1(filename):
    logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    start_points = g.get_points_matching('S')
    assert len(start_points) == 1

    cp = start_points.pop()
    #logger.debug(f"Current point: cp={cp}")
    g.set_symbol(cp, '|')

    splitters = g.get_points_matching('^')
    assert len(splitters) > 0
    #logger.debug(f"Splitter points: splitters={splitters}")

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
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"
