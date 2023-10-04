import point2d

def lines_to_grid(input_lines):
    height = len(input_lines)
    width = len(input_lines[0])

    grid = Grid2D(width, height)

    y = 0
    for line in input_lines:
        for x in range(width):
            point = point2d.Point2D(x, y)
            grid.setSymbol(point, line[x])
        y += 1

    return grid

def grid_to_lines(grid):
    lines = []
    for h in range(grid.getHeight()):
        line = ""
        for w in range(grid.getWidth()):
            line += grid.getSymbol(point2d.Point2D(w,h))
        lines.append(line)
    return lines
            

class Grid2D():

    def __init__(self, width:int, height:int):
        if width < 1:
            raise Exception(f"Invalid width: {width}")

        if height < 1:
            raise Exception(f"Invalid height: {height}")

        self.width = width 
        self.height = height
        self.array = [['.' for i in range(height)] for j in  range(width)]

    def getWidth(self) -> int:
        return self.width

    def getHeight(self) -> int:
        return self.height

    def getSymbol(self, coord:point2d.Point2D) -> chr:
        if not self.contains(coord):
            raise(Exception("Point {coord} not within grid!"))
        return self.array[coord.getX()][coord.getY()]

    def setSymbol(self, coord:point2d.Point2D, symbol:chr):
        if not self.contains(coord):
            raise(Exception("Point {coord} not within grid!"))
        self.array[coord.getX()][coord.getY()] = symbol

    def contains(self, coord: point2d.Point2D) -> bool:
        if coord.getX() < 0 or coord.getX() >= self.getWidth():
            return False

        if coord.getY() < 0 or coord.getY() >= self.getHeight():
            return False

        return True
    
    def getCardinalPointNeighbours(self, point:point2d.Point2D) -> set:
        neightbours = set()

        x = point.getX()
        y = point.getY()

        cardinal_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        for (a,b) in cardinal_points:
            np = point2d.Point2D(a,b)
            if self.contains(np):
                neightbours.add(np)
        return neightbours  

    def getSurroundingNeighbours(self, point:point2d.Point2D) -> set:
        neightbours = set()

        x = point.getX()
        y = point.getY()

        surrounding_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1),(x-1,y-1), (x+1,y+1), (x+1,y-1), (x-1,y+1)]

        for (a,b) in surrounding_points:
            np = point2d.Point2D(a,b)
            if self.contains(np):
                neightbours.add(np)
        return neightbours    

    def __str__(self):
        return f"Grid2D(id={id(self)} , width: {self.getWidth()}, height: {self.getHeight()})"