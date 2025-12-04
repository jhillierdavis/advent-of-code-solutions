#from typing import Self # Python 3.11+

def tuple_to_point2d(p):
    x,y = p
    return Point2D(x, y)


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
    
    def to_tuple(self):
        return (self.x, self.y)
    
    def get_manhatten_distance_to(self, other):
        return abs(self.get_x() - other.get_x()) + abs(self.get_y() - other.get_y())    

    
    def get_closest_neighbours(self):
        neighbour_set = set()
        for x in range(-1,2):
            for y in range(-1,2):
                np = Point2D(self.get_x() + x, self.get_y() + y)
                neighbour_set.add(np)

        neighbour_set.remove(self) # Don't include the point provided (just the 8 direct neighbouring points)
        return neighbour_set

    
    def __str__(self) -> str:
        return f"Point2D(id={id(self)} , x: {self.get_x()}, y: {self.get_y()})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        if other == None:
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
    
    def __hash__(self):
        return hash(self.get_x() * 17) + hash(self.get_y() * 19)
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.get_x() < other.get_x() or self.get_y() < other.get_y()

    def __le__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.get_x() <= other.get_x() or self.get_y() <= other.get_y()


class Point3D():
    def __init__(self, x:int, y:int, z:int):
        if not isinstance(x, int):
            raise TypeError("Non integer value provided for x")

        if not isinstance(y, int):
            raise TypeError("Non integer value provided for y")

        if not isinstance(z, int):
            raise TypeError("Non integer value provided for z")

        self.x = x
        self.y = y
        self.z = z

    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def get_z(self) -> int:
        return self.z
    
    
    def to_tuple(self):
        return (self.x, self.y, self.z)

    
    def get_manhatten_distance_to(self, other):
        return abs(self.get_x() - other.get_x()) + abs(self.get_y() - other.get_y()) + abs(self.get_z() - other.get_z())   


    def get_closest_neighbours(self):
        neighbour_set = set()
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    np = Point3D(self.get_x() + x, self.get_y() + y, self.get_z() + z)
                    neighbour_set.add(np)

        neighbour_set.remove(self)
        #assert len(neighbour_set) == 26 # 9 + 9 + 8
        #logger.debug(f"p3d={p3d} neighbour_set={neighbour_set}")
        return neighbour_set         

    
    def __str__(self) -> str:
        return f"Point3D(id={id(self)} , x: {self.get_x()}, y: {self.get_y()}, z: {self.get_z()})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y() and self.get_z() == other.get_z()
    
    def __hash__(self):
        return hash(self.get_x() * 17) + hash(self.get_y() * 19) + hash(self.get_z() * 23)
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.get_x() < other.get_x() or self.get_y() < other.get_y() or self.get_z() < other.get_z()
    
    def clone(self):
        cloned = Point3D(self.get_x(), self.get_y(), self.get_z())
        return cloned

class Point4D():
    def __init__(self, x:int, y:int, z:int, t:int):
        if not isinstance(x, int):
            raise TypeError("Non integer value provided for x")

        if not isinstance(y, int):
            raise TypeError("Non integer value provided for y")

        if not isinstance(z, int):
            raise TypeError("Non integer value provided for z")

        if not isinstance(t, int):
            raise TypeError("Non integer value provided for t")

        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def get_z(self) -> int:
        return self.z
    
    def get_t(self) -> int:
        return self.t
    
    def to_tuple(self):
        return (self.x, self.y, self.z, self.t)

    
    def get_manhatten_distance_to(self, other):
        return abs(self.get_x() - other.get_x()) + abs(self.get_y() - other.get_y()) + abs(self.get_z() - other.get_z()) + abs(self.get_t() - other.get_t())   


    def get_closest_neighbours(self):
        neighbour_set = set()
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    for t in range(-1,2):
                        np = Point4D(self.get_x() + x, self.get_y() + y, self.get_z() + z, self.get_t() + t)
                        neighbour_set.add(np)

        neighbour_set.remove(self)
        return neighbour_set         

    
    def __str__(self) -> str:
        return f"Point4D(id={id(self)} , x: {self.get_x()}, y: {self.get_y()}, z: {self.get_z()}, t: {self.get_t()})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y() and self.get_z() == other.get_z() and self.get_t() == other.get_t()
    
    def __hash__(self):
        return hash(self.get_x() * 17) + hash(self.get_y() * 19) + hash(self.get_z() * 23 ) + hash(self.get_t() * 29)
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.get_x() < other.get_x() or self.get_y() < other.get_y() or self.get_z() < other.get_z() or self.get_t() < other.get_t()
    
    def clone(self):
        cloned = Point4D(self.get_x(), self.get_y(), self.get_z(), self.get_t())
        return cloned

