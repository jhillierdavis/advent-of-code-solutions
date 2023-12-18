import pytest

import solution, solution_part2
"""
@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("grid-with-interior-1.txt", 1),
        pytest.param("grid-with-interior-4.txt", 4),
        pytest.param("grid-with-interior-11.txt", 11),
        pytest.param("grid-with-interior-15.txt", 15),
        pytest.param("grid-with-interior-62.txt", 24),        
        pytest.param("grid-with-interior-35.txt", 35),
        pytest.param("grid-with-interior-full-puzzle.txt", -1),
    ],    
)
def test_count_interior(filename, expected):
    assert solution.count_interior(filename) == expected
"""

@pytest.mark.parametrize(
    "filename,grid_size,expected",
    [
        pytest.param("puzzle-input-example.txt", 20, 62),
        pytest.param("puzzle-input-full.txt", 1000, 47675), # 46131 too low ( perimeter_count=3730 content_count=42401)! # 43258 too low
    ],    
)
def test_solve_part1(filename, grid_size, expected):
    assert solution.solve_using_fjl7_grid_from(filename, grid_size) == expected

    # Alternative area calculation approach (used for part2)
    assert solution_part2.solve_part1_using_area_calculation_from(filename)


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("(#70c710)", ('R', 461937)),
        pytest.param("(#5713f0)", ('R', 356671)),
        pytest.param("(#d2c081)", ('D', 863240)),
        pytest.param("(#59c680)", ('R', 367720)),
        pytest.param("(#411b91)", ('D', 266681 )),
        pytest.param("(#8ceee2)", ('L', 577262)),
        pytest.param("(#caa173)", ('U', 829975)),
        pytest.param("(#1b58a2)", ('L', 112010)),
        pytest.param("(#caa171)", ('D', 829975)),
        pytest.param("(#7807d2)", ('L', 491645)),
        pytest.param("(#a77fa3)", ('U', 686074)),
        pytest.param("(#015232)", ('L', 5411)),
        pytest.param("(#7a21e3)", ('U', 500254)),
    ],    
)
def test_get_direction_and_distance_from(input, expected):
    assert solution_part2.get_direction_and_distance_from(input) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 952408144115),
        pytest.param("puzzle-input-full.txt", 122103860427465),
    ],    
)
def test_solve_part2(filename,expected):
    assert solution_part2.solve_part2(filename) == expected    