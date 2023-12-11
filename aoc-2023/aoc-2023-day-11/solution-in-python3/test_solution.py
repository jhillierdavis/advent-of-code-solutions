import pytest

from helpers import grid

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", [3,7]),
    ],    
)
def test_get_empty_rows_from_filename(filename, expected):
    assert solution.get_empty_rows_from_filename(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", [2,5,8]),
    ],    
)
def test_get_empty_columns_from_filename(filename, expected):
    assert solution.get_empty_columns_from_filename(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", "puzzle-input-example-expanded.txt"),
    ],    
)
def test_matches_expanded(filename, expected):
    g_orig = solution.get_grid_from_filename(filename)
    g_exp = solution.get_grid_from_filename(expected)
    assert grid.grid_to_lines(g_orig) != grid.grid_to_lines(g_exp)

    g_actual = solution.get_expanded_grid_from_filename(filename)

    # TODO: Implement grid equality!
    assert grid.grid_to_lines(g_actual) != grid.grid_to_lines(g_orig)
    assert grid.grid_to_lines(g_actual) == grid.grid_to_lines(g_exp)


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 9),
    ],    
)
def test_solution(filename, expected):
    g = solution.get_expanded_grid_from_filename(filename)

    locations = solution.get_galaxy_locations(g)

    assert len(locations) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 374),
        pytest.param("puzzle-input-full.txt",  9693756),
    ],    
)
def test_solution(filename, expected):
    assert solution.solve_part1(filename) == expected


# Expansion 2 -> ratio 1:2 (i.e. double) for empty lines (i.e. rows or columns without any galaxies identified by '#' - should have been '@' :-)
@pytest.mark.parametrize(
    "filename, expansion_ratio, expected",
    [
        pytest.param("puzzle-input-example.txt", 1, 292), # No expansion
        pytest.param("puzzle-input-example.txt", 2, 374), # Double expansion
        pytest.param("puzzle-input-full.txt", 2, 9693756),
        pytest.param("puzzle-input-example.txt", 10, 1030), # 10 x expansion
        pytest.param("puzzle-input-example.txt", 100, 8410),
        pytest.param("puzzle-input-full.txt", 1000000, 717878258016), # 1 million times expansion
    ],    
)
def test_solution(filename, expansion_ratio, expected):
    assert solution.solve_part2(filename, expansion_ratio) == expected