import point2d

class Grid2D():

    def __init__(self, width:int, height:int):
        if width < 1:
            raise Exception(f"Invalid width: {width}")

        if height < 1:
            raise Exception(f"Invalid height: {height}")

        self.width = width 
        self.height = height
        self.array = [['.' for i in range(width)] for j in  range(height)]

    def getWidth(self) -> int:
        return self.width

    def getHeight(self) -> int:
        return self.height

    def getSymbol(self, coord:point2d.Point2D) -> chr:
        if not self.checkContains(coord):
            raise(Exception("Point {coord} not within grid!"))
        return self.array[coord.getX()][coord.getY()]

    def setSymbol(self, coord:point2d.Point2D, symbol:chr):
        if not self.checkContains(coord):
            raise(Exception("Point {coord} not within grid!"))
        self.array[coord.getX()][coord.getY()] = symbol

    def checkContains(self, coord: point2d.Point2D) -> bool:
        if coord.getX() < 0 or coord.getX() > self.getWidth():
            return False

        if coord.getY() < 0 or coord.getY() > self.getHeight():
            return False

        return True

    def __str__(self):
        return f"Grid2D(id={id(self)} , width: {self.getWidth()}, height: {self.getHeight()})"