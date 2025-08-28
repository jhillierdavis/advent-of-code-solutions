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
        y += amount 
    elif 'S' == direction:
        y -= amount
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


def rotate_90(x, y, is_clockwise=True):
    """
    Rotates a 2D point (x, y) 90 degrees clockwise around the origin.
    Returns: (new_x, new_y): Tuple of rotated coordinates.
    """
    if is_clockwise:
        new_x = y
        new_y = -x    
        return (new_x, new_y)
    else:
        new_x = -y
        new_y = x    
        return (new_x, new_y)


def change_waypoint_direction(wx, wy, amount, is_clockwise):
    if amount == 90:
        wx, wy = rotate_90(wx, wy, is_clockwise)
    elif amount == 180:
        wx, wy = rotate_90(wx, wy, is_clockwise)
        wx, wy = rotate_90(wx, wy, is_clockwise)
    elif amount == 270:
        wx, wy = change_waypoint_direction(wx, wy, 90, not is_clockwise)
    return wx, wy


def solve_part2(filename):
    #logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    # Ship coordinates (absolute)
    sx = 0
    sy = 0

    # Waypoint coordinates (relative to ship)
    wx = 10
    wy = 1
    

    for l in lines:
        instruction = l[0]
        amount = int(l[1:])

        logger.debug(f"instruction={instruction} amount={amount}")

        if 'R' == instruction:
            wx, wy, = change_waypoint_direction(wx, wy, amount, True)
        elif 'L' == instruction:
            wx, wy, = change_waypoint_direction(wx, wy, amount, False)
        elif 'F' == instruction:            
            sx += wx * amount
            sy += wy * amount
        else:
            wx, wy = move(wx, wy, instruction, amount)   

        logger.debug(f"sx={sx} sy={sy} wx={wx} wy={wy}")

    origin = point.Point2D(0,0)
    destination = point.Point2D(sx,sy)
    return origin.get_manhatten_distance_to(destination)