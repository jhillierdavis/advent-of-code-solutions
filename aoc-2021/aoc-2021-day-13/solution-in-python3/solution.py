# Local libs
from helpers import fileutils, point, grid

def create_grid_from_file(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)

    max_x = 0
    max_y = 0

    points = set()
    for l in lines:
        (a,b) = l.split(",")
        x = int(a)
        y = int(b)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        p = point.Point2D(x,y)
        points.add(p)

    g = grid.Grid2D(max_x + 1, max_y + 1)

    for p in points:
        g.set_symbol(p, '#')

    return g
        