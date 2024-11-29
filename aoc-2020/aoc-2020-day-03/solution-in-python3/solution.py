from helpers import fileutils, grid, point

def solve(filename):
    lines = fileutils.get_file_lines_from(filename)

    tree_grid = grid.lines_to_grid(lines)

    location = point.Point2D(0, 0)

    print(f'DEBUG: Tree grid height={tree_grid.get_height()} width={tree_grid.get_width()}')  

    tree_count = 0
    for h in range(tree_grid.get_height() -1):
        print(f'DEBUG: {location}')
        location = point.Point2D((location.get_x() + 3 ) % tree_grid.get_width(), location.get_y() + 1)

        if tree_grid.get_symbol(location) == '#':
            tree_count += 1

    return tree_count