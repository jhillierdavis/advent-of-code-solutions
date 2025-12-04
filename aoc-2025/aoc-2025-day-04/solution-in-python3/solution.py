# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def is_roll_symbol(s):
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