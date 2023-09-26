import aoc_2021_day_05

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_count_points_of_line_overlap_for_puzzle_input_sample():
    assert aoc_2021_day_05.count_points_of_line_overlap_from_file(sample_file) == 5

#def test_count_points_of_line_overlap_for_puzzle_input_full():
#   assert aoc_2021_day_05.count_points_of_line_overlap_from_file(full_file) == 5608

def test_count_points_of_line_overlap_including_diagonals_for_puzzle_input_sample():
    assert aoc_2021_day_05.count_points_of_line_overlap_including_diagonals_from_file(sample_file) == 12

