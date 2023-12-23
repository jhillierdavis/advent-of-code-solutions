#from collections import defaultdict

from helpers import fileutils, strutils

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



class Block():
    def __init__(self, begin:Point3D, end:Point3D):
        if not isinstance(begin, Point3D):
            raise TypeError("Non Point3D value provided for 'begin'")

        if not isinstance(end, Point3D):
            raise TypeError("Non Point3D value provided for 'end'")

        self.begin = begin
        self.end = end

    def is_grounded(self) -> bool:
        #return True if self.begin[2] <= 1 or self.end[2] <= 1 else False
        return True if self.begin.get_z() <= 1 else False
        
    def is_supporting(self, other) -> bool:
        if self.end.get_z() != other.begin.get_z() - 1:
            return False

        cloned_other = other.clone()
        other = None
        cloned_other.decrement_z()

        if self.end.get_z() != cloned_other.begin.get_z():
            return False        

        cubes_self = self.get_set_of_cubes()
        cubes_cloned_other = cloned_other.get_set_of_cubes()

        intersection = cubes_self.intersection(cubes_cloned_other)
        #print(f"DEBUG: {intersection} {self} {cloned_other} {other}")
        return len(intersection) > 0
    
    def is_neighbour(self, other:Point3D) -> bool:
        # Coords at same height (z axis values) ?
        if self.end.get_z() == other.end.get_z():
            return True
        return False


    def get_set_of_cubes(self):
        cubes = set()

        if self.begin.get_x() == self.end.get_x() and self.begin.get_y() == self.end.get_y():
            for z in range(self.begin.get_z(), 1 + self.end.get_z()):
                cubes.add(Point3D(self.begin.get_x(), self.begin.get_y(), z))
        elif self.begin.get_x() == self.end.get_x() and self.begin.get_z() == self.end.get_z():
            for y in range(self.begin.get_y(), 1 + self.end.get_y()):
                cubes.add(Point3D(self.begin.get_x(), y, self.begin.get_z()))
        elif self.begin.get_y() == self.end.get_y() and self.begin.get_z() == self.end.get_z():
            for x in range(self.begin.get_x(), 1 + self.end.get_x()):
                cubes.add(Point3D(x, self.begin.get_y(), self.begin.get_z()))
        else:
            assert False

        return cubes
        
    
    def is_supported_by(self, other) -> bool:
        return other.is_supporting(self)


    def is_supported_by_any_of(self, other_blocks) -> bool:
        for other in other_blocks:
            if self == other:
                continue
            if self.is_supported_by(other):
                return True
        return False


    def decrement_z(self):
        self.begin = Point3D(self.begin.get_x(), self.begin.get_y(), self.begin.get_z() -1)
        self.end = Point3D(self.end.get_x(), self.end.get_y(), self.end.get_z() -1)
    
    def __str__(self) -> str:
        return f"Block(id={id(self)} , begin: {self.begin}, end: {self.end})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.begin == other.begin and self.end == other.end
    
    def __hash__(self):
        return hash(self.begin) + hash(self.end) 
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.begin < other.begin or self.end < other.end
    
    def clone(self):
        cloned_block = Block(self.begin, self.end)
        return cloned_block

def get_supporting(blocks, cb):
    supporting = set()
    for ob in blocks:
        if ob == cb:
            continue

        if cb.is_supporting(ob):
            supporting.add(ob)

    return supporting

def get_neighbours(blocks, cb):
    neighbours = set()
    for ob in blocks:
        if ob == cb:
            continue

        if cb.is_neighbour(ob):
            neighbours.add(ob)
    return neighbours


def get_blocks_from(filename):
    lines = fileutils.get_file_lines(filename)

    blocks = []
    for l in lines:
        #print(f"DEBUG: l={l}")
        p1,p2 = l.split('~')
        begin = strutils.string_to_int_list(p1, ',')
        end = strutils.string_to_int_list(p2, ',')
        b = Block(Point3D(begin[0], begin[1], begin[2]), Point3D(end[0], end[1], end[2]))
        #print(f"DEBUG: block={b} ")
        blocks.append(b) 
    return blocks

def solve_part1(filename):
    blocks = get_blocks_from(filename)
    #print(f"DEBUG: Initial blocks={blocks} ")

    for b in blocks:
        if b.is_grounded():
            continue

        while not b.is_supported_by_any_of(blocks):
            #print(f"DEBUG: Moving down: {b}")
            b.decrement_z()
            if b.is_grounded():
                break

    #print(f"DEBUG: Final blocks={blocks} ")

    count = 0
    
    for b in blocks:
        if b.is_grounded():
            continue

        supporting = get_supporting(blocks, b)
        supporting_count = len(supporting)
        neighbours = get_neighbours(blocks, b)
        neighbours_count = len(neighbours)
        #print(f"DEBUG: {supporting_count} {neighbour_count} {b}")


        if supporting_count == 0:
            #print(f"DEBUG: Block can be disintegrated: {b}")
            count += 1
        elif neighbours_count == 0:
            continue
        elif is_sole_supporter(blocks, supporting, neighbours):
            """
            for n in neighbours:
                ns = get_supporting(blocks, n)
                intersect = supporting.intersection(ns)
                if len(intersect) > 0:
                    count += 1
                    break
            """
            count += 1


    return count

def is_sole_supporter(blocks, supporting, neighbours):
    for s in supporting:
        for n in neighbours:
            ns = get_supporting(blocks, n)
            if s not in ns:    
                return False
    return True


def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO