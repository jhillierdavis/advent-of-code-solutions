import pytest

import solution


@pytest.mark.parametrize(
    "input, expected, nth",
    [
        pytest.param([0,3,6], 0, 1),
        pytest.param([0,3,6], 3, 2),
        pytest.param([0,3,6], 6, 3),
        pytest.param([0,3,6], 0, 4),
        pytest.param([0,3,6], 3, 5),
        pytest.param([0,3,6], 3, 6),
        pytest.param([0,3,6], 436, 2020),
        pytest.param([1,3,2], 1, 2020),
        pytest.param([2,1,3], 10, 2020),
        pytest.param([1,2,3], 27, 2020),
        pytest.param([2,3,1], 78, 2020),
        pytest.param([3,2,1], 438, 2020),
        pytest.param([3,1,2], 1836, 2020),
        pytest.param([15,12,0,14,3,1], 249, 2020),
    ],    
)
def test_solve_part1(input, expected, nth):
    value = solution.solve_part1(input, nth)    
    assert expected == value

@pytest.mark.parametrize(
    "input, expected, nth",
    [
        pytest.param([0,3,6], 0, 1),
        pytest.param([0,3,6], 3, 2),
        pytest.param([0,3,6], 6, 3),
        pytest.param([0,3,6], 0, 4),
        pytest.param([0,3,6], 3, 5),
        pytest.param([0,3,6], 3, 6),
        pytest.param([0,3,6], 436, 2020),
        pytest.param([1,3,2], 1, 2020),
        pytest.param([2,1,3], 10, 2020),
        pytest.param([1,2,3], 27, 2020),
        pytest.param([2,3,1], 78, 2020),
        pytest.param([3,2,1], 438, 2020),
        pytest.param([3,1,2], 1836, 2020),
        pytest.param([15,12,0,14,3,1], 249, 2020),
        pytest.param([0,3,6], 175594, 30000000),
        pytest.param([1,3,2], 2578, 30000000),
        pytest.param([2,1,3], 3544142, 30000000),
        pytest.param([1,2,3], 261214, 30000000),
        pytest.param([2,3,1], 6895259, 30000000),
        pytest.param([3,2,1], 18, 30000000),
        pytest.param([3,1,2], 362, 30000000),
        pytest.param([15,12,0,14,3,1], 41687, 30000000),
    ],    
)
def test_solve_part2(input, expected, nth):
    value = solution.solve_part2(input, nth)
    assert expected == value
