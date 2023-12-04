import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 4),
        pytest.param('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', 2),
        pytest.param('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', 2),
        pytest.param('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', 1),
        pytest.param('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', 0),
        pytest.param('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11', 0),
    ],    
)
def test_foo(input, expected):
     assert solution.get_card_matches_from_string(input) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 13),
        pytest.param('puzzle-input-full.txt', 26914), # Not 1538
    ],    
)
def test_solution_part1(input, expected):
    assert solution.solve_part1(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 30),
        pytest.param('puzzle-input-full.txt', 13080971),
    ],    
)
def test_solution_part2(input, expected):
    assert solution.solve_part2(input) == expected    