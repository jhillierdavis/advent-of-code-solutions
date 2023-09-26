import fileutils
import aoc_2021_day_07

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'

def test_cost():
    # Given:
    positions = fileutils.get_file_first_line_to_int_array(sample_file)
    
    # Then:
    assert aoc_2021_day_07.calcuate_cost_to_align_at_position(positions, 2) == 37

def test_calculate_least_cost_for_puzzle_input_sample():
    # Given:
    positions = fileutils.get_file_first_line_to_int_array(sample_file)
    
    # Then:
    assert aoc_2021_day_07.calculate_least_cost(positions) == 37

def test_calculate_least_cost_for_puzzle_input_full():
    # Given:
    positions = fileutils.get_file_first_line_to_int_array(full_file)
    
    # Then:
    assert aoc_2021_day_07.calculate_least_cost(positions) == 347011

def test_calculate_least_part2_cost_for_puzzle_input_sample():
    # Given:
    positions = fileutils.get_file_first_line_to_int_array(sample_file)
    
    # Then:
    assert aoc_2021_day_07.calculate_least_cost(positions, True) == 168

def test_calculate_least_part2_cost_for_puzzle_input_full():
    # Given:
    positions = fileutils.get_file_first_line_to_int_array(full_file)
    
    # Then:
    assert aoc_2021_day_07.calculate_least_cost(positions, True) == 98363777
