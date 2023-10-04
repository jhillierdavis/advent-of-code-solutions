import grid2d
import point2d
import fileutils

def find_grid_point_matches(grid:grid2d.Grid2D, target_symbol:chr):
    matches = set()
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            coord = point2d.Point2D(w,h)
            value = grid.getSymbol(coord)
            if value == target_symbol:
                matches.add(coord)
    return matches

def find_grid_high_energy_points(grid:grid2d.Grid2D):
    matches = set()
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            coord = point2d.Point2D(w,h)
            value = grid.getSymbol(coord)
            if value != '*' and int(value) > 9:
                matches.add(coord)
    return matches

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
    for fp in flash_points:
        grid.setSymbol(fp, '*')
        neighbours = grid.getSurroundingNeighbours(fp)
        for n in neighbours:
            increment_grid_value(grid, n)
    return len(flash_points)


def reset_flashed_points(grid:grid2d.Grid2D) -> int:
    flashed_points = find_grid_point_matches(grid, '*')
    for fp in flashed_points:
        grid.setSymbol(fp, '0')
    return len(flashed_points)


def step(grid:grid2d.Grid2D):
    increment_all_grid_values(grid)

    flash_point_count = 1
    while flash_point_count > 0:
        flash_point_count = handle_flash_points(grid)

    return reset_flashed_points(grid)
    

def test_small_example():
    lines = ["11111","19991","19191","19991","11111"]
    grid = grid2d.lines_to_grid(lines)
    assert lines == grid2d.grid_to_lines(grid)

    step(grid)

    expected = ["34543","40004","50005","40004","34543"]
    assert grid2d.grid_to_lines(grid) == expected


def count_flashes(filename, steps):
    lines = fileutils.get_file_lines(filename)
    grid = grid2d.lines_to_grid(lines)

    count = 0
    for i in range(steps):
        count += step(grid)
        #print(f"step {1+i} : {grid2d.grid_to_lines(grid)}")

    return count

def steps_to_all_flashing(filename):
    lines = fileutils.get_file_lines(filename)
    grid = grid2d.lines_to_grid(lines)

    grid_size = grid.getHeight() * grid.getWidth()

    step_flashes = 0
    for s in range(1000):
        step_flashes = step(grid)
        if step_flashes == grid_size:
            break

    return 1 + s