import pytest

from helpers.grid import lines_to_grid, get_single_symbol_point
#from helpers.fileutils import get_file_lines_from
from helpers.pathutils import get_least_steps , get_cheat_path_ends, get_quickest_path
from helpers import point, grid

input_example = "AOC-2024-Day-20_Puzzle-Input-Example.txt"


AOC_2024_Day_20_Example_Grid = [ \
'###############', \
'#...#...#.....#', \
'#.#.#.#.#.###.#', \
'#S#...#.#.#...#', \
'#######.#.#.###', \
'#######.#.#...#', \
'#######.#.###.#', \
'###..E#...#...#', \
'###.#######.###', \
'#...###...#...#', \
'#.#####.#.###.#', \
'#.#...#.#.#...#', \
'#.#.#.#.#.#.###', \
'#...#...#...###', \
'###############']

@pytest.mark.parametrize(
    "grid_lines, expected",
    [
        pytest.param(AOC_2024_Day_20_Example_Grid, 85),

    ],    
)
def test_get_quickest_path(grid_lines, expected):
    # Given:
    g = lines_to_grid(grid_lines)
    sp = grid.find_single_symbol_point_and_replace(g, 'S', '.')
    ep = grid.find_single_symbol_point_and_replace(g, 'E', '.')

    # When:
    path = get_quickest_path(g, sp, ep)        

    # Then:
    size = len(path)

    assert size == expected
    assert path[0] == sp
    assert path[size -1] == ep