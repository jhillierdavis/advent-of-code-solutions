# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_count_of_neighbours_with_symbol(g, p, s):
    count = 0
    
    neighbour_points = g.get_surrounding_neighbours(p)            
    for np in neighbour_points:
        symbol = g.get_symbol(np)
        if symbol == s:
            count += 1

    return count


def apply_rule_occupy(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == 'L':
                continue
            count = get_count_of_neighbours_with_symbol(g, p, '#')
            if count == 0:
                gc.set_symbol(p, '#')
    #grid.display_grid(gc)
    #print()
    return gc


def apply_rule_empty(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == '#':
                continue
            count = get_count_of_neighbours_with_symbol(g, p, '#')
            if count >= 4:
                gc.set_symbol(p, 'L')
    #grid.display_grid(gc)
    #print()
    return gc


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    
    gc = g.clone()
    prior_count = gc.count_symbol('#')
    for i in range(1000):
        gc = apply_rule_occupy(gc)
        gc = apply_rule_empty(gc)

        count = gc.count_symbol('#')
        logger.debug(f"Occupied i={i} count={count}")
        if count == prior_count:
            break
        prior_count = count

    return prior_count


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
