import pytest

import solution

input_example = "AOC-2024-Day-19_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-19_Puzzle-Input-Full.txt"



#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "towel_pattern, design, expected",
    [
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'brwrr', True), # br + wr + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bggr', True), # b + g + g + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'gbbr', True), # g + b + b + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'rrbgbr', True), # r + rb + g + br
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'ubwu', False), # no u
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bwurrg', True),
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'brgr', True), 
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bbrgwb', False), 
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'w', False), 
    ],    
)
def test_is_possible_design(towel_pattern, design, expected):
    value = solution.is_possible_design(towel_pattern, design)   
    assert expected == value

#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "towel_pattern, design, expected",
    [
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'brwrr', True), # br + wr + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bggr', True), # b + g + g + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'gbbr', True), # g + b + b + r
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'rrbgbr', True), # r + rb + g + br
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'ubwu', False), # no u
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bwurrg', True),
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'brgr', True), 
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'bbrgwb', False), 
        pytest.param('r, wr, b, g, bwu, rb, gb, br', 'w', False), 
    ],    
)
def test_has_patterns(towel_pattern, design, expected):
    patterns = towel_pattern.split(', ')
    value = solution.has_patterns(patterns, design)   
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 6),
        pytest.param(input_full, 293), # 318 too high! , # 277 too low!
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)   
    assert expected == value


#@pytest.mark.skip(reason="TODO: Ignore until implemented")
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 16),
        pytest.param(input_full, 623924810770264),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)    
    assert expected == value