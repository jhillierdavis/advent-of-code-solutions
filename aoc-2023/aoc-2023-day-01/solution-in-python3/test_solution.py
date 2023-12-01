import pytest

import solution
from helpers import fileutils

def extract_number_from_string(input, digits_only=True):
    num_str = ""
    for i in range(len(input)):
        ch = input[i]
        if ch.isnumeric():
            num_str += ch
        elif digits_only == False:
             substr = input[i:]
             if (substr.startswith('one')):
                  num_str += '1'
             if (substr.startswith('two')):
                  num_str += '2'
             if (substr.startswith('three')):
                  num_str += '3'
             if (substr.startswith('four')):
                  num_str += '4'
             if (substr.startswith('five')):
                  num_str += '5'
             if (substr.startswith('six')):
                  num_str += '6'
             if (substr.startswith('seven')):
                  num_str += '7'
             if (substr.startswith('eight')):
                  num_str += '8'
             if (substr.startswith('nine')):
                  num_str += '9'

    length = len(num_str)

    if length == 1:
           num_str += num_str

    if length > 2:
           num_str = num_str[0] + num_str[length-1]

    #print(f"DEBUG: {num_str}")
    return int(num_str)
        

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
    assert extract_number_from_string(input) == expected

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
    ],    
)
def test_extract_number_from_string_including_words(input, expected):
    assert extract_number_from_string(input, False) == expected

def extract_first_and_last_numbers_from_file(filename, digits_only=True):
    lines = fileutils.get_file_lines(filename)

    ans = 0
    for l in lines:
         ans += extract_number_from_string(l, digits_only)
    return ans     


@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param('puzzle-input-example.txt', 142),
        pytest.param('puzzle-input-full.txt', 54968),
    ],    
)
def test_part1_solution(input, expected):
    assert extract_first_and_last_numbers_from_file(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [        
        pytest.param('puzzle-input-example-part2.txt', 281),
        pytest.param('puzzle-input-full.txt', 54094),
    ],    
)
def test_part2_solution(input, expected):
    assert extract_first_and_last_numbers_from_file(input, False) == expected