import pytest

import solution

input_example = "AOC-2025-Day-06_Puzzle-Input-Example.txt"
input_full = "AOC-2025-Day-06_Puzzle-Input-Full.txt"


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 4277556),
        pytest.param(input_full, 6169101504608),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)    
    assert expected == value


@pytest.mark.parametrize(
    "num, expected",
    [
        pytest.param(123, [1,2,3]),
        pytest.param(431, [4,3,1]),        
    ],    
)
def test_split_by_tens(num, expected):
    actual = solution.split_by_tens(num)
    assert actual == expected

"""
@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([123, 45, 6], [356, 24, 1]),
        pytest.param([328, 64, 98], [8,248,369]),
        #pytest.param([328, 64, 98], [8,248,369]),            
    ],    
)
def test_convert(nums, expected):
    actual = solution.convert(nums)
    assert actual == expected
"""

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3263827),
        pytest.param(input_full, 10442199710797),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value
