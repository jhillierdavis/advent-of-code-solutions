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
    "input_a, input_b, expected",
    [
        pytest.param("19, 13, 30 @ -2, 1, -2", "18, 19, 22 @ -1, -1, -2", (14.333, 15.333)),
        pytest.param("19, 13, 30 @ -2, 1, -2", "20, 25, 34 @ -2, -2, -4", (11.667, 16.667)),
        pytest.param("19, 13, 30 @ -2, 1, -2", "12, 31, 28 @ -1, -2, -1", (6.2, 19.4)),
        pytest.param("19, 13, 30 @ -2, 1, -2", "20, 19, 15 @ 1, -5, -3", (21.444, 11.778)),
        pytest.param("18, 19, 22 @ -1, -1, -2", "20, 25, 34 @ -2, -2, -4", None), # Parallel lines!
        pytest.param("18, 19, 22 @ -1, -1, -2", "12, 31, 28 @ -1, -2, -1", (-6, -5)),
        pytest.param("18, 19, 22 @ -1, -1, -2", "20, 19, 15 @ 1, -5, -3", (19.667, 20.667)),
        pytest.param("20, 25, 34 @ -2, -2, -4", "12, 31, 28 @ -1, -2, -1", (-2.0, 3.0)),
        pytest.param("20, 25, 34 @ -2, -2, -4", "20, 19, 15 @ 1, -5, -3", (19.0, 24.0)),
        pytest.param("12, 31, 28 @ -1, -2, -1", "20, 19, 15 @ 1, -5, -3", (16.0, 39.0)),
    ],    
)
def test_get_hailstone_from(input_a, input_b, expected):
    ha = solution.get_hailstone_from(input_a)
    hb = solution.get_hailstone_from(input_b)

    assert solution.get_hailstone_intersection_point(ha, hb) == expected


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        pytest.param("19, 13, 30 @ -2, 1, -2", "18, 19, 22 @ -1, -1, -2", True),
        pytest.param("19, 13, 30 @ -2, 1, -2", "20, 25, 34 @ -2, -2, -4", True),
        pytest.param("19, 13, 30 @ -2, 1, -2", "12, 31, 28 @ -1, -2, -1", True),
        pytest.param("19, 13, 30 @ -2, 1, -2", "20, 19, 15 @ 1, -5, -3", False),
        pytest.param("18, 19, 22 @ -1, -1, -2", "20, 25, 34 @ -2, -2, -4", False), # Parallel lines!
        pytest.param("18, 19, 22 @ -1, -1, -2", "12, 31, 28 @ -1, -2, -1", True),
        pytest.param("18, 19, 22 @ -1, -1, -2", "20, 19, 15 @ 1, -5, -3", False),
        pytest.param("20, 25, 34 @ -2, -2, -4", "12, 31, 28 @ -1, -2, -1", True),
        pytest.param("20, 25, 34 @ -2, -2, -4", "20, 19, 15 @ 1, -5, -3", False),
        pytest.param("12, 31, 28 @ -1, -2, -1", "20, 19, 15 @ 1, -5, -3", False),
    ],    
)
def test_have_future_intersection(input_a, input_b, expected):
    ha = solution.get_hailstone_from(input_a)
    hb = solution.get_hailstone_from(input_b)

    assert solution.have_future_intersection(ha, hb) == expected


@pytest.mark.parametrize(
    "filename, target_min, target_max, expected",
    [
        pytest.param("puzzle-input-example.txt", 7, 27, 2),
        pytest.param("puzzle-input-full.txt", 200000000000000, 400000000000000, 19523),
    ],    
)
def test_solve_part1(filename, target_min, target_max, expected):
    assert solution.solve_part1(filename, target_min, target_max) == expected

@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", -1),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    