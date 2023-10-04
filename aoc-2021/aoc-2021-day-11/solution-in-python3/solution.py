import grid2d
import point2d
import fileutils

def find_grid_points_by_predicate(grid:grid2d.Grid2D, predicate:callable):
    matches = set()
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            coord = point2d.Point2D(w,h)
            value = grid.getSymbol(coord)
            if predicate(value):
                matches.add(coord)
    return matches


def find_grid_point_matches(grid:grid2d.Grid2D, target_symbol:chr):
    lf = lambda value : value == target_symbol # Lambda function
    return find_grid_points_by_predicate(grid, lf) 


def find_grid_high_energy_points(grid:grid2d.Grid2D):
    lf = lambda value : value != '*' and int(value) > 9 # Lambda function
    return find_grid_points_by_predicate(grid, lf)


def increment_grid_value(grid:grid2d.Grid2D, coord:point2d.Point2D):
    symbol = grid.getSymbol(coord)
    if symbol == '*':
        return
    symbolValue = int(symbol)
    symbolValue += 1
    grid.setSymbol(coord, str(symbolValue))


def increment_all_grid_values(grid:grid2d.Grid2D):
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            coord = point2d.Point2D(w,h)
            increment_grid_value(grid, coord)


def handle_flash_points(grid:grid2d.Grid2D):
    flash_points = find_grid_high_energy_points(grid)
    if len(flash_points) == 0:
        return # Nothing to handle

    for fp in flash_points:
        grid.setSymbol(fp, '*') # Mark as flashing (at this step)
        neighbours = grid.getSurroundingNeighbours(fp)
        for n in neighbours:
            increment_grid_value(grid, n)

    handle_flash_points(grid) # Recurse (for flashing neigbours)


def reset_flashed_points(grid:grid2d.Grid2D) -> int:
    flashed_points = find_grid_point_matches(grid, '*')
    for fp in flashed_points:
        grid.setSymbol(fp, '0')
    return len(flashed_points)


def step(grid:grid2d.Grid2D):
    increment_all_grid_values(grid)
    handle_flash_points(grid)
    return reset_flashed_points(grid)


def grid_from_file(filename):
    lines = fileutils.get_file_lines(filename)
    return grid2d.lines_to_grid(lines)

    
# Part 1 solution
def count_flashes(filename, steps):
    grid = grid_from_file(filename)

    count = 0
    for i in range(steps):
        count += step(grid)
        #print(f"step {1+i} : {grid2d.grid_to_lines(grid)}")

    return count

# Part 2 solution
def steps_to_all_flashing(filename):
    grid = grid_from_file(filename)

    grid_size = grid.getHeight() * grid.getWidth()

    step_flashes = 0
    for i in range(1000): # Assume under 1K steps!
        step_flashes = step(grid)
        if step_flashes == grid_size:
            break

    return 1 + i