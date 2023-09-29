import grid2d
import point2d

import fileutils

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

def getNeighbours(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> list:
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

def isLowestPoint(heatmap:grid2d.Grid2D, point:point2d.Point2D) -> int:
    neighbours = getNeighbours(heatmap, point)

    current_value = int(heatmap.getSymbol(point))

    for neighbour in neighbours:
        if int(heatmap.getSymbol(neighbour)) <= current_value:
            return False
    return True

def sum_low_points(heatmap:grid2d.Grid2D) -> int:

    sum = 0
    for x in range(heatmap.getWidth()):
        for y in range(heatmap.getHeight()):
            point = point2d.Point2D(x,y)
            if isLowestPoint(heatmap, point):
                value = heatmap.getSymbol(point)
                sum += int(value) + 1
    return sum

def sum_low_points_from_file(filename) -> int:
    lines = fileutils.get_file_lines(filename)

    height = len(lines)
    width = len(lines[0])

    print(f"DEBUG: width={width} height={height}")
    heatmap = grid2d.Grid2D(width, height)

    y = 0
    for line in lines:
        for x in range(width):
            point = point2d.Point2D(x, y)
            heatmap.setSymbol(point, line[x])
        y += 1

    return sum_low_points(heatmap)