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


def get_fold_input(filename):
    folds = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: folds: {folds}")
    fold = folds[0].split("fold along ",1)[1]
    return fold.split("=")


def fold_grid_vertically(grid, fold_y):
    # Upper grid
    ug = grid.get_subgrid_from_origin(grid.get_width(), fold_y -1)

    # Lower grid
    lg = grid.get_subgrid_inclusive(point.Point2D(0, fold_y), point.Point2D(grid.get_width() - 1, grid.get_height() - 1))
    ilg = lg.get_inverted_vertically()

    return ug.merge_symbol(ilg, '#')

def fold_grid_horizontally(grid, fold_x):
    # Left grid
    lg = grid.get_subgrid_from_origin(fold_x, grid.get_height())

    # Right grid
    rg = grid.get_subgrid_inclusive(point.Point2D(fold_x, 0), point.Point2D(grid.get_width() - 1, grid.get_height() - 1))
    irg = rg.get_inverted_horizontally()

    return lg.merge_symbol(irg, '#')        


def process_first_fold_from_filename(filename):
    g = create_grid_from_file(filename)

    fold = get_fold_input(filename)

    
    if fold[0] == 'y': # fold vertically       
        fold_y = int(fold[1])

        g = fold_grid_vertically(g, fold_y)        

    elif fold[0] == 'x': # fold horizontally   
        fold_x = int(fold[1])

        g = fold_grid_horizontally(g, fold_x)

    else:
        print(f"DEBUG: fold[0]={fold[0]} ")
        raise Exception(f"Unhandled instruction: {fold[0]}")

    return g.count_symbol('#')   
        