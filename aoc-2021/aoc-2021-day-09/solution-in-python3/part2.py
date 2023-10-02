import grid2d
import point2d
import fileutils
import common

def is_basin_value(heatmap:grid2d.Grid2D, point) -> bool:
    value = int(heatmap.getSymbol(point))
    if value == 9:
        return False
    return True

def get_basin_points(heatmap:grid2d.Grid2D, point:point2d.Point2D, existing_basin_points:set=None):
    if None == existing_basin_points:
        existing_basin_points = set()

    if not is_basin_value(heatmap, point):
        return set() # Empty set
    
    existing_basin_points.add(point)

    neighbours = common.getValidCompassPointNeighbours(heatmap, point)

    for neighbour in neighbours:
        if neighbour not in existing_basin_points:
            additional_basin_points = get_basin_points(heatmap, neighbour, existing_basin_points)
            for additional in additional_basin_points:
                if is_basin_value(heatmap, additional):
                    existing_basin_points.add(additional)    
            if is_basin_value(heatmap, neighbour):
                existing_basin_points.add(neighbour)        

    return existing_basin_points

def get_largest_basins_score(filename):
    lines = fileutils.get_file_lines(filename)
    heatmap = common.populate_heatmap_from_lines(lines)

    lowest_points = common.get_lowest_points(heatmap)
    #lowest_points = [ point2d.Point2D(9,0) ]

    print(f"DEBUG: lowest_points={lowest_points}")

    basin_sizes = []
    for lowest_point in lowest_points:
        basin_points = get_basin_points(heatmap, lowest_point)
        basin_size = len(basin_points)
        print(f"DEBUG: lowest_point={lowest_point} basin_size={basin_size}")
        basin_sizes.append(basin_size)

    sorted_basin_sizes = sorted(basin_sizes, reverse=True)
    print(f"DEBUG: sorted_basin_sizes={sorted_basin_sizes}")

    score = 1
    i = 0
    for size in sorted_basin_sizes:
        score *= size
        i += 1
        if i >= 3:
            break
    return score