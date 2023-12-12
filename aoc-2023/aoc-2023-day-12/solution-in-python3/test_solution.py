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
def test_count_valid_arrangements_using_brute_force(input, expected):
    assert solution.count_valid_arrangements_using_brute_force(input) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 21),
        #pytest.param("puzzle-input-full.txt", 7599), # Rather slow (~ 1 minute)
    ],    
)
def test_solution_part1(filename, expected):
    assert solution.solve_part1(filename) == expected



@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('???.###', ['???','###']),
        pytest.param('.??..??...?##.', ['??','??','?##']),
        pytest.param('?###????????', ['?###????????']),
        pytest.param('?#?#?#?#?#?#?#?', ['?#?#?#?#?#?#?#?']),
    ],    
)
def test_get_chunks(input, expected):
    assert solution.get_chunks(input) == expected


@pytest.mark.parametrize(
    "chunk, hash_pattern, expected_combo_count",
    [
        pytest.param('???', [4], 0), # Not valid        
        pytest.param('???', [3], 1), # ??? -> ###
        pytest.param('???', [2], 2), # ??? -> .## or ##.
        pytest.param('???', [1,1], 1), # ??? -> #.#
        pytest.param('?###????????', [3,2,1], 10),
    ],    
)
def test_get_combo_count_for_chunk_and_hash_pattern(chunk, hash_pattern, expected_combo_count):
    assert solution.get_combo_count_for_chunk_and_hash_pattern(chunk, hash_pattern) == expected_combo_count


"""
@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('???.### 1,1,3', 1),
        #pytest.param('.??..??...?##. 1,1,3', 16384), # Too slow!
        #pytest.param('?###???????? 3,2,1', 506250),
    ],    
)
def test_count_valid_arrangements_with_unfolding(input, expected):
    assert solution.count_valid_arrangements_with_unfolding(input) == expected
"""

"""
@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 525152),
        #pytest.param("puzzle-input-full.txt", 0),
    ],    
)
def test_solution_part2(filename, expected):
    assert solution.solve_part2(filename) == expected
"""

"""
@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('???.### 1,1,3', 1),
        pytest.param('.??..??...?##. 1,1,3', 4),
        pytest.param('?###???????? 3,2,1', 10),
    ],    
)
def test_count_valid_arrangements_using_caching(input, expected):
    assert solution.count_valid_arrangements_using_brute_force(input) == expected
"""