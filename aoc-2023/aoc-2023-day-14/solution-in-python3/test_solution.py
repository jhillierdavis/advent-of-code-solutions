import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-slid-north.txt", 18),
    ],    
)
def test_count_rounded_rocks_from(filename, expected):
    assert solution.count_rounded_rocks_from(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-slid-north.txt", 136),
    ],    
)
def test_calculate_load_from(filename, expected):
    assert solution.calculate_load_from(filename) == expected    

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 136),
        pytest.param("puzzle-input-full.txt", 113456),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected        