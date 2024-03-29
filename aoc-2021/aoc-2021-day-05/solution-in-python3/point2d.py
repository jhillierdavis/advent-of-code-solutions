#from typing import Self # Not available before Python version 3.11: ImportError: cannot import name 'Self' from 'typing'

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
    
    def __eq__(self,other) -> bool:
        return self.getX() == other.getX() and self.getY() == other.getY()