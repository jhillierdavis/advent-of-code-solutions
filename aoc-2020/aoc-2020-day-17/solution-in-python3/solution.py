# Shared helper libraries
from helpers import fileutils, point, grid

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
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
            
    logger.debug(f"active_set={active_set}")
    return len(active_set)


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
