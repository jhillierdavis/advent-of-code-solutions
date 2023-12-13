import pytest

import solution

"""
In a spring sequence string, representing the condition of a set of springs (e.g. '.#.???.###'):

A '.' character represents an operational spring
A '#' character represents a damaged spring
A '?' character represents a unknown spring (could be either '.' or '#')
"""

@pytest.mark.parametrize(
    "condition_record,expected", 
    [
        pytest.param('#.#.###', [1,1,3]), 
        pytest.param('.#.###.#.######', [1,3,1,6]), 
        pytest.param('####.#...#...', [4,1,1]),
        pytest.param('#....######..#####.', [1,6,5]),
        pytest.param('.###.##....#', [3,2,1]),       
    ],    
)
def test_get_damaged_contiguous_spring_list_from_condition_record(condition_record, expected):
    # expected is a list where each entry is the length of contiguous damaged springs 
    assert solution.get_damaged_contiguous_spring_list_from_condition_record(condition_record) == expected


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


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param("???.###", "???.###????.###????.###????.###????.###"),
    ],    
)
def test_unfold_record(input, expected):
    assert solution.unfold_record(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param([1,1,3], [1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]),
    ],    
)
def test_unfold_grouping(input, expected):
    assert solution.unfold_grouping(input) == expected



@pytest.mark.parametrize(
    "record, unfold, expected",
    [
        pytest.param('???.### 1,1,3', False, 1),
        pytest.param('.??..??...?##. 1,1,3', False, 4),
        pytest.param('.?###????????. 3,2,1', False, 10),
        pytest.param('.??..??...?##. 1,1,3', True, 16384), # with unfolding
        pytest.param('?###???????? 3,2,1', True, 506250), # with unfolding
    ],    
)
def test_count_valid_arrangements_using_cache(record, unfold, expected):
    assert solution.count_valid_arrangements_using_cache(record, unfold) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 21),
        pytest.param("puzzle-input-full.txt", 7599),
    ],    
)
def test_solution_part1_using_cache(filename, expected):
    assert solution.solve_part1_using_cache(filename) == expected    


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 525152),
        pytest.param("puzzle-input-full.txt", 15454556629917),
    ],    
)
def test_solution_part2(filename, expected):
    assert solution.solve_part2(filename) == expected