import pytest

import solution

input_example = "AOC-2025-Day-02_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-02_Puzzle-Input-Full.txt"


"""
@pytest.mark.parametrize(
    "id, expected",
    [
        pytest.param(10, True),
        pytest.param(11, False),
        pytest.param(22, False),
        pytest.param(95, True),
        pytest.param(99, False),
        pytest.param(115, True),
        pytest.param(222220, True),
        pytest.param(222224, True),
        pytest.param(222222, False),
        pytest.param(1188511885, False),
        pytest.param(1188511880, True),
        pytest.param(1188511890, True),
    ],    
)
def test_is_valid_id(id, expected):
    actual = solution.is_valid_id(id)    
    assert expected == actual
"""

    
@pytest.mark.parametrize(
    "id, expected",
    [
        pytest.param(10, False),
        pytest.param(11, True),
        pytest.param(22, True),
        pytest.param(95, False),
        pytest.param(99, True),
        pytest.param(115, False),
        pytest.param(222220, False),
        pytest.param(222224, False),
        pytest.param(222222, True),
        pytest.param(1188511885, True),
        pytest.param(1188511880, False),
        pytest.param(1188511890, False),
    ],    
)
def test_has_repeating_half(id, expected):
    actual = solution.has_repeating_half(id)    
    assert expected == actual


@pytest.mark.parametrize(
    "id, expected",
    [
        pytest.param(10, False),
        pytest.param(11, True),
        pytest.param(123123123, True), # (123 three times)
        pytest.param(1212121212, True), # (12 five times)
        pytest.param(1111111, True), # (1 seven times)
        pytest.param(2121212121, True),
    ],    
)
def has_repeating_sequences(id, expected):
    actual = solution.has_repeating_sequences(id)    
    assert expected == actual    


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
