import pytest
import sys

import solution

@pytest.mark.parametrize(
    "current, next, expected",
    [
        pytest.param('.', '.', False),
        pytest.param('-', '.', False),
        pytest.param('|', '.', False),
        pytest.param('F', '.', False),
        pytest.param('7', '.', False),
        pytest.param('J', '.', False),
        pytest.param('L', '.', False),
        pytest.param('-', '|', False),
        pytest.param('|', '-', False),
        pytest.param('-', '-', True),
        pytest.param('-', 'F', True), # only if moving left
        pytest.param('-', 'L', True), # only if moving left        
        pytest.param('-', '7', True), # only if moving right
        pytest.param('-', 'J', True), # only if moving right
        pytest.param('|', '|', True),
    ],    
)
def test_can_move_from_to(current, next, expected):
    assert solution.can_move_from_to(current, next) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example-1.txt', 4),
        pytest.param('puzzle-input-example-1a.txt', 4),
        pytest.param('puzzle-input-example-2.txt', 8),
        pytest.param('puzzle-input-example-2a.txt', 8),
        #pytest.param('puzzle-input-full.txt', 0), # TODO: Answer?
    ],    
)
def test_solution(filename, expected):
    sys.setrecursionlimit(10000)    
    assert solution.solve(filename) == expected
