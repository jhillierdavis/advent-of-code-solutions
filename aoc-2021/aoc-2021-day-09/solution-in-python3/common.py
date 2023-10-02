import grid2d
import point2d

def isPointOnGrid(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> bool:
    if point.getX() < 0:
        return False
    
    if point.getX() >= heatmap.getWidth():
        return False
    
    if point.getY() < 0:
        return False
    
    if point.getY() >= heatmap.getHeight():
        return False
    
    return True

def getValidConcentricNeighbours(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> list:
    neightbours =  getValidCompassPointNeighbours(heatmap, point)

    x = point.getX()
    y = point.getY()

    diagonal_left_bottom = point2d.Point2D(x-1, y-1)
    if isPointOnGrid(heatmap, diagonal_left_bottom):
        neightbours.append(diagonal_left_bottom)

    diagonal_right_bottom = point2d.Point2D(x+1, y-1)
    if isPointOnGrid(heatmap, diagonal_right_bottom):
        neightbours.append(diagonal_right_bottom)

    diagonal_left_top = point2d.Point2D(x-1, y+1)
    if isPointOnGrid(heatmap, diagonal_left_top):
        neightbours.append(diagonal_left_top)

    diagonal_right_top = point2d.Point2D(x+1, y+1)
    if isPointOnGrid(heatmap, diagonal_right_top):
        neightbours.append(diagonal_right_top)

    return neightbours


def getValidCompassPointNeighbours(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> list:
    neightbours = []

    x = point.getX()
    y = point.getY()
    left = point2d.Point2D(x-1, y)
    if isPointOnGrid(heatmap, left):
        neightbours.append(left)

    right = point2d.Point2D(x+1, y)           
    if isPointOnGrid(heatmap, right):
        neightbours.append(right)

    up = point2d.Point2D(x, y-1)
    if isPointOnGrid(heatmap, up):
        neightbours.append(up)

    down = point2d.Point2D(x, y+1)           
    if isPointOnGrid(heatmap, down):
        neightbours.append(down)

    return neightbours   

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
    neighbours = getValidCompassPointNeighbours(heatmap, point)

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
