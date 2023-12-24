import pytest

import solution


@pytest.mark.parametrize(
    "input, expected",
    [
        pytest.param("19, 13, 30 @ -2, 1, -2", [19,13,30,-2,1,-2]),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_get_hailstone_from(input, expected):
    h = solution.get_hailstone_from(input)
    assert h

    assert h.position.get_x() == expected[0]
    assert h.position.get_y() == expected[1]
    assert h.position.get_z() == expected[2]

    assert h.velocity.get_x() == expected[3]
    assert h.velocity.get_y() == expected[4]
    assert h.velocity.get_z() == expected[5]


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
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