from helpers import fileutils, grid, point

def get_tree_count(tree_grid, x_movement, y_movement):
    location = point.Point2D(0, 0)

    tree_count = 0
    for h in range(tree_grid.get_height() -1):
        #print(f'DEBUG: {location}')
        x_new = (location.get_x() + x_movement ) % tree_grid.get_width()
        y_new = location.get_y() + y_movement
        if y_new >= tree_grid.get_height():
            break

        location = point.Point2D(x_new, y_new)

        if tree_grid.get_symbol(location) == '#':
            tree_count += 1

    return tree_count    

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    tree_grid = grid.lines_to_grid(lines)

    #print(f'DEBUG: Tree grid height={tree_grid.get_height()} width={tree_grid.get_width()}')  

    return get_tree_count(tree_grid, 3, 1)


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    tree_grid = grid.lines_to_grid(lines)

    return get_tree_count(tree_grid, 1, 1) * get_tree_count(tree_grid, 3, 1) * get_tree_count(tree_grid, 5, 1) * get_tree_count(tree_grid, 7, 1) * get_tree_count(tree_grid, 1, 2)