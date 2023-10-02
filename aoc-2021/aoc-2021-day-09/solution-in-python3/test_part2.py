import point2d

import part2 as solution

import common

import pytest


""" @pytest.mark.parametrize(
    "lines,expected",
    [
        pytest.param(
            ["2199943210","3987894921","9856789892","8767896789","9899965678"], 3
        ),
    ],
)
def test_get_basin_size(lines, expected):
    heatmap = common.populate_heatmap_from_lines(lines)

    basin_points = solution.get_basin_points(heatmap, point2d.Point2D(1,0))
    assert len(basin_points) == expected
 """

def test_get_basin_size_top_right_basin():
    lines = ["2199943210","3987894921","9856789892","8767896789","9899965678"]

    heatmap = common.populate_heatmap_from_lines(lines)

    basin_points = solution.get_basin_points(heatmap, point2d.Point2D(9,0))
    assert len(basin_points) == 9

def test_get_basin_size_middle_basin():
    lines = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

    heatmap = common.populate_heatmap_from_lines(lines)

    basin_points = solution.get_basin_points(heatmap, point2d.Point2D(2,2))    
    assert len(basin_points) == 14


def test_part1():
    # When: Solved with example puzzle data
    assert solution.get_largest_basins_score("puzzle-input-example.txt") == 1134

    # Then: Also solved with full puzzle data
    assert solution.get_largest_basins_score("puzzle-input-full.txt") == 882942