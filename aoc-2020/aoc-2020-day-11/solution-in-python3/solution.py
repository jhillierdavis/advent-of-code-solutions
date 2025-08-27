# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_count_of_surrounding_neighbours_with_symbol(g:grid.Grid2D, p, s):
    count = 0
    
    neighbour_points = g.get_surrounding_neighbours(p)            
    for np in neighbour_points:
        symbol = g.get_symbol(np)
        if symbol == s:
            count += 1

    return count


def apply_rule_occupy_based_on_surrounding(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == 'L':
                continue
            count = get_count_of_surrounding_neighbours_with_symbol(g, p, '#')
            if count == 0:
                gc.set_symbol(p, '#')
    #grid.display_grid(gc)
    #print()
    return gc


def apply_rule_empty_based_on_surrounding(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == '#':
                continue
            count = get_count_of_surrounding_neighbours_with_symbol(g, p, '#')
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
        gc = apply_rule_occupy_based_on_surrounding(gc)
        gc = apply_rule_empty_based_on_surrounding(gc)

        count = gc.count_symbol('#')
        logger.debug(f"Occupied i={i} count={count}")
        if count == prior_count:
            break
        prior_count = count

    return prior_count

def is_continue_with_count(g, cp):
    if not g.contains(cp):
        return False, 0
    
    s = g.get_symbol(cp)
    if '#' == s:
        return False, 1
    elif 'L' == s:
        return False, 0
    
    return True, 0


def get_count_of_visible_neighbours_with_symbol(g:grid.Grid2D, p:point.Point2D):
    count = 0

    w = g.get_width()
    h = g.get_height()
    x = p.get_x()
    y = p.get_y()

    # Horizontals
    for i in range(0, x):
        cp = point.Point2D(x-1-i, y)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break
        

    for i in range(x+1, w):
        cp = point.Point2D(i, y)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    # Verticals
    for i in range(0, y):
        cp = point.Point2D(x, y-1-i)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    for i in range(y+1, h):
        cp = point.Point2D(x, i)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    # Diagonals
    for i in range(max(x, y)):
        cp = point.Point2D(x-1-i, y-1-i)        
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    for i in range(max(w, h)):
        cp = point.Point2D(x+1+i, y+1+i)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    for i in range(max(w-x, y)):
        cp = point.Point2D(x+1+i, y-1-i)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    for i in range(max(x, h-y)):
        cp = point.Point2D(x-1-i, y+1+i)
        b, n = is_continue_with_count(g, cp)
        if not b:
            count += n
            break

    return count


def apply_rule_occupy_based_on_visability(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == 'L':
                continue
            count = get_count_of_visible_neighbours_with_symbol(g, p)
            if count == 0:
                gc.set_symbol(p, '#')
    #grid.display_grid(gc)
    #print()
    return gc


def apply_rule_empty_based_on_visability(g:grid.Grid2D):
    gc = g.clone()

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            symbol = g.get_symbol(p)
            if not symbol == '#':
                continue
            count = get_count_of_visible_neighbours_with_symbol(g, p)
            if count >= 5:
                gc.set_symbol(p, 'L')
    #grid.display_grid(gc)
    #print()
    return gc


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)
    
    gc = g.clone()
    prior_count = gc.count_symbol('#')
    for i in range(1000):
        gc = apply_rule_occupy_based_on_visability(gc)
        gc = apply_rule_empty_based_on_visability(gc)

        count = gc.count_symbol('#')
        logger.debug(f"Occupied i={i} count={count}")
        if count == prior_count:
            break
        prior_count = count

    return prior_count
