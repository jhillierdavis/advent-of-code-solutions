# Shared helper libraries
from helpers import fileutils, point

# Standard libraries
from collections import defaultdict
import re

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


def get_orientations(x,y,z):
    variants = []

    # About x
    variants.append((x,y,z))
    variants.append((x,z,-y))
    variants.append((x,-y,-z))
    variants.append((x,-z,y))
    #variants.append((x,-z,-y))

    # About -x
    variants.append((-x,-y,z))
    variants.append((-x,z,y))
    variants.append((-x,y,-z))
    variants.append((-x,-z,-y))
    #variants.append((-x,y,z))

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

        for v in variant_map.values():
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
    md_set = set()

    for i,ie in enumerate(point_set):
        ix, iy, iz = ie
        point_i = point.Point3D(ix, iy, iz)
        for j,je in enumerate(point_set):
            
            if i <= j:
                continue

            jx, jy, jz = je
            point_j = point.Point3D(jx, jy, jz)

            md = point_i.get_manhatten_distance_to(point_j)
            #logger.debug(f"point_i={point_i} point_i={point_j} m={m}")

            md_set.add(md)

    return md_set


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
        
        if len(intersect) >= 12:
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


def get_scanner_overlap_map(bmd_map):
    overlap_map = defaultdict(set)
    for ik,iv in bmd_map.items():
        for jk,jv in bmd_map.items():
            if ik == jk:
                continue

            overlap = iv.intersection(jv)
            overlap_size = len(overlap)

            if overlap_size >= 2 * 12:
                overlap_map[ik].add(((jk, overlap_size)))
    
    logger.debug(f"overlap_map={overlap_map}")
    return overlap_map


def get_next_unprocessed_scanner_id(overlap_map, to_process_next_scanner_id, unprocessed_set):
    overlap_set = overlap_map[to_process_next_scanner_id]
    next_id = None
    max_size = 0
    for e in overlap_set:
        id, size = e
        if id not in unprocessed_set:
            continue

        if size > max_size:
            next_id = id
            max_size = size

    logger.debug(f"next_id={next_id} to_process_next_scanner_id={to_process_next_scanner_id}")  
    return next_id  


def get_transposed_beacons(scanner_beacons, offset):
    transposed_beacons = set()
    for sb in scanner_beacons:
        (x,y,z) = sb
        ox,oy,oz = offset
        new_location = ((x+ox), (y+oy), (z+oz))
        transposed_beacons.add(new_location)        
    return transposed_beacons


def get_beacons_and_scanner_locations(filename):
    input_scanner_beacon_map = get_input_scanner_beacon_map(filename)
    logger.debug(f"input_scanner_beacon_map.keys={input_scanner_beacon_map.keys()}")

    bmd_map = defaultdict(set) # BMD (Beacon Manhatten Distance)
    for k,v in input_scanner_beacon_map.items():
        bmd_map[k] = get_manhatten_distances_between_points(v)
    #logger.debug(f"bmd_map={bmd_map}")

    # Determine overlaps
    overlap_map = get_scanner_overlap_map(bmd_map)

    beacon_locations = set()
    beacon_locations.update(input_scanner_beacon_map[0])

    scanner_locations = set()
    scanner_locations.add((0,0,0))

    unprocessed_set = set(overlap_map.keys())
    unprocessed_set.remove(0)
    while len(unprocessed_set) > 0:
        for k, v in input_scanner_beacon_map.items():
            if k not in unprocessed_set:
                continue

            scanner_beacons, offset = process_scanner_beacons_against_pair(beacon_locations, input_scanner_beacon_map[k])
            if None != offset and None != scanner_beacons:
                transposed_beacons = get_transposed_beacons(scanner_beacons, offset)
                beacon_locations.update(transposed_beacons)
                unprocessed_set.remove(k)
                scanner_locations.add(offset)

    logger.debug(f"scanner_locations={scanner_locations}")
    return beacon_locations, scanner_locations



def solve_part1(filename):
    beacon_locations, _ = get_beacons_and_scanner_locations(filename)
    return len(beacon_locations)


def solve_part2(filename):
    _ , scanner_locations = get_beacons_and_scanner_locations(filename)
    logger.debug(f"scanner_locations={scanner_locations}")
    
    location_md_set = get_manhatten_distances_between_points(scanner_locations)
    return max(location_md_set)