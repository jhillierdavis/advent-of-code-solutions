# Shared helper libraries
from helpers import fileutils

# Logging libraries
import logging
import logging.config

# Create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleLogger')


def get_2d_points_from_lines(lines:str) -> list[tuple[int,int]]:
    points = [tuple(map(int, l.split(','))) for l in lines]
    #logger.debug(f"points={points}")
    return points


def get_rectangle_size(p, q) -> int:
    width = 1 + abs(p[0] - q[0])
    height = 1 + abs(p[1] - q[1])
    rectangle_size = width * height
    return rectangle_size


def get_rectangle_sizes(points:list[tuple[int,int]]):
    rectangle_sizes = list()

    size = len(points)
    for i, p in enumerate(points):
        for j in range(i+1, size):      
            q = points[j]    

            r_size = get_rectangle_size(p,q)
            rectangle_sizes.append(r_size)

    #logger.debug(f"rectangle_sizes={rectangle_sizes}")
    return rectangle_sizes


def solve_part1(filename:str) -> int:
    lines = fileutils.get_file_lines_from(filename)

    points = get_2d_points_from_lines(lines)
    
    rectangle_sizes = get_rectangle_sizes(points)

    return max(rectangle_sizes)


from functools import cache


@cache
def get_x_and_y_min_max(p:tuple[int,int], q:tuple[int,int]) -> tuple[int, int, int, int]:
    x_min = min(p[0], q[0])
    x_max = max(p[0], q[0])
    y_min = min(p[1], q[1])
    y_max = max(p[1], q[1])

    return x_min, x_max, y_min, y_max


@cache
def get_midpoint(p:tuple[int,int], q:tuple[int,int]) -> tuple[int,int]:
    x_min, x_max, y_min, y_max = get_x_and_y_min_max(p,q)
    return (x_min + ((x_max - x_min) // 2) , y_min + ((y_max - y_min) // 2) )


@cache
def get_innerpoints(p:tuple[int,int], q:tuple[int,int]) -> list[tuple[int,int]]:
    inner_points = list()

    x_min, x_max, y_min, y_max = get_x_and_y_min_max(p,q)

    inner_points.append((x_min+1, y_min+1))
    inner_points.append((x_min+1, y_max-1))
    inner_points.append((x_max-1, y_max-1))
    inner_points.append((x_max-1, y_min+1))

    return inner_points


@cache
def get_sample_points(p:tuple[int,int], q:tuple[int,int]) -> list[tuple[int,int]]:
    sample_points = get_innerpoints(p,q)
    sample_points.append(get_midpoint(p,q))
    return sample_points


def solve_part2_using_brute_force_approach(filename:str) -> int:
    lines = fileutils.get_file_lines_from(filename)

    points = get_2d_points_from_lines(lines)

    @cache
    def point_in_rectilinear_polygon(p:tuple[int,int]) -> bool:
        """
        Ray casting for rectilinear polygon (inclusive of boundary).
        
        see:
        
        https://en.wikipedia.org/wiki/Rectilinear_polygon
        https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
        """
        x, y = p
        n = len(points)
        is_point_inside = False

        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]

            # Boundary check
            if x1 == x2 and x == x1 and min(y1, y2) <= y <= max(y1, y2):
                return True
            
            if y1 == y2 and y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True

            # Ray casting
            if (y1 > y) != (y2 > y):
                x_intersect = x1 if x1 == x2 else None
                if x_intersect is not None:
                    if x_intersect == x:
                        return True
                    if x_intersect > x:
                        is_point_inside = not is_point_inside

        return is_point_inside

    @cache
    def is_valid_sub_rectangle(p:tuple[int,int], q:tuple[int,int]) -> bool:
        x_min, x_max, y_min, y_max = get_x_and_y_min_max(p,q)
        
        for x in range(x_min + 1, x_max):
            if not point_in_rectilinear_polygon((x, y_min)) or not point_in_rectilinear_polygon((x, y_max)):
                return False
        
        for y in range(y_min + 1, y_max):
            if not point_in_rectilinear_polygon((x_min, y)) or not point_in_rectilinear_polygon((x_max, y)):
                return False
                
        return True

    def has_valid_enclosed_sample_points(p:tuple[int,int], q:tuple[int,int]) -> bool:
        sample_points = get_sample_points(p,q)

        for sp in sample_points:
            if not point_in_rectilinear_polygon(sp):
                return False
        return True

    def get_valid_rectangle_sizes_using_opposing_corner_points():
        valid_rectangle_sizes = list()
        p_size = len(points)
        for i, p in enumerate(points):
            #for j, q in enumerate(points):
            for j in range(i+1, p_size):      
                q = points[j]

                # Ignore if same point
                if p == q:
                    continue

                # Ignore p and q if on same lines (horizontal or vertical)
                #if p[0] == q[0] or p[1] == q[1]:
                #    continue

                a = (p[0], q[1])
                b = (q[0], p[1])

                if a in points and b not in points:
                    if not point_in_rectilinear_polygon(b):
                        continue

                elif b in points and a not in points:
                    if not point_in_rectilinear_polygon(a):
                        continue

                # Attempt to use some sample points to spot invalid rectangles earlier               
                if not has_valid_enclosed_sample_points(p,q):
                    continue

                # Use a brute force approach to validate the rectangle 
                if is_valid_sub_rectangle(p, q):
                    r_size = get_rectangle_size(p,q)    
                    #logger.debug(f"p={p} q={q} a={a} b={b} r_size={r_size}")            
                    valid_rectangle_sizes.append(r_size)                

        return valid_rectangle_sizes


    valid_rectangle_sizes = get_valid_rectangle_sizes_using_opposing_corner_points()
    
    #logger.debug(sorted(valid_rectangle_sizes))

    return max(valid_rectangle_sizes)


def solve_part2(filename:str) -> int:
    return "TODO!"