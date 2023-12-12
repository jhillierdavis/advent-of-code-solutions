import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('#.#.###', [1,1,3]),
        pytest.param('.#.###.#.######', [1,3,1,6]), 
        pytest.param('####.#...#...', [4,1,1]),
        pytest.param('#....######..#####.', [1,6,5]),
        pytest.param('.###.##....#', [3,2,1]),       
    ],    
)
def test_list_broken_springs(input, expected):
    assert solution.list_broken_springs(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('???.### 1,1,3', 1),
        pytest.param('.??..??...?##. 1,1,3', 4),
        pytest.param('?###???????? 3,2,1', 10),
    ],    
)
def test_count_valid_arrangements(input, expected):
    assert solution.count_valid_arrangements(input) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 21),
        pytest.param("puzzle-input-full.txt", 7599),
    ],    
)
def test_solution_part1(filename, expected):
    assert solution.solve_part1(filename) == expected
