

class Point2D():

    def __init__(self, x:int, y:int):
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