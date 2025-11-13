import pytest

import solution


@pytest.mark.parametrize(
    "input, nth, expected",
    [
        pytest.param([0,3,6], 1, 0),
        pytest.param([0,3,6], 2, 3),
        pytest.param([0,3,6], 3, 6),
        pytest.param([0,3,6], 4, 0),
        pytest.param([0,3,6], 5, 3),
        pytest.param([0,3,6], 6, 3),
        pytest.param([0,3,6], 2020, 436),
        pytest.param([1,3,2], 2020, 1),
        pytest.param([2,1,3], 2020, 10),
        pytest.param([1,2,3], 2020, 27),
        pytest.param([2,3,1], 2020, 78),
        pytest.param([3,2,1], 2020, 438),
        pytest.param([3,1,2], 2020, 1836),
        pytest.param([15,12,0,14,3,1], 2020, 249),
    ],    
)
def test_solve_part1(input, nth, expected):
    value = solution.solve(input, nth)    
    assert expected == value


@pytest.mark.parametrize(
    "input, nth, expected",
    [
        pytest.param([0,3,6], 30000000, 175594),
        pytest.param([1,3,2], 30000000, 2578),
        pytest.param([2,1,3], 30000000, 3544142),
        pytest.param([1,2,3], 30000000, 261214),
        pytest.param([2,3,1], 30000000, 6895259),
        pytest.param([3,2,1], 30000000, 18),
        pytest.param([3,1,2], 30000000, 362),
        pytest.param([15,12,0,14,3,1], 30000000, 41687),
    ],    
)
def test_solve_part2(input, nth, expected):
    value = solution.solve(input, nth)
    assert expected == value
