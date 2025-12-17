# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_fit_region_dimensions(fit_requirements):
    vals = fit_requirements.split(':')
    dims = vals[0].split('x')
    region_width = int(dims[0])
    region_height = int(dims[1])
    region_size = region_width * region_height

    logger.debug(f"region_size={region_size} region_width={region_width} region_height={region_height}")

    return region_width, region_height, region_size


def get_fit_requirements_map(fit_requirements):
    vals = fit_requirements.split(':')

    r_map = dict()
    qs = vals[1].split()
    for i, v in enumerate(qs):
        r_map[i] = int(v)
    logger.debug(f"r_map={r_map}") 
    return r_map


def get_shape_size(shape:list[str]) -> int:
    size = 0
    for s_line in shape:
        size += sum(1 if x == '#' else 0 for x in s_line)
    return size


def can_fit_required_shapes_using_estimation(shapes_map, fit_requirements):
    region_width, region_height, region_size = get_fit_region_dimensions(fit_requirements)
    r_map = get_fit_requirements_map(fit_requirements)

    max_shape_size = 3 * 3 # NB: All shapes are the same size (3 x 3 squares)
    max_size_all_shapes = sum(r_map.values()) * max_shape_size

    logger.debug(f"max_size_all_shapes={max_size_all_shapes}")

    if max_size_all_shapes < region_size:
        return True
    
    min_size_map = dict()
    for k, v in shapes_map.items():
        #g = grid.lines_to_grid(v)
        #min_size_map[k] = g.count_symbol('#')
        min_size_map[k] = get_shape_size(v)

    min_size_all_shapes = 0
    for k,v in r_map.items():
        min_size_all_shapes += min_size_map[k] * v

    logger.debug(f"min_size_all_shapes={min_size_all_shapes}")

    # Check whether total size of non-overlapping shapes would fit (even if arrangement not actually possible)
    if min_size_all_shapes > region_size:
        logger.debug(f"Region too small for all non-overlapping shapes: region_size={region_size} min_size_all_shapes={min_size_all_shapes}")
        return False    

    # Check whether possible to total size of non-overlapping shapes (even if arrangement not actually possible)
    remainder = region_size - min_size_all_shapes
    if remainder <=  max_shape_size:
        logger.debug(f"Region fits all non-overlapping shapes: region_size={region_size} remainder={remainder} min_size_all_shapes={min_size_all_shapes}")
        return True
    
    # Use estimation to determine whether fits within region specified
    fudge_factor = 1 + (max_shape_size // 2)
    est_size_all_shapes = ((min_size_all_shapes + max_size_all_shapes) // 2) + fudge_factor 
    logger.debug(f"est_size_all_shapes={est_size_all_shapes} region_size={region_size} fudge_factor={fudge_factor}")
    return est_size_all_shapes <= region_size


def get_block_list_from_file_input_data(filename:str) -> list[str]:
    lines = fileutils.get_file_lines_from(filename)

    block_list = list()
    block = list()

    l_size = len(lines)
    for i, l  in enumerate(lines):        
        if not l:
            block_list.append(block)
            block = list()
        elif i == (l_size - 1):
            block.append(l)
            block_list.append(block)
        else:
            block.append(l)

        logger.debug(f"block_list={block_list}")
    
    return block_list


def get_shape_map(input_list:list[str]) -> dict:
    # Process shapes
    shape_map = dict()
    for s in input_list:
        shape_index = int(s[0][0])
        shape_map[shape_index] = s[1:]

    logger.debug(f"shape_map={shape_map}")    
    return shape_map


def solve_part1(filename):
    # Process a list of requirements for whether a quantity of different shapes fit in a provided region.
    # Count the number that do, & return this as the answer

    # Obtain input blocks (groups of lines separated by newline, or end of input file)
    block_list = get_block_list_from_file_input_data(filename)
    shape_list = block_list[:-1] # All except last input block (of grouped non-empty lines)
    fit_requirements_list = block_list[-1] # Last input block only

    # Obtain shapes to match (from all but last input block)

    shape_map = get_shape_map(shape_list) 

    # Process each specified empty regions (specified width & height) against its shape fit requirements
    ans = 0
    for i, fit_requirement in enumerate(fit_requirements_list):
        logger.debug(f"i={i} fit_requirement={fit_requirement}")
        if can_fit_required_shapes_using_estimation(shape_map, fit_requirement):
            ans += 1

    return ans
