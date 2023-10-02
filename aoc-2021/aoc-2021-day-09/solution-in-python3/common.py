import grid2d
import point2d

def populate_heatmap_from_lines(input_lines):
    height = len(input_lines)
    width = len(input_lines[0])

    # print(f"DEBUG: width={width} height={height}")
    heatmap = grid2d.Grid2D(width, height)

    y = 0
    for line in input_lines:
        for x in range(width):
            point = point2d.Point2D(x, y)
            heatmap.setSymbol(point, line[x])
        y += 1

    return heatmap


def is_lowest_point(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> int:
    neighbours = heatmap.getCardinalPointNeighbours(point)

    current_value = int(heatmap.getSymbol(point))

    for neighbour in neighbours:
        if int(heatmap.getSymbol(neighbour)) <= current_value:
            return False
    return True


def get_lowest_points(heatmap):
    lowestpoints:[] = []
    for x in range(heatmap.getWidth()):
        for y in range(heatmap.getHeight()):
            point = point2d.Point2D(x,y)
            if is_lowest_point(heatmap, point):
                lowestpoints.append(point)
    return lowestpoints
