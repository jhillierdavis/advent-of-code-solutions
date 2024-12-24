import pytest

import solution

input_example = "AOC-2024-Day-23_Puzzle-Input-Example.txt"
input_full = "AOC-2024-Day-23_Puzzle-Input-Full.txt"


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 12),
        pytest.param(input_full, 11011),
    ],    
)
def test_get_triple_connections(filename, expected):
    value = solution.get_triple_connections(filename)    
    assert expected == value


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 7),
        pytest.param(input_full, 1302),
    ],    
)
def test_solve_part1(filename, expected):
    value = solution.solve_part1(filename)
    
    assert expected == value


#@pytest.mark.skip
@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(input_example, 'co,de,ka,ta'),
        pytest.param(input_full, 'cb,df,fo,ho,kk,nw,ox,pq,rt,sf,tq,wi,xz'),
    ],    
)
def test_solve_part2(filename, expected):
    value = solution.solve_part2(filename)
    
    assert expected == value
