# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')

def get_rotated_and_flipped_grid(og):
    w = og.get_width()
    h = og.get_height()
    assert w == h 

    rg = grid.Grid2D(w,h)

    for x in range(w):
        for y in range(h):
            og_p = point.Point2D(x,y)
            rg_p = point.Point2D(y,x)
            rg.set_symbol(rg_p, og.get_symbol(og_p))
    return rg


def get_all_rotated_or_flipped_shapes_in_grid(g):
    g_set = set()
    g_set.add(g)

    g_set.add(g.get_inverted_horizontally())
    g_set.add(g.get_inverted_vertically())

    rg = get_rotated_and_flipped_grid(g)
    g_set.add(rg)

    g_set.add(rg.get_inverted_horizontally())
    g_set.add(rg.get_inverted_vertically())

    return g_set




def can_fit_required_shapes(shapes_map, fit_requirements):

    vals = fit_requirements.split(':')
    dims = vals[0].split('x')
    region_width = int(dims[0])
    region_height = int(dims[1])
    region_size = region_width * region_height

    logger.debug(f"region_size={region_size} region_width={region_width} region_height={region_height}")

    r_map = dict()
    qs = vals[1].split()
    for i, v in enumerate(qs):
        r_map[i] = int(v)
    logger.debug(f"r_map={r_map}") 


    max_shape_size = 3 * 3
    max_size_all_shapes = sum(r_map.values()) * max_shape_size

    logger.debug(f"max_size_all_shapes={max_size_all_shapes}")

    if max_size_all_shapes < region_size:
        return True

    
    min_size_map = dict()
    for k, v in shapes_map.items():
        g = grid.lines_to_grid(v)
        min_size_map[k] = g.count_symbol('#')

    min_size_all_shapes = 0
    for k,v in r_map.items():
        min_size_all_shapes += min_size_map[k] * v

    logger.debug(f"min_size_all_shapes={min_size_all_shapes}")

    if min_size_all_shapes > region_size:
        return False    

    if (max_size_all_shapes - min_size_all_shapes) >= 9:
        return True
    """
    for k, v in shapes_map.items():
        logger.debug(f"k={k}")

        g = grid.lines_to_grid(v)
        g_set = get_all_rotated_or_flipped_shapes_in_grid(g)
        for g in g_set:
            grid.display_grid(g)
            print()
    """
    est_size_all_shapes = (min_size_all_shapes + max_size_all_shapes) // 2


    return est_size_all_shapes <= region_size


def process_lines(lines):
    v_blocks = list()
    block = list()

    l_size = len(lines)
    for i, l  in enumerate(lines):        
        if not l:
            v_blocks.append(block)
            block = list()
        elif i == (l_size - 1):
            block.append(l)
            v_blocks.append(block)
        else:
            block.append(l)


    logger.debug(f"v_blocks={v_blocks}")

    # Process shapes
    shape_map = dict()
    for s in v_blocks[:-1]:
        shape_index = int(s[0][0])
        shape_map[shape_index] = s[1:]

    logger.debug(f"shape_map={shape_map}")

    # Process regions with shape fit requirements
    ans = 0
    for i, r in enumerate(v_blocks[-1]):
        logger.debug(f"i={i} r={r}")
        if can_fit_required_shapes(shape_map, r):
            ans += 1
    return ans    


def solve_part1(filename):
    #logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)

    ans = process_lines(lines)
    return ans


def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"
