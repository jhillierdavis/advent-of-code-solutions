#from typing import Self # Python 3.11+

class Point2D():

    def __init__(self, x:int, y:int):
        if not isinstance(x, int):
            raise TypeError("Non integer value provided for x")

        if not isinstance(y, int):
            raise TypeError("Non integer value provided for y")

        self.x = x
        self.y = y
    
    def getX(self) -> int:
        return self.x
    
    def getY(self) -> int:
        return self.y
    
    def __str__(self) -> str:
        return f"Point2D(id={id(self)} , x: {self.getX()}, y: {self.getY()})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __hash__(self):
        return hash(self.getX()) + hash(self.getY())

