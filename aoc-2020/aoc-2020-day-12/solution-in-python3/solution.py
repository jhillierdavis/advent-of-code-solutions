# Shared helper libraries
from helpers import fileutils, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def move(x, y, direction, amount):
    if 'N' == direction:
        y -= amount 
    elif 'S' == direction:
        y += amount
    elif 'E' == direction:
        x += amount
    elif 'W' == direction:
        x -= amount
    return (x,y)

def change_direction(direction, amount, is_clockwise):
    if amount == 90:
        
        if direction == 'E':
            return 'S' if is_clockwise else 'N'
        
        if direction == 'S':
            return 'W' if is_clockwise else 'E'

        if direction == 'W':
            return 'N' if is_clockwise else 'S'

        if direction == 'N':
            return 'E' if is_clockwise else 'W'
        
    elif amount == 180:

        if direction == 'E':
            return 'W'
        
        if direction == 'S':
            return 'N'

        if direction == 'W':
            return 'E'

        if direction == 'N':
            return 'S'
    
    elif amount == 270:

        return change_direction(direction, 90, not is_clockwise)

    return direction


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    direction = 'E'
    x = 0
    y = 0
    for l in lines:
        instruction = l[0]
        magnitude = int(l[1:])

        logger.debug(f"direction={direction} instruction={instruction} magnitude={magnitude}")

        if 'R' == instruction:
            direction = change_direction(direction, magnitude, True)
        elif 'L' == instruction:
            direction = change_direction(direction, magnitude, False)
        elif 'F' == instruction:
            x, y = move(x, y, direction, magnitude)
        else:
            x, y = move(x,y, instruction, magnitude)   

        #logger.debug(f"x={x}, y={y}")

    origin = point.Point2D(0,0)
    destination = point.Point2D(x,y)
    return origin.get_manhatten_distance_to(destination)


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
