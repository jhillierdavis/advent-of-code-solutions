import aoc_2021_day_03
import utils

# Ref: https://adventofcode.com/2021/day/2

def test_part1_puzzle_input_sample_result():
    # gamma_rate:int = aoc_2021_day_03.get_gamma_rate('puzzle-input-sample.txt')
    # assert "10110" == gamma_rate
    
    # gamma_rate_int_value = utils.decimal_value_of_binary_string(gamma_rate)
    # assert  gamma_rate_int_value == 22

    # epsilon_rate = aoc_2021_day_03.get_epsilon_rate_from_gamma_rate(gamma_rate)
    # assert "01001" == epsilon_rate

    # epsilon_rate_int_value = utils.decimal_value_of_binary_string(epsilon_rate)
    # assert epsilon_rate_int_value == 9

    # power_consumption = gamma_rate_int_value * epsilon_rate_int_value
    # assert power_consumption == 198

    power_consumption = aoc_2021_day_03.get_power_consumption_from_file('puzzle-input-sample.txt')
    assert power_consumption == 198

def test_part1_puzzle_input_full_result():
    power_consumption = aoc_2021_day_03.get_power_consumption_from_file('puzzle-input-full.txt')
    assert power_consumption == 852500    

def test_get_oxygen_generator_rating():
    entries = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    assert aoc_2021_day_03.get_oxygen_generator_rating(entries) == 23

def test_part2_puzzle_input_sample_result():
    result:int = aoc_2021_day_03.get_life_support_rating('puzzle-input-sample.txt')
    assert result == 230

def test_part2_puzzle_input_full_result():
     result:int = aoc_2021_day_03.get_life_support_rating('puzzle-input-full.txt')
     assert result == 1007985 
