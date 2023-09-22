import aoc_2021_day_01

def test_part1_puzzle_input_sample_result():
    result:int = aoc_2021_day_01.count_sequential_increases_from_file('puzzle-input-sample.txt')
    assert result == 7

def test_part1_puzzle_input_full_result():
    result:int = aoc_2021_day_01.count_sequential_increases_from_file('puzzle-input-full.txt')
    assert result == 1448   

def test_part2_puzzle_input_sample_result():
    result:int = aoc_2021_day_01.count_sliding_window_increases_from_file('puzzle-input-sample.txt')
    assert result == 5

def test_part2_puzzle_input_full_result():
    result:int = aoc_2021_day_01.count_sliding_window_increases_from_file('puzzle-input-full.txt')
    assert result == 1471
