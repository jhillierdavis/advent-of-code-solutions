import pytest

import solution
from helpers import fileutils

def extract_number_from_string(input):
    num_str = ""
    for i in range(len(input)):
        ch = input[i]
        if ch.isnumeric():
            num_str += ch

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
        pytest.param('puzzle-input-example.txt', 142),
        pytest.param('puzzle-input-full.txt', 54968),
    ],    
)
def test_solution(input, expected):
    lines = fileutils.get_file_lines(input)
    #print(f"DEBUG: {lines}")

    ans = 0
    for l in lines:
         ans += extract_number_from_string(l)

    assert ans == expected
