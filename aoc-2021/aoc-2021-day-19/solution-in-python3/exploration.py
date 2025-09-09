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
