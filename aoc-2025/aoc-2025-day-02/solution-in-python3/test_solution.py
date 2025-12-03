import pytest

import solution, ai_solution

input_example = "AOC-2025-Day-02_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-02_Puzzle-Input-Full.txt"

    
#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 1227775554),
        pytest.param(input_full, 12850231731),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value

    # Repeat with AI generated code
    value = ai_solution.solve_part1(filename)    
    assert expected == value



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4174379265),
        pytest.param(input_full, 24774350322),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value

    # Repeat with AI generated code
    value = ai_solution.solve_part2(filename)    
    assert expected == value
    



"""
AI Prompt:

Create a parameterised test using PyTest for the function ....
"""

@pytest.mark.parametrize(
    "num, expected",
    [
        (55, True),       # "5" repeated twice
        (6464, True),     # "64" repeated twice
        (123123, True),   # "123" repeated twice
        (1234, False),    # halves "12" vs "34" differ
        (1212, True),     # "12" repeated twice
        (111, False),     # odd length, cannot split evenly
    ]
)
def test_is_double_half(num, expected):
    assert ai_solution.is_double_half(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        (55, True),            # "5" repeated
        (6464, True),          # "64" repeated
        (123123, True),        # "123" repeated
        (2121212121, True),    # "21" repeated
        (1234, False),         # not repeating
        (777777, True),        # "7" repeated 6 times
        (12341234, True),      # "1234" repeated twice
        (101010, True),        # "10" repeated 3 times
        (1231231234, False),   # not fully repeating
        (1, False),            # single digit cannot repeat
    ]
)
def test_is_repeating_sequence(num, expected):
    assert ai_solution.is_repeating_sequence(num) == expected
