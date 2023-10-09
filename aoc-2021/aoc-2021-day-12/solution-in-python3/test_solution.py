import pytest

import solution

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-1.txt", 10),
        pytest.param("puzzle-input-example-2.txt", 19),
        pytest.param("puzzle-input-example-3.txt", 226),
        pytest.param("puzzle-input-full.txt", 4720), 
    ],    
)
def test_part1_solution(filename, expected):
    assert solution.count_part1_paths(filename) ==  expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example-1.txt", 36),
        pytest.param("puzzle-input-example-2.txt", 103),
        pytest.param("puzzle-input-example-3.txt", 3509),
        pytest.param("puzzle-input-full.txt", 147848), 
    ],    
)
def test_part2_solution(filename, expected):
    assert solution.count_part2_paths(filename) ==  expected    