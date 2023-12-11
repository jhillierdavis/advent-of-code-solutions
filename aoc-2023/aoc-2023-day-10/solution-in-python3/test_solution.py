import pytest
import sys

import solution

@pytest.mark.parametrize(
    "current, next, expected",
    [
        pytest.param('.', '.', False),
        pytest.param('S', '.', False),
        pytest.param('S', 'S', False),        

        pytest.param('S', '|', False),
        pytest.param('S', 'F', False),
        pytest.param('S', 'L', False),

        pytest.param('S', '-', True),
        pytest.param('S', '7', True),
        pytest.param('S', 'J', True),

        pytest.param('|', 'S', False),
        pytest.param('|', '|', False),
        pytest.param('|', '-', False),
        pytest.param('|', 'F', False),
        pytest.param('|', '7', False),
        pytest.param('|', 'L', False),
        pytest.param('|', 'J', False),

        pytest.param('-', 'S', True),
        pytest.param('-', '|', False),
        pytest.param('-', '-', True),
        pytest.param('-', 'F', False),
        pytest.param('-', '7', True),
        pytest.param('-', 'L', False),
        pytest.param('-', 'J', True),

        pytest.param('7', 'S', False),
        pytest.param('7', '|', False),
        pytest.param('7', '-', False),
        pytest.param('7', 'F', False),
        pytest.param('7', '7', False),
        pytest.param('7', 'L', False),
        pytest.param('7', 'J', False),

        pytest.param('J', 'S', False),
        pytest.param('J', '|', False),
        pytest.param('J', '-', False),
        pytest.param('J', 'F', False),
        pytest.param('J', '7', False),
        pytest.param('J', 'L', False),
        pytest.param('J', 'J', False),

        pytest.param('F', 'S', True),
        pytest.param('F', '|', False),
        pytest.param('F', '-', True),
        pytest.param('F', 'F', False),
        pytest.param('F', '7', True),
        pytest.param('F', 'L', False),
        pytest.param('F', 'J', True),

        pytest.param('L', 'S', True),
        pytest.param('L', '|', False),
        pytest.param('L', '-', True),
        pytest.param('L', 'F', False),
        pytest.param('L', '7', True),
        pytest.param('L', 'L', False),
        pytest.param('L', 'J', True),
    ],    
)
def test_can_move_east(current, next, expected):
    assert solution.can_move_east(current, next) == expected

@pytest.mark.parametrize(
    "current, next, expected",
    [
        pytest.param('.', '.', False),
        pytest.param('S', '.', False),
        pytest.param('S', 'S', False),        
        pytest.param('S', '|', False),
        pytest.param('S', '7', False),
        pytest.param('S', 'J', False),

        pytest.param('S', '-', True),
        pytest.param('S', 'F', True),
        pytest.param('S', 'L', True),

        pytest.param('|', 'S', False),
        pytest.param('|', '|', False),
        pytest.param('|', '-', False),
        pytest.param('|', 'F', False),
        pytest.param('|', '7', False),
        pytest.param('|', 'L', False),
        pytest.param('|', 'J', False),

        pytest.param('-', 'S', True),
        pytest.param('-', '|', False),
        pytest.param('-', '-', True),
        pytest.param('-', 'F', True),
        pytest.param('-', '7', False),
        pytest.param('-', 'L', True),
        pytest.param('-', 'J', False),

        pytest.param('7', 'S', True),
        pytest.param('7', '|', False),
        pytest.param('7', '-', True),
        pytest.param('7', 'F', True),
        pytest.param('7', '7', False),
        pytest.param('7', 'L', True),
        pytest.param('7', 'J', False),

        pytest.param('J', 'S', True),
        pytest.param('J', '|', False),
        pytest.param('J', '-', True),
        pytest.param('J', 'F', True),
        pytest.param('J', '7', False),
        pytest.param('J', 'L', True),
        pytest.param('J', 'J', False),

        pytest.param('F', 'S', False),
        pytest.param('F', '|', False),
        pytest.param('F', '-', False),
        pytest.param('F', 'F', False),
        pytest.param('F', '7', False),
        pytest.param('F', 'L', False),
        pytest.param('F', 'J', False),

        pytest.param('L', 'S', False),
        pytest.param('L', '|', False),
        pytest.param('L', '-', False),
        pytest.param('L', 'F', False),
        pytest.param('L', '7', False),
        pytest.param('L', 'L', False),
        pytest.param('L', 'J', False),
    ],    
)
def test_can_move_west(current, next, expected):
    assert solution.can_move_west(current, next) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example-1.txt', 4),
        pytest.param('puzzle-input-example-1a.txt', 4),
        pytest.param('puzzle-input-example-2.txt', 8),
        pytest.param('puzzle-input-example-2a.txt', 8),
        pytest.param('puzzle-input-full.txt', 7145), 
    ],    
)
def test_solution(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param('puzzle-input-example-1.txt', 1),
        pytest.param('puzzle-input-example-1a.txt', 1),
        pytest.param('puzzle-input-part2-example-1.txt', 4),
        pytest.param('puzzle-input-part2-example-2.txt', 8),        
        #pytest.param('puzzle-input-part2-example-3.txt', 10),        
        #pytest.param('puzzle-input-full.txt', 0), 
    ],    
)
def test_solution_part2(filename, expected):
    assert solution.solve_part2(filename) == expected
