import pytest # for parameterised tests

import part2 as solution
import common
import point2d

@pytest.mark.parametrize(
    "low_point,expected",
    [
        pytest.param(
            point2d.Point2D(1,0), 3
        ),
        pytest.param(
            point2d.Point2D(9,0), 9
        ),
        pytest.param(
            point2d.Point2D(2,2), 14
        ),
    ],
)
def test_get_basin_size(low_point, expected):
    # Given: a heatmap grid
    lines = ["2199943210","3987894921","9856789892","8767896789","9899965678"]    
    heatmap = common.populate_heatmap_from_lines(lines)

    # When: the basin points are determined (around the low point specified)
    basin_points = solution.get_basin_points(heatmap, low_point)

    # Then: the expected number of basin points are identified
    assert len(basin_points) == expected


@pytest.mark.parametrize(
    "filename,expected",
    [
        pytest.param(
            "puzzle-input-example.txt", 1134
        ),
        pytest.param(
            "puzzle-input-full.txt", 882942
        ),
    ],
)
def test_part2_solution(filename, expected):
    assert solution.get_largest_basins_score(filename) == expected