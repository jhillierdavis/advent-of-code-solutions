import pytest

import solution

input_example = "AOC-2024-Day-07_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-07_Puzzle-Input-Full.txt"


@pytest.mark.parametrize(
    "alpha, beta, expected",
    [
        pytest.param(1,2,12),
        pytest.param(12,345,12345),
    ],    
)
def test_concatonate(alpha, beta, expected):
    assert expected == solution.concatonate(alpha, beta)


@pytest.mark.parametrize(
    "values, result, expected",
    [
        pytest.param([0,1],1,True),
        pytest.param([15,6],156,True),        
        pytest.param([6,8,6,15],7290,True),
        pytest.param([17,8,14],192,True),
        pytest.param([34, 79, 78, 217, 6],2987,True),
        pytest.param([633, 5, 5],3170,True),
        pytest.param([7, 1, 9], 19, False),
        pytest.param([7, 1, 9, 701], 720, False),
        pytest.param([7, 1, 9, 701, 797],1517,False)
    ],    
)
def test_is_possible_equation_with_concatonation(values, result, expected):
    assert expected == solution.is_possible_equation_with_concatonation(values, result)    


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 3749),
        pytest.param(input_full, 7885693428401),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 11387),
        pytest.param(input_full, 348360680516005), # 7887657898042 too low, 348360680517522 too high!
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
