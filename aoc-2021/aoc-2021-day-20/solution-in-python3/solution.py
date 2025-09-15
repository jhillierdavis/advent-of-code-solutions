# Shared helper libraries
from helpers import fileutils, grid, point

# Logging libraries
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def  get_image_enhancement_algorithm(filename):
    lines = fileutils.get_file_lines(filename)
    image_enhancement_algorithm = lines[0]
    logger.debug(f"image_enhancement_algorithm={image_enhancement_algorithm}")
    return image_enhancement_algorithm


def pixels_to_binary(pixel_str):
    return ''.join('1' if char == '#' else '0' for char in pixel_str)


def get_expanded_image_grid(image_grid):
    expansion = 10
    expanded_grid = grid.Grid2D(image_grid.get_width() + (2 * expansion), image_grid.get_height() + (2*expansion))
        
    for h in range(image_grid.get_height()):
        for w in range(image_grid.get_width()):
            symbol = image_grid.get_symbol(point.Point2D(w,h))
            if symbol == '#':
                expanded_grid.set_symbol(point.Point2D(w+expansion, h+expansion), '#')

    return expanded_grid

def strip_grid_parimeter(image_grid):
    parimeter = 2
    smaller_grid = grid.Grid2D(image_grid.get_width() - (2 * parimeter), image_grid.get_height() - (2* parimeter))
        
    for h in range(parimeter, image_grid.get_height()-parimeter):
        for w in range(parimeter, image_grid.get_width()-parimeter):
            symbol = image_grid.get_symbol(point.Point2D(w,h))
            if symbol == '#':
                smaller_grid.set_symbol(point.Point2D(w-parimeter, h-parimeter), '#')

    return smaller_grid


def get_value(image_grid, p:point.Point2D) -> set:
    x = p.get_x()
    y = p.get_y()

    surrounding_points = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x,y), (x+1,y), (x-1,y+1), (x,y+1),(x+1,y+1)]

    value = ''
    for (a,b) in surrounding_points:
        np = point.Point2D(a,b)
        if image_grid.contains(np):
            s = image_grid.get_symbol(np)
            value += s
    return value    


def get_enhanced_image_grid(image_grid, image_enhancement_algorithm):
    width = image_grid.get_width()
    height = image_grid.get_height()

    enhanced_grid = grid.Grid2D(height, width)
    

    for h in range(1, height-1):
        for w in range(1, width-1):        
            p = point.Point2D(w,h)
            value = get_value(image_grid, p)
            binary_str = pixels_to_binary(value)
            index = int(binary_str, 2)
            s = image_enhancement_algorithm[index]
            logger.debug(f"p={p} value={value} binary_str={binary_str} index={index} s={s}")
            enhanced_grid.set_symbol(p, s)
    return enhanced_grid


def solve_part1(filename):
    logger.debug("TODO: Implement Part 1")
    lines = fileutils.get_file_lines_from(filename)
    image_enhancement_algorithm = lines[0]    

    grid_lines = []
    for i in range(2, len(lines)):        
        grid_lines.append(lines[i])
    logger.debug(f"grid_lines={grid_lines}")

    image_grid = grid.lines_to_grid(grid_lines)
    #grid.display_grid(image_grid)

    image_grid = get_expanded_image_grid(image_grid)



    for i in range(2):

        enhanced_image_grid = get_enhanced_image_grid(image_grid, image_enhancement_algorithm)
        #grid.display_grid(enhanced_image_grid)

        image_grid = enhanced_image_grid

    image_grid = strip_grid_parimeter(enhanced_image_grid)
    grid.display_grid(image_grid)

    return image_grid.count_symbol('#')

def solve_part2(filename):
    logger.debug("TODO: Implement Part 2")
    lines = fileutils.get_file_lines_from(filename)

    return "TODO"
