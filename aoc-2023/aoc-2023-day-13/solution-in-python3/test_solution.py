import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 2),
        pytest.param("puzzle-input-full.txt", 100),
    ],    
)
def test_get_grids_from(filename, expected):
    grids = solution.get_grids_from(filename)

    assert len(grids) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 405),
        pytest.param("puzzle-input-full.txt", 30487),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 400),
        pytest.param("puzzle-input-full.txt", 31954),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected
