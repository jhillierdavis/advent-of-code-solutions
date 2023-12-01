import pytest

import solution        

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('1abc2', 12),
        pytest.param('pqr3stu8vwx', 38),
        pytest.param('a1b2c3d4e5f', 15),
        pytest.param('treb7uchet', 77),
    ],    
)
def test_extract_number_from_string(input, expected):
    assert solution.extract_calibration_value_from_string(input) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('two1nine', 29),
        pytest.param('eightwothree', 83),
        pytest.param('abcone2threexyz', 13), 
        pytest.param('xtwone3four', 24), 
        pytest.param('4nineeightseven2', 42),
        pytest.param('zoneight234', 14), 
        pytest.param('7pqrstsixteen', 76),
        pytest.param('five', 55),       
        pytest.param('sevenmfpxvntvkpqvpbnnbpr5seven18sixeighteightwok',72),
    ],    
)
def test_extract_number_from_string_including_words(input, expected):
    assert solution.extract_calibration_value_from_string(input, False) == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 142),
        pytest.param('puzzle-input-full.txt', 54968),
    ],    
)
def test_part1_solution(input, expected):
    assert solution.extract_calibration_value_sum_from_file(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [        
        pytest.param('puzzle-input-example-part2.txt', 281),
        pytest.param('puzzle-input-full.txt', 54094),
    ],    
)
def test_part2_solution(input, expected):
    assert solution.extract_calibration_value_sum_from_file(input, False) == expected