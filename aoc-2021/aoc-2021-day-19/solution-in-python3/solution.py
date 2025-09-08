# Shared helper libraries
from helpers import fileutils, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def calculate_beacon_overlap_in_2d(scanner_set_0:set, scanner_set_1:set, min_intersection:int):
    overlap_count = 0

    for b0 in scanner_set_0:
        b0_x, b0_y = b0

        for b1 in scanner_set_1:
            b1_x, b1_y = b1

            offset_x = b0_x - b1_x
            offset_y = b0_y - b1_y
            #logger.debug(f"b0={b0} b1={b1} offset_x={offset_x} offset_y={offset_y}")

            offset_scanner_1 = set()            
            for e in scanner_set_1:
                x, y = e
                x += offset_x
                y += offset_y

                offset_scanner_1.add((x,y))

            intersection = scanner_set_0.intersection(offset_scanner_1)
            overlap_count =  len(intersection)
            if overlap_count >= min_intersection:
                logger.debug(f"min_intersection={min_intersection} intersection={intersection} scanner_location={offset_x, offset_y}")
                return overlap_count
    return 0

def generate_variant_map(scanner_set):
    variant_map = defaultdict(set)

    
    for e in scanner_set:
        index = 0
        x,y,z = e

        for i in [x,-x]:
            for j in [y, -y]:
                for k in [z, -z]:                    
                    variant_map[index].add((i,j,k))
                    index += 1
                    
                    # Facing directions
                    variant_map[index].add((i,k,j))
                    index += 1
                    variant_map[index].add((j,i,k))
                    index += 1
                    variant_map[index].add((j,k,i))
                    index += 1
                    variant_map[index].add((k,i,j))
                    index += 1
                    variant_map[index].add((k,j,i))
                    index += 1
                    
    
    return variant_map


def get_orientations(x,y,z):
    variants = []

    # About x
    variants.append((x,y,z))
    variants.append((x,z,-y))
    variants.append((x,-y,-z))
    variants.append((x,-z,y))

    # About -x
    variants.append((-x,-y,-z))
    variants.append((-x,z,y))
    variants.append((-x,y,-z))
    variants.append((-x,-z,-y))

    # About y
    variants.append((y,z,x))
    variants.append((y,x,-z))
    variants.append((y,-z,-x))
    variants.append((y,-x,z))

    # About -y
    variants.append((-y,-z,x))
    variants.append((-y,x,z))
    variants.append((-y,z,-x))
    variants.append((-y,-x,-z))


    # About y
    variants.append((z,x,y))
    variants.append((z,y,-x))
    variants.append((z,-x,-y))
    variants.append((z,-y,x))

    # About -y
    variants.append((-z,-x,y))
    variants.append((-z,y,x))
    variants.append((-z,x,-y))
    variants.append((-z,-y,-x))


    assert len(variants) == 24
    return variants


def get_orientation_map(point3d_set:set):
    orientation_map = defaultdict(set)
    for coord in point3d_set:
        (x,y,z) = coord
        variants = get_orientations(x,y,z)
        for i, v in enumerate(variants):
            orientation_map[i].add(v)

    return orientation_map


def calculate_beacon_overlap_in_3d(scanner_set_0:set, scanner_set_1:set, min_intersection:int):
    logger.debug(f"scanner_set_0={scanner_set_0} scanner_set_1={scanner_set_1} min_intersection={min_intersection}")
    overlap_count = 0

    variant_map = generate_variant_map(scanner_set_0)
    #logger.debug(f"variant_map={variant_map}")

    for b0 in scanner_set_0:
        b0_x, b0_y, b0_z = b0

        for k, v in variant_map.items():
            for b1 in v:
                b1_x, b1_y, b1_z = b1

                offset_x = b0_x - b1_x
                offset_y = b0_y - b1_y
                offset_z = b0_z - b1_z
                #logger.debug(f"b0={b0} b1={b1} offset_x={offset_x} offset_y={offset_y} offset_z={offset_z}")

                offset_scanner_1 = set()            
                for e in v:
                    x, y, z = e
                    x += offset_x
                    y += offset_y
                    z += offset_z

                    offset_scanner_1.add((x,y,z))

                intersection = scanner_set_0.intersection(offset_scanner_1)
                overlap_count =  len(intersection)
                if overlap_count >= min_intersection:
                    logger.debug(f"min_intersection={min_intersection} intersection={intersection} scanner_location={offset_x, offset_y, offset_z}")
                    
                    #return 0
                    return overlap_count
    return 0

import re

def extract_integers(text):
    # Find all sequences of digits in the string
    numbers = re.findall(r'\d+', text)
    # Convert them to integers
    return [int(num) for num in numbers]

def remove_blank_lines(lines):
    # Strip whitespace and filter out empty lines
    return [line for line in lines if line.strip()]

def parse_integer_string(input_string):
    # Split the string by commas and convert each part to an integer
    return [int(num.strip()) for num in input_string.split(',') if num.strip()]

def generate_orientation_variants(point3d:point.Point3D):
    variants = []
    x,y,z = point3d.to_tuple()

    for i in [x,-x]:
        for j in [y, -y]:
            for k in [z, -z]:
                variants.append((i,j,k))
                #variants.append((k,i,j))
                #variants.append((j,k,i))
    
    logger.debug(f"variants={variants}")
    return variants

from collections import defaultdict


def get_scanner_beacon_map(filename):
    lines = fileutils.get_file_lines_from(filename)
    lines = remove_blank_lines(lines)

    scanner_beacon_map = defaultdict(set)

    scanner_number = 0
    for l in lines:
        if l.startswith('--- scanner '):
            integers = extract_integers(l)
            scanner_number = integers[0]
        else:
            x,y,z = parse_integer_string(l)
            scanner_beacon_map[scanner_number].add((x,y,z))

    return scanner_beacon_map



def solve_part1(filename):
    #logger.debug("TODO: Implement AOC 2021 Part 1")    
    lines = fileutils.get_file_lines_from(filename)

    lines = remove_blank_lines(lines)

    scanner_beacon_map = defaultdict(list)

    scanner_number = 0
    for l in lines:
        if l.startswith('--- scanner '):
            integers = extract_integers(l)
            scanner_number = integers[0]
        else:
            x,y,z = parse_integer_string(l)
            scanner_beacon_map[scanner_number].append((x,y,z))

    #logger.debug(f"scanner_beacon_map={scanner_beacon_map}")

    """
    count = 12
    for k in scanner_beacon_map.keys():
        # TODO: Find same beacons (& don't double count)
        count += len(scanner_beacon_map[k]) - 12
    """
    """
    count = 0
    m_set = set()
    for k in scanner_beacon_map.keys():
        beacon_list = scanner_beacon_map[k]
        if k >= 2:
            break

        for i,ie in enumerate(beacon_list):
            ix, iy, iz = ie
            point_i = point.Point3D(ix, iy, iz)
            for j,je in enumerate(beacon_list):
                
                if i <= j:
                    continue

                jx, jy, jz = je
                point_j = point.Point3D(jx, jy, jz)

                m = point_i.get_manhatten_distance_to(point_j)
                logger.debug(f"k={k} point_i={point_i} point_i={point_j} m={m}")

                m_set.add(m)
                    
                
    logger.debug(f"m_set={m_set}")
    count = len(m_set)
    """

    # Approach:
    # For scanners > 0: map each 3d point to each scanner 0 point & calculate overlap count.  If less than 12 then repeat with re-oriented coords   

    count = 0
    return count

def solve_part2(filename):
    logger.debug("TODO: Implement AOC 2021 Part 1")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"