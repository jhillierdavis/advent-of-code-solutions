# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

import solution


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


def calculate_beacon_overlap_in_3d(scanner_set_0:set, scanner_set_1:set, min_intersection:int):
    #logger.debug(f"scanner_set_0={scanner_set_0} scanner_set_1={scanner_set_1} min_intersection={min_intersection}")
    overlap_count = 0

    #variant_map = generate_variant_map(scanner_set_0)
    #logger.debug(f"variant_map={variant_map}")

    variant_map = solution.get_orientation_map(scanner_set_1)

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
