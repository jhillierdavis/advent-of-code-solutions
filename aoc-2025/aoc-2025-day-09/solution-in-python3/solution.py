# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_2d_points_from_lines(lines:str) -> list[tuple[int,int]]:
    points = [tuple(map(int, l.split(','))) for l in lines]
    #logger.debug(f"points={points}")
    return points


def get_rectangle_size(p, q) -> int:
    width = 1 + abs(p[0] - q[0])
    height = 1 + abs(p[1] - q[1])
    rectange = width * height
    return rectange


def get_rectangles(points:list[tuple[int,int]]):
    rectangles = list()

    size = len(points)
    for i, p in enumerate(points):
        for j in range(i+1, size):      
            q = points[j]    

            rectangle = get_rectangle_size(p,q)
            rectangles.append(rectangle)

    #logger.debug(f"rectangles={rectangles}")
    return rectangles


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    points = get_2d_points_from_lines(lines)
    
    rectangles = get_rectangles(points)

    return max(rectangles)


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"
