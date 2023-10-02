import fileutils
import grid2d
import fileutils
import common


def sum_lowest_points(heatmap:grid2d.Grid2D) -> int:
    lowestpoints = common.get_lowest_points(heatmap)

    sum = 0
    for lowpoint in lowestpoints:
        value = heatmap.getSymbol(lowpoint)
        sum += int(value) + 1
    return sum


def sum_low_points_from_file(filename) -> int:
    lines = fileutils.get_file_lines(filename)

    heatmap = common.populate_heatmap_from_lines(lines)

    return sum_lowest_points(heatmap)