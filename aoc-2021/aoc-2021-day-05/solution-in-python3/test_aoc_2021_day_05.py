import aoc_2021_day_05

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_part1_with_puzzle_input_sample():
    assert aoc_2021_day_05.count_points_of_line_overlap_from_file(sample_file) == 5

def test_part1_with_puzzle_input_full():
   assert aoc_2021_day_05.count_points_of_line_overlap_from_file(full_file) == 5608

def test_part2_with_puzzle_input_sample():
    assert aoc_2021_day_05.count_points_of_line_overlap_including_diagonals_from_file(sample_file) == 12

def test_part2_with_puzzle_input_full():
    assert aoc_2021_day_05.count_points_of_line_overlap_including_diagonals_from_file(full_file) == 20299 
