import aoc_2021_day_02

# Ref: https://adventofcode.com/2021/day/2

def test_part1_puzzle_input_sample_result():
    result:int = aoc_2021_day_02.calculate_position_from_file('puzzle-input-sample.txt')
    assert result == 150

def test_part1_puzzle_input_full_result():
    result:int = aoc_2021_day_02.calculate_position_from_file('puzzle-input-full.txt')
    assert result == 1694130

def test_part2_puzzle_input_sample_result():
    result:int = aoc_2021_day_02.calculate_position_using_aim_from_file('puzzle-input-sample.txt')
    assert result == 900

def test_part2_puzzle_input_full_result():
    result:int = aoc_2021_day_02.calculate_position_using_aim_from_file('puzzle-input-full.txt')
    assert result == 1698850445    
