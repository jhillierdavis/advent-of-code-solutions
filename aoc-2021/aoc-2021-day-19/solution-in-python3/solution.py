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

"""
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
"""

def get_orientations(x,y,z):
    variants = []

    # About x
    variants.append((x,y,z))
    variants.append((x,z,-y))
    variants.append((x,-y,-z))
    variants.append((x,-z,y))

    # About -x
    variants.append((-x,-y,z))
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


    # About z
    variants.append((z,x,y))
    variants.append((z,y,-x))
    variants.append((z,-x,-y))
    variants.append((z,-y,x))

    # About -z
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
    #logger.debug(f"scanner_set_0={scanner_set_0} scanner_set_1={scanner_set_1} min_intersection={min_intersection}")
    overlap_count = 0

    #variant_map = generate_variant_map(scanner_set_0)
    #logger.debug(f"variant_map={variant_map}")

    variant_map = get_orientation_map(scanner_set_0)

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

"""
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
"""

from collections import defaultdict


def get_input_scanner_beacon_map(filename):
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


def get_manhatten_distances_between_points(point_set:set):
    m_set = set()
    for i,ie in enumerate(point_set):
        ix, iy, iz = ie
        point_i = point.Point3D(ix, iy, iz)
        for j,je in enumerate(point_set):
            
            if i <= j:
                continue

            jx, jy, jz = je
            point_j = point.Point3D(jx, jy, jz)

            m = point_i.get_manhatten_distance_to(point_j)
            #logger.debug(f"point_i={point_i} point_i={point_j} m={m}")

            m_set.add(m)
    return m_set

def get_manhatten_distance_map(scanner_beacon_map):
    md_map = dict()
    
    scanner_beacons_0 = scanner_beacon_map[0]
    md_0 = get_manhatten_distances_between_points(scanner_beacons_0) 
    #logger.debug(f"md_0={md_0}")
    md_map[(0,0)] = md_0
    
    for k,v in scanner_beacon_map.items():
        if k == 0:
            continue

        o_map = get_orientation_map(v)
        for i, o in o_map.items():
            md_1 = get_manhatten_distances_between_points(o) 
            md_map[(k,i)] = md_1

    return md_map


def get_exclusions(index, scanner_beacon_map, md_map, exclusion_set):
    for i in scanner_beacon_map.keys():
        if i == 0:
            continue

        for j in range(24):
            k = (i,j)
            if k in exclusion_set:
                continue

            intersect = md_map[index].intersection(md_map[k])
            if len(intersect) < 2 * 12:                
                exclusion_set.add(k)
    return exclusion_set


from collections import defaultdict

def get_point_pairs_diff_map(point_set:set):
    pair_map = defaultdict(None)

    for i,ie in enumerate(point_set):
        ix, iy, iz = ie
        
        for j,je in enumerate(point_set):
            
            if i <= j:
                continue

            jx, jy, jz = je

            diff = (ix-jx, iy-jy, iz-jz)

            pair_map[diff] = (ie,je)
    return pair_map


def get_offset(intersect, origin_pair_diff_map, pair_diff_map):
    offsets = set()
    offset = None
    for key in intersect:
        (tx_0, ty_0, tz_0) = origin_pair_diff_map[key][0]
        tx_1, ty_1, tz_1 = pair_diff_map[key][0]
        #offset = (tx_1 - tx_0, ty_1 - ty_0, tz_1 - tz_0)
        offset = (tx_0 - tx_1, ty_0 - ty_1, tz_0 - tz_1)
        offsets.add(offset)

    assert len(offsets) == 1
    return offset


def get_shared_beacons(scanner_beacons, origin_pair_diff_map):
    orientation_map = get_orientation_map(scanner_beacons)
    shared_beacons = set()
    for k, v in orientation_map.items():
        #print(f"scanner_1_beacons={scanner_1_beacons}")    
        pp_info = get_point_pairs_diff_map(v)

        intersect = set(pp_info.keys()).intersection(origin_pair_diff_map.keys())
        
        if len(intersect) >= 24:
            print(f"k={k} len(intersect)={len(intersect)} intersect={intersect}")

            #offset = get_offsets(intersect, origin_pair_diff_map, pp_info)            
            for key in intersect:
                shared_beacons.add(origin_pair_diff_map[key][0])
                shared_beacons.add(origin_pair_diff_map[key][1])
            break    
    return shared_beacons


def get_transposed_beacons(scanner_beacons, origin_pair_diff_map):
    orientation_map = get_orientation_map(scanner_beacons)
    
    for k, v in orientation_map.items():
        
        pp_info = get_point_pairs_diff_map(v)
        #logger.debug(f"origin_pair_diff_map.keys={sorted(origin_pair_diff_map.keys())}")
        #logger.debug(f"pp_info.keys={sorted(pp_info.keys())}")
        #logger.debug("")

        intersect = set(pp_info.keys()).intersection(origin_pair_diff_map.keys())
        logger.debug(f"k={k} len(intersect)={len(intersect)} intersect={intersect}")
        logger.debug("")
        if len(intersect) >= 24:
            

            offset = get_offset(intersect, origin_pair_diff_map, pp_info)            
            tranposed_beacons = set()
            for sb in scanner_beacons:
                (x,y,z) = sb
                ox,oy,oz = offset
                tranposed_beacons.add(((x+ox), (y+oy), (z+oz)))
            return tranposed_beacons 
        
    raise Exception(f"Failed to transpose beacons for scanner_beacons={scanner_beacons}")

from collections import defaultdict

def get_max_overlapping_scanner_id(scanner_id, md_map):
    overlap_index = None
    overlap_count = 0

    for i in md_map.keys():
        if i == scanner_id:
            continue    
            
        intersect = (set(md_map[i])).intersection(md_map[scanner_id])
        intersect_overlap = len(intersect)
        if intersect_overlap > overlap_count:
            overlap_count = intersect_overlap
            overlap_index = i

    return overlap_index


def solve_part1_legacy(filename):

    scanner_beacon_map = get_input_scanner_beacon_map(filename)
    logger.debug(f"scanner_beacon_map.keys={scanner_beacon_map.keys()}")

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
    """
    md_map = get_manhatten_distance_map(scanner_beacon_map)
    logger.debug(f"md_map.keys={md_map.keys()}")
    count = 0

    exclusion_set = get_exclusions((0,0), scanner_beacon_map, md_map, set())

    for i in scanner_beacon_map.keys():
        if i == 0:
            continue

        for j in range(24):
            k = (i,j)
            if k in exclusion_set:
                continue

            exclusion_set = get_exclusions(k, scanner_beacon_map, md_map, exclusion_set)

    logger.debug(f"exclusion_set={exclusion_set}")
    inclusion_set = set(md_map.keys()).difference(exclusion_set)
    logger.debug(f"inclusion_set={inclusion_set}")
    """

    origin_scanner_beacons = scanner_beacon_map[0]
    origin_pair_diff_map = get_point_pairs_diff_map(origin_scanner_beacons)

    beacons = set()
    for k, v in scanner_beacon_map.items():
        logger.debug(f"k={k}")
        logger.debug(f"v={v}")
        if k == 0: # Origin
            beacons.update(origin_scanner_beacons)
        else:
            transposed_beacons = get_transposed_beacons(v, origin_pair_diff_map)
            beacons.update(transposed_beacons)

    return len(beacons)



def get_paired_scanner_based_on_overlap(current_scanner_id, md_map, processed_scanner_id_set):
    overlap_index = None
    overlap_count = 0

    for i in md_map.keys():
        if i == current_scanner_id or i in processed_scanner_id_set:
            continue    
            
        intersect = (set(md_map[i])).intersection(md_map[current_scanner_id])
        intersect_overlap = len(intersect)
        if intersect_overlap > overlap_count:
            overlap_count = intersect_overlap
            overlap_index = i

    return overlap_index   


def get_next_scanner_id_to_process(processed_beacons, md_map, processed_scanner_id_set):
    overlap_index = None
    overlap_count = 0

    pb_md_set = get_manhatten_distances_between_points(processed_beacons)

    for i in md_map.keys():
        if i in processed_scanner_id_set:
            continue    
            
        intersect = (set(md_map[i])).intersection(pb_md_set)
        intersect_overlap = len(intersect)
        if intersect_overlap > overlap_count:
            overlap_count = intersect_overlap
            overlap_index = i

    return overlap_index  

def process_scanner_beacons_against_pair(processed_scanner_beacons, unprocessed):
    origin_pair_diff_map = get_point_pairs_diff_map(processed_scanner_beacons)


    orientation_map = get_orientation_map(unprocessed)
    
    for k, v in orientation_map.items():
        
        pp_info = get_point_pairs_diff_map(v)

        intersect = set(pp_info.keys()).intersection(origin_pair_diff_map.keys())
        if len(intersect) >= 12:
            offset = get_offset(intersect, origin_pair_diff_map, pp_info)            
            return v, offset        
    return None, None


def solve_part1(filename):
    input_scanner_beacon_map = get_input_scanner_beacon_map(filename)
    logger.debug(f"input_scanner_beacon_map.keys={input_scanner_beacon_map.keys()}")

    count = 0
    for k,v in input_scanner_beacon_map.items():
        size = len(v)
        logger.debug(f"k={k} size={size}")
        count += len(v)
    logger.debug(f"Initial count of beacon coords = {count}")


    bmd_map = defaultdict(set) # BMD (Beacon Manhatten Distance)
    for k,v in input_scanner_beacon_map.items():
        bmd_map[k] = sorted(get_manhatten_distances_between_points(v))

    """
    for i in range(4):
        for j in range(4):
            if i <= j:
                continue

            intersect = (set(md_map[i])).intersection(md_map[j])
            overlap = len(intersect)
            if overlap >= 24:
                print(f"Pair i={i} j={j} overlap={overlap}")
    """

    beacons = set()
    beacons.update(input_scanner_beacon_map[0])

    scanner_location_map = defaultdict()
    scanner_location_map[0] = (0,0,0)

    processed_scanner_beacon_map = defaultdict(set)
    processed_scanner_beacon_map[0] = input_scanner_beacon_map[0]



    current_scanner_id = 0

    
    processed_scanner_id_set = set()

    count = 0
    for _ in bmd_map.keys():
        processed_scanner_id_set.add(current_scanner_id)
        """
        overlap_index = get_max_overlapping_scanner_id(i, bmd_map)
        logger.debug(f"Pair i={i} overlap_index={overlap_index}")
        """
        #process_next_scanner_id = get_paired_scanner_based_on_overlap(current_scanner_id, bmd_map, processed_scanner_id_set)
        process_next_scanner_id = get_next_scanner_id_to_process(beacons, bmd_map, processed_scanner_id_set)
        if None == process_next_scanner_id:
            break
        logger.debug(f"process_next_scanner_id={process_next_scanner_id}")
        # TODO: Process 
        scanner_beacons, offset = process_scanner_beacons_against_pair(beacons, input_scanner_beacon_map[process_next_scanner_id])
        assert scanner_beacons is not None
        assert offset is not None

        logger.debug(f"offset={offset}")

        transposed_beacons = set()
        for sb in scanner_beacons:
            (x,y,z) = sb
            ox,oy,oz = offset
            new_location = ((x+ox), (y+oy), (z+oz))
            transposed_beacons.add(new_location)        
            beacons.add(new_location)
        
        # Overlapping beacons
        #overlapping_beacons = transposed_beacons.intersection(processed_scanner_beacon_map[current_scanner_id])
        #overlapping_beacons_count = len(overlapping_beacons)
        #logger.debug(f"overlapping_beacons_count={overlapping_beacons_count}")
        #logger.debug(f"overlapping_beacons={overlapping_beacons}")


        current_scanner_id = process_next_scanner_id
        scanner_location_map[current_scanner_id] = offset
        processed_scanner_beacon_map[current_scanner_id] = transposed_beacons
        count = len(beacons)
        logger.debug(f"Processed beacon count={count}")
        


    return count



def solve_part2(filename):
    logger.debug("TODO: Implement AOC 2021 Part 1")
    lines = fileutils.get_file_lines_from(filename)

    

    return "TODO"