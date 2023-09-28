import aoc_2021_day_08

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_part1_count_words_by_length():
    # Given:
    list_word_sizes_to_match = [2,3,4,7]

    # Then:
    assert aoc_2021_day_08.count_words_by_length("fdgacbe cefdb cefbgd gcbe", list_word_sizes_to_match) == 2
    assert aoc_2021_day_08.count_words_by_length("fcgedb cgb dgebacf gc", list_word_sizes_to_match) == 3
    assert aoc_2021_day_08.count_words_by_length("cg cg fdcagb cbg", list_word_sizes_to_match) == 3


def test_part1_count_unique_instructions_in_puzzle_input():
    # Given:
    list_word_sizes_to_match = [2,3,4,7]

    # Then:
    assert aoc_2021_day_08.count_words_by_length_from_file(sample_file, list_word_sizes_to_match) == 26
    assert aoc_2021_day_08.count_words_by_length_from_file(full_file, list_word_sizes_to_match) == 362
    
def test_part2_single_line_example():
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |cdfeb fcadb cdfeb cdbaf"
    assert aoc_2021_day_08.decipher_output_values(input) == 5353


def test_part2_sample():    
    assert aoc_2021_day_08.decipher_total_from_file(sample_file) == 61229 
    assert aoc_2021_day_08.decipher_total_from_file(full_file) == 1020159    