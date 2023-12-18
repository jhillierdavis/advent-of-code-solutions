import pytest

import solution
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
    assert solution.solve_part1(filename, grid_size) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename,expected):
    assert solution.solve_part2(filename) == expected    