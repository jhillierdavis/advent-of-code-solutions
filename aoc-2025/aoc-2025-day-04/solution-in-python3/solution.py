# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

"""
def get_closest_neighbours(p):
    neighbour_set = set()
    for x in range(-1,2):
        for y in range(-1,2):
            np = point.Point2D(p.get_x() + x, p.get_y() + y)
            neighbour_set.add(np)

    neighbour_set.remove(p)
    #assert len(neighbour_set) == 26 # 9 + 9 + 8
    #logger.debug(f"p3d={p3d} neighbour_set={neighbour_set}")
    return neighbour_set  
"""

def is_roll_symbol(s):
    #return not (s == '.' or s == 'x')
    return s == '@'


def get_matching_rolls(g):
    match_set = set()
    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            s = g.get_symbol(p)
            if not is_roll_symbol(s):
                continue

            count = 0
            neighbours = p.get_closest_neighbours()
            for np in neighbours:
                if g.contains(np):
                    ns = g.get_symbol(np)
                    if not is_roll_symbol(ns):
                        continue
                    else:
                        count += 1

            if count < 4:
                #logger.debug(f"s={s} p={p} count={count}")            
                match_set.add(p)
    return match_set


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    match_set = get_matching_rolls(g)
    return len(match_set)


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    ans = 0
    g = grid.lines_to_grid(lines)
    while(True):
        match_set = get_matching_rolls(g)
        count = len(match_set)
        if count == 0:
            break

        ans += count
        for m in match_set:
            g.set_symbol(m, 'x')

    return ans
