import pytest

from helpers import fileutils, point
import solution



def count_dots(grid):
    count = 0
    for x in range(grid.get_width()):
        for y in range(grid.get_height()):
            value = grid.get_symbol(point.Point2D(x,y))
            if value == '#':
                count += 1
    return count

def get_fold_input(filename):
    folds = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: folds: {folds}")
    fold = folds[0].split("fold along ",1)[1]
    return fold.split("=")

# def merge_grids(grid_one, grid_two):
#     min_width = min(grid_one.get_width(), grid_two.get_width())
#     min_height = min(grid_one.get_height(), grid_two.get_height())

#     for x in range(min_width):
#         for y in range(min_height):
#             p = point.Point2D(x,y)
#             if '#' == grid_one.get_symbol(p) or '#' == grid_two.get_symbol(p):




@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 17),
        pytest.param("puzzle-input-full.txt", 682), 
    ],    
)
def test_part1_solution(filename, expected):
    g = solution.create_grid_from_file(filename)

    fold = get_fold_input(filename)

    count = 0
    if fold[0] == 'y':        
        fold_y = int(fold[1])

        print(f"DEBUG: fold_y: {fold_y}")

        # Upper grid
        ug = g.get_subgrid_from_origin(g.get_width(), fold_y -1)

        lg = g.get_subgrid_inclusive(point.Point2D(0, fold_y), point.Point2D(g.get_width() - 1, g.get_height() - 1))
        ilg = lg.get_inverted_vertically()
        
        for x in range(ug.get_width()):
            for y in range(ug.get_height()):
                p = point.Point2D(x,y)
                if '#' == ug.get_symbol(p) or '#' == ilg.get_symbol(p):
                    count += 1

    elif fold[0] == 'x': 
        fold_x = int(fold[1])

        # Upper grid
        lg = g.get_subgrid_from_origin(fold_x, g.get_height())

        rg = g.get_subgrid_inclusive(point.Point2D(fold_x, 0), point.Point2D(g.get_width() - 1, g.get_height() - 1))
        irg = rg.get_inverted_horizontally()
        
        for x in range(lg.get_width()):
            for y in range(lg.get_height()):
                p = point.Point2D(x,y)
                if '#' == lg.get_symbol(p) or '#' == irg.get_symbol(p):
                    count += 1
    else:
        print(f"DEBUG: fold[0]={fold[0]} ")

    assert count == expected