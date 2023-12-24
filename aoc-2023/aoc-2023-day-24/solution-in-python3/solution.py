#from collections import defaultdict

from helpers import fileutils, point, strutils


class Hailstone():

    def __init__(self, position:point.Point3D, velocity:point.Point3D):
        if not isinstance(position, point.Point3D):
            raise TypeError("Non point.Point3D value provided for 'position'")

        if not isinstance(velocity, point.Point3D):
            raise TypeError("Non point.Point3D value provided for 'velocity'")

        self.position = position
        self.velocity = velocity

    
    def __str__(self) -> str:
        return f"Hailstone(id={id(self)} , position: {self.position}, end: {self.velocity})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.position == other.position and self.velocity == other.velocity
    
    def __hash__(self):
        return hash(self.position) + hash(self.velocity) 
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.position < other.position or self.velocity < other.velocity
    
    def clone(self):
        cloned_instance = Hailstone(self.position, self.velocity)
        return cloned_instance


def get_hailstone_from(input):
    p, v = input.split(' @ ')
    pil = strutils.string_to_int_list(p, ',')
    vil = strutils.string_to_int_list(v, ',')

    h = Hailstone(point.Point3D(pil[0], pil[1], pil[2]), point.Point3D(vil[0], vil[1], vil[2]))
    #print(f"DEBUG: h={h}")
    return h

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

