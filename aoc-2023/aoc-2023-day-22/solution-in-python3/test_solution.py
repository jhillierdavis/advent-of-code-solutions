import pytest

import solution

@pytest.mark.parametrize(
    "cube_a, cube_b, expected",
    [
        pytest.param((0,0,0), (0,0,0), True),
        pytest.param((1,2,3), (1,2,3), True),
        pytest.param((1,0,0), (0,0,0), False),
        pytest.param((1,1,1), (0,0,0), False),
        pytest.param((1,2,3), (3,2,1), False),
    ],    
)
def test_is_same_cube(cube_a, cube_b, expected):
    assert solution.is_same_cube(cube_a, cube_b) == expected


@pytest.mark.parametrize(
    "block, expected",
    [
        pytest.param([(0,0,0), (1,0,0), (2,0,0)], True),
        pytest.param([(0,0,1), (1,0,1), (2,0,1)], True),
        pytest.param([(0,0,4), (1,0,3), (2,0,2)], False),
        pytest.param([(1,1,9), (2,1,9), (3,1,9)], False),
    ],    
)
def test_is_block_grounded(block, expected):
    assert solution.is_block_grounded(block) == expected


@pytest.mark.parametrize(
    "block_a, block_b, expected",
    [
        pytest.param([(0,0,0), (1,0,0), (2,0,0)], [(0,0,0), (0,1,0), (0,2,0)], True),
        pytest.param([(1, 0, 1), (1, 1, 1), (1, 2, 1)], [(0, 0, 1), (1, 0, 1), (2, 0, 1)], True),
        pytest.param([(0,0,0), (1,0,0), (2,0,0)], [(0,1,0), (1,1,0), (2,1,0)], False),
        pytest.param([(1, 0, 1), (1, 1, 1), (1, 2, 1)], [(0, 0, 2), (1, 0, 2), (2, 0, 2)], False),
    ],    
)
def test_has_block_intersection(block_a, block_b, expected):
    assert solution.has_block_intersection(block_a, block_b) == expected


@pytest.mark.parametrize(
    "block, expected",
    [
        pytest.param([(0,0,2), (1,0,2), (2,0,2)], [(0,0,1), (1,0,1), (2,0,1)]),
        pytest.param([(1,1,4), (1,1,3), (1,1,2)], [(1,1,3), (1,1,2), (1,1,1)]),        
    ],    
)
def test_get_block_shifted_down(block, expected):
    assert solution.get_block_shifted_down(block) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 9),
    ],    
)
def test_get_max_height_from(filename, expected):
    blocks = solution.get_blocks_from(filename)

    assert solution.get_max_block_height_from(blocks) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", [[(1, 0, 1), (1, 1, 1), (1, 2, 1)],[(0, 0, 2), (1, 0, 2), (2, 0, 2)],[(0, 2, 2), (1, 2, 2), (2, 2, 2)],[(0, 0, 3), (0, 1, 3), (0, 2, 3)],[(2, 0, 3), (2, 1, 3), (2, 2, 3)],[(0, 1, 4), (1, 1, 4), (2, 1, 4)],[(1, 1, 5), (1, 1, 6)]]),
    ],    
)
def test_move_until_stable_from(filename, expected):
    assert solution.move_until_stable_from(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param("puzzle-input-example.txt", 5),
        pytest.param("puzzle-input-full.txt", 434), # not 730! # 754 too high! # 1235 too high!
    ],    
)
def test_solve_part1(filename, expected):
    assert solution.solve_part1(filename) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        #pytest.param("puzzle-input-example.txt", 7),
        #pytest.param("puzzle-input-full.txt", -1),
    ],    
)
def test_solve_part2(filename, expected):
    assert solution.solve_part2(filename) == expected    