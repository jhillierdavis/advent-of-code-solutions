import pytest

import solution

@pytest.mark.parametrize(
    "input,expected",
    [
        pytest.param([(1,0,1),(1,2,1)], True),
        pytest.param([(0,0,2),(2,0,2)], False),
    ],    
)
def test_block_is_grounded(input, expected):
    b = solution.Block(input[0], input[1])
    assert b.is_grounded() == expected

BLOCK_A = [(1,0,1),(1,2,1)]
BLOCK_B = [(0,0,2),(2,0,2)]
BLOCK_C = [(0,2,3),(2,2,3)]
BLOCK_D = [(0,0,4),(0,2,4)]
BLOCK_E = [(2,0,5),(2,2,5)]
BLOCK_F = [(0,1,6),(2,1,6)]
BLOCK_G = [(1,1,8),(1,1,9)]

@pytest.mark.parametrize(
    "input1,input2,expected",
    [
        pytest.param(BLOCK_A, BLOCK_B, True), # Block A supports B        
        pytest.param(BLOCK_E, BLOCK_F, True), 
        pytest.param(BLOCK_F, BLOCK_G, False),
        pytest.param(BLOCK_B, BLOCK_A, False), 
        pytest.param(BLOCK_C, BLOCK_A, False), 
        pytest.param(BLOCK_C, BLOCK_B, False), 
        pytest.param(BLOCK_D, BLOCK_E, False), 
    ],    
)
def test_block_is_supporting(input1, input2, expected):
    b1 = solution.Block(input1[0], input1[1])
    b2 = solution.Block(input2[0], input2[1])

    assert b1.is_supporting(b2) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 5),
        pytest.param("puzzle-input-full.txt", -1), # 754 too high! # 1235 too high!
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    