import pytest

from helpers import fileutils, point
import solution


def count_dots(grid):
    count = 0
    for x in range(grid.set_width()):
        for y in range(grid.set_height()):
            value = grid.get_symbol(point.Point2D(x,y))
            if value == '#':
                count += 1
    return count

def get_fold_input(filename):
    folds = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: folds: {folds}")
    fold = folds[0].split("fold along ",1)[1]
    return fold.split("=")


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

    
    if fold[0] == 'y': # fold vertically       
        fold_y = int(fold[1])

        #print(f"DEBUG: fold_y: {fold_y}")

        # Upper grid
        ug = g.get_subgrid_from_origin(g.get_width(), fold_y -1)

        lg = g.get_subgrid_inclusive(point.Point2D(0, fold_y), point.Point2D(g.get_width() - 1, g.get_height() - 1))
        ilg = lg.get_inverted_vertically()
        
        g = ug.merge_symbol(ilg, '#')
        

    elif fold[0] == 'x': # fold horizontally   
        fold_x = int(fold[1])

        # Upper grid
        lg = g.get_subgrid_from_origin(fold_x, g.get_height())

        rg = g.get_subgrid_inclusive(point.Point2D(fold_x, 0), point.Point2D(g.get_width() - 1, g.get_height() - 1))
        irg = rg.get_inverted_horizontally()

        g = lg.merge_symbol(irg, '#')        
    else:
        print(f"DEBUG: fold[0]={fold[0]} ")
        raise Exception(f"Unhandled instruction: {fold[0]}")

    assert g.count_symbol('#') == expected