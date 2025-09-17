# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def get_coords(desc_str:str):
    v1,v2 = desc_str.split("..")
    return max(int(v1), -50), min(int(v2), 50)

def get_cubes(desc_str:str):
    values = desc_str.split(',')
    
    x1,x2 = get_coords(values[0][2:])
    y1,y2 = get_coords(values[1][2:])
    z1,z2 = get_coords(values[2][2:])

    cubes = set()
    for x in range(int(x1), 1+int(x2)):
        for y in range(int(y1), 1+int(y2)):
            for z in range(int(z1), 1+int(z2)):
                cubes.add((x,y,z))
    return cubes
    

def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    on_cubes = set()
    for l in lines:
        values = l.split(' ')
        is_on = True if values[0] == 'on' else False
        cubes = get_cubes(values[1])
        if is_on:
            on_cubes = on_cubes.union(cubes)
        else:
            on_cubes = on_cubes.difference(cubes)


    return len(on_cubes)

def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
