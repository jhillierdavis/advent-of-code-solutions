import utils
import parser
import grid2d
import point2d

def setGridValue(grid:grid2d.Grid2D, coord:point2d.Point2D):
    sym = grid.getSymbol(coord)
    if type(sym) is int:
        grid.setSymbol(coord, 1 + sym)
    else:
        grid.setSymbol(coord, 1)    

def displayGrid(grid):
    print(f"DEBUG: grid={grid}")
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            sym = grid.getSymbol(point2d.Point2D(w,h))
            print(f"{sym}",end="")
        print()

def count_points_of_line_overlap_from_file(filename):
    inputLines = utils.get_file_lines(filename)

    lines = []
    maxX = 0
    maxY = 0
    for str in inputLines:
        line = parser.parseInputStringToLine2D(str)
        if line.isHorizontalLine() or line.isVerticalLine():
            lines.append(line)
            maxX = max(maxX, max(line.begin.getX(), line.end.getX()))
            maxY = max(maxY, max(line.begin.getY(), line.end.getY()))
                       
            print(f"DEBUG: Adding line={line}")

    #assert len(lines) == 6

    grid = grid2d.Grid2D(maxX+1,maxY+1)
    for line in lines:
        for point in line.getAllPoints():
            setGridValue(grid, point)


    count = 0
    for h in range(grid.getHeight()):
        for w in range(grid.getWidth()):
            sym = grid.getSymbol(point2d.Point2D(w,h))
            if type(sym) is int and sym > 1:
                count = 1 + count # increment

    displayGrid(grid)
    return count