
from collections import defaultdict

from helpers import grid, point

def clone_and_increment_grid(original_grid):
    new_grid = original_grid.clone()

    for w in range(new_grid.get_width()):
        for h in range(new_grid.get_height()):
            p = point.Point2D(w,h)
            value = int(original_grid.get_symbol(p))
            if value >= 9: 
                value = 0 # reset
            new_grid.set_symbol(p, 1 + value)
    
    return new_grid

def copy_grid_symbols(original_grid, target_grid, offset_x, offset_y):
    for w in range(original_grid.get_width()):
        for h in range(original_grid.get_height()):
            p = point.Point2D(w,h)
            offset_p = point.Point2D(w + offset_x, h + offset_y)
            target_grid.set_symbol(offset_p, original_grid.get_symbol(p))



def spawn_grid_from(original_grid):
    larger_grid = grid.Grid2D(original_grid.get_width() * 5, original_grid.get_height() * 5)

    map = defaultdict(int)
    map[0] = original_grid
    for i in range(1, 9):
        map[i] = clone_and_increment_grid(map[i -1])
        print(f"DEBUG: map[{i}]={map[i]}")
        grid.display_grid(map[i])



    for x in range(0,5):
        for y in range(0,5):
            i = x + y
            copy_grid_symbols(map[i], larger_grid, x * original_grid.get_width(), y * original_grid.get_height())
            

    grid.display_grid(larger_grid)
    
    return larger_grid