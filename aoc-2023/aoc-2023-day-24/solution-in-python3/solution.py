from z3 import *

from helpers import fileutils, point, strutils

class Hailstone():

    def __init__(self, position:point.Point3D, velocity:point.Point3D):
        if not isinstance(position, point.Point3D):
            raise TypeError("Non point.Point3D value provided for 'position'")

        if not isinstance(velocity, point.Point3D):
            raise TypeError("Non point.Point3D value provided for 'velocity'")

        self.position = position
        self.velocity = velocity


    def get_next_position(self):
        return point.Point2D(self.position.get_x() + self.velocity.get_x(), self.position.get_y() + self.velocity.get_y())
    

    def is_future_xy_position(self, p):
        if not p:
            return False
        
        x = p[0]
        y = p[1]

        if self.velocity.get_x() > 0:
            if x <= self.position.get_x():
                return False
        else:
            if x >= self.position.get_x():
                return False

        if self.velocity.get_y() > 0:
            if y <= self.position.get_y():
                return False
        else:
            if y >= self.position.get_y():
                return False
            
        return True


    def get_xy_intersection_point_with(self, other):
        s1 = point.Point2D(self.position.get_x(), self.position.get_y())
        s2 = self.get_next_position()

        o1 = point.Point2D(other.position.get_x(), other.position.get_y())
        o2 = other.get_next_position()

        # Line 'self' (with xy positions s1 & s2) represented as a1x + b1y = c1
        a1 = s2.get_y() - s1.get_y()
        b1 = s1.get_x() - s2.get_x()
        c1 = a1*(s1.get_x()) + b1*(s1.get_y())
    
        # Line 'other' (with xy positions o1 & o2) represented as a2x + b2y = c2
        a2 = o2.get_y() - o1.get_y()
        b2 = o1.get_x() - o2.get_x()
        c2 = a2*(o1.get_x()) + b2*(o1.get_y())
    
        determinant = (a1 * b2) - (a2 * b1)
    
        if (determinant == 0):
            # Lines are parallel!
            return None
        
        x = (b2*c1 - b1*c2) / determinant
        y = (a1*c2 - a2*c1) / determinant
        return (round(x,3), round(y,3)) # Use a tuple rather than Point2D as can be float values

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
    

def get_hailstone_intersection_point(ha, hb) -> point.Point2D:
    return ha.get_xy_intersection_point_with(hb)
    

def get_hailstone_from(input):
    p, v = input.split(' @ ')
    pil = strutils.string_to_int_list(p, ',')
    vil = strutils.string_to_int_list(v, ',')

    h = Hailstone(point.Point3D(pil[0], pil[1], pil[2]), point.Point3D(vil[0], vil[1], vil[2]))
    #print(f"DEBUG: h={h}")
    return h

def solve_part1(filename, target_min, target_max):
    lines = fileutils.get_file_lines(filename)

    hailstones = set()
    for l in lines:
        h = get_hailstone_from(l)
        hailstones.add(h)

    count = 0
    for h1 in hailstones:
        for h2 in hailstones:
            if h1 == h2:
                continue

            intersection = get_hailstone_intersection_point(h1, h2)
            if h1.is_future_xy_position(intersection) and h2.is_future_xy_position(intersection):
                
                ix = intersection[0]
                iy = intersection[1]
                #print(f"DEBUG: {intersection}")
                if ix >= target_min and ix <= target_max and iy >= target_min and iy <= target_max:
                    count += 1

    return count // 2


def solve_part2_using_z3_from(hailstones):
    n = len(hailstones)

    x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
    T = [Int(f'T{i}') for i in range(n)]
    z3_solver = Solver()
    for i in range(n):
        z3_solver.add(x + T[i]*vx - hailstones[i].position.get_x() - T[i]*hailstones[i].velocity.get_x() == 0)
        z3_solver.add(y + T[i]*vy - hailstones[i].position.get_y() - T[i]*hailstones[i].velocity.get_y() == 0)
        z3_solver.add(z + T[i]*vz - hailstones[i].position.get_z() - T[i]*hailstones[i].velocity.get_z() == 0)
    res = z3_solver.check()
    z3_model = z3_solver.model()

    return z3_model.eval(x+y+z)


def solve_part2(filename):
    # Use Z3, see: https://microsoft.github.io/z3guide/docs/logic/intro/ , https://github.com/Z3Prover/z3

    lines = fileutils.get_file_lines(filename)

    hailstones = []
    for l in lines:
        h = get_hailstone_from(l)
        hailstones.append(h)

    return solve_part2_using_z3_from(hailstones)