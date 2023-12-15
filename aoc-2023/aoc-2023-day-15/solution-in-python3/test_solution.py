import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("HASH", 52),
    ],    
)
def test_hash_of(input, expected):
    assert solution.hash_of(input) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 1320),
        pytest.param("puzzle-input-full.txt", 517015),
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 145),
        pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    