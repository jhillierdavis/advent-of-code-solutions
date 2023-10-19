#from typing import Self # Python 3.11+

class Point2D():

    def __init__(self, x:int, y:int):
        if not isinstance(x, int):
            raise TypeError("Non integer value provided for x")

        if not isinstance(y, int):
            raise TypeError("Non integer value provided for y")

        self.x = x
        self.y = y
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def __str__(self) -> str:
        return f"Point2D(id={id(self)} , x: {self.get_x()}, y: {self.get_y()})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
    
    def __lt__(self, other) -> bool:
        return self.get_x() < other.get_x() or self.get_y() < other.get_y()

    def __le__(self, other) -> bool:
        return self.get_x() <= other.get_x() or self.get_y() <= other.get_y()

    def __hash__(self):
        return hash(self.get_x()) + hash(self.get_y())

