
import fileutils
import aoc_2021_day_06_part1
import aoc_2021_day_06_part2

sample_file = 'puzzle-input-sample.txt'
full_file = 'puzzle-input-full.txt'


def test_part1_exploration():
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days([3], 18) == 5
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days([4], 18) == 4
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days([1], 18) == 7
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days([2], 18) == 5

def test_part1_sample():
    # Given:
    initial_fish_ages = fileutils.get_file_first_line_to_int_array(sample_file)

    # Then:
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days(initial_fish_ages, 18) == 26
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days(initial_fish_ages, 80) == 5934

def test_part1_full():
    # Given:
    initial_fish_ages = fileutils.get_file_first_line_to_int_array(full_file)

    # Then:
    assert aoc_2021_day_06_part1.get_number_of_fish_after_elapsed_days(initial_fish_ages, 80) == 352151
    assert aoc_2021_day_06_part2.get_number_of_fish_after_elapsed_days(initial_fish_ages, 80) == 352151

def test_part2_sample():
    # Given:
    initial_fish_ages = fileutils.get_file_first_line_to_int_array(sample_file)

    # Then:
    assert aoc_2021_day_06_part2.get_number_of_fish_after_elapsed_days(initial_fish_ages, 256) == 26984457539

def test_part2_full():
    # Given:
    initial_fish_ages = fileutils.get_file_first_line_to_int_array(full_file)

    # Then:
    assert aoc_2021_day_06_part2.get_number_of_fish_after_elapsed_days(initial_fish_ages, 256) == 1601616884019