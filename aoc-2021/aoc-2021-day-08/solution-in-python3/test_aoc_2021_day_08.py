import aoc_2021_day_08 as solution

# Puzzle data
example_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

# List of counts of segments used for unique digial display (for digits 1, 7, 4 and 8) 
list_word_sizes_to_match = [2,3,4,7]

def test_part1_count_words_by_length():
    # Match correct number of 'words' (instruction segments) for unique digital display in output line
    assert solution.count_words_by_length("fdgacbe cefdb cefbgd gcbe", list_word_sizes_to_match) == 2
    assert solution.count_words_by_length("fcgedb cgb dgebacf gc", list_word_sizes_to_match) == 3
    assert solution.count_words_by_length("cg cg fdcagb cbg", list_word_sizes_to_match) == 3


def test_part1_count_unique_instructions_in_puzzle_input():
    # Match correct number of 'words' (instruction segments) for unique digital display in each output line in data file

    # Solution using example data
    assert solution.count_words_by_length_from_file(example_file, list_word_sizes_to_match) == 26

    # Solution using full (personalised) data
    assert solution.count_words_by_length_from_file(full_file, list_word_sizes_to_match) == 362