#from collections import defaultdict

from helpers import fileutils, strutils

class Block():
    def __init__(self, begin:(int,int,int), end:(int,int,int)):
        self.begin = begin
        self.end=end

    def is_grounded(self) -> bool:
        return True if self.begin[2] == 1 or self.end[2] == 1 else False
    
    """
    def is_supporting(self, other) -> bool:
        if 1 != other.begin[2] - self.end[2]:
            print(f"DEBUG: Not directly above: {self} {other}")
            return False

        is_x_overlap = (other.begin[0] <= self.begin[0] and other.begin[0] <= self.end[0]) or (other.end[0] >= self.begin[0] and other.end[0] >= self.end[0])
        is_y_overlap = (other.begin[1] >= self.begin[1] and other.begin[1] <= self.end[1]) or (other.end[1] >= self.begin[1] and other.end[1] <= self.end[1])
        print(f"DEBUG: Overlap x {is_x_overlap}: y {is_y_overlap} for {self} {other}")

        return True if is_x_overlap and is_y_overlap else False
    """

    def is_supporting(self, other) -> bool:
        cloned_other = other.clone()
        cloned_other.decrement_z()

        cubes_self = self.get_set_of_cubes()
        cubes_cloned_other = cloned_other.get_set_of_cubes()

        intersection = cubes_self.intersection(cubes_cloned_other)
        #print(f"DEBUG: {intersection} {self} {cloned_other} {other}")
        return len(intersection) > 0
    
    def is_neighbour(self, other) -> bool:
        if self.begin[2] == other.begin[2] and self.end[2] == other.end[2]:
            return True
        return False


    def get_set_of_cubes(self):
        cubes = set()

        if self.begin[0] == self.end[0] and self.begin[1] == self.end[1]:
            for z in range(self.begin[2], 1 + self.begin[2]):
                cubes.add((self.begin[0], self.end[1], z))
        elif self.begin[0] == self.end[0] and self.begin[2] == self.end[2]:
            for y in range(self.begin[1], 1 + self.end[1]):
                cubes.add((self.begin[0], y, self.begin[2]))
        elif self.begin[1] == self.end[1] and self.begin[2] == self.end[2]:
            for x in range(self.begin[0], 1 + self.end[0]):
                cubes.add((x, self.begin[1], self.begin[2]))
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
        self.begin = (self.begin[0], self.begin[1], self.begin[2] -1)
        self.end = (self.end[0], self.end[1], self.end[2] -1)
    
    def __str__(self) -> str:
        return f"Block(id={id(self)} , begin: {self.begin}, end: {self.end})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self,other) -> bool:
        return self.begin == other.begin and self.end == other.end
    
    def __hash__(self):
        return hash(self.begin * 17) + hash(self.end * 19)
    
    def __lt__(self, other) -> bool:
        # E.g. for Heapq: to handle "Handle duplicate point values -> TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'"
        return self.begin < other.begin or self.end < other.end
    
    def clone(self):
        cloned_block = Block((self.begin[0], self.begin[1], self.begin[2]), (self.end[0], self.end[1], self.end[2]))
        return cloned_block


def count_supporting(blocks, cb):
    count = 0
    for ob in blocks:
        if ob == cb:
            continue

        if cb.is_supporting(ob):
            count += 1

    return count

def count_neighbours(blocks, cb):
    count = 0
    for ob in blocks:
        if ob == cb:
            continue

        if cb.is_neighbour(ob):
            count += 1

    return count


def can_fall(blocks:[Block], cb:Block):
    if cb.is_grounded():
        return False
    
    count = count_supporting(blocks, cb)
    print(f"DEBUG: Supporting count={count} for {cb}")
    return False if count == 1 else True

def get_blocks_from(filename):
    lines = fileutils.get_file_lines(filename)

    blocks = []
    for l in lines:
        #print(f"DEBUG: l={l}")
        p1,p2 = l.split('~')
        begin = strutils.string_to_int_list(p1, ',')
        end = strutils.string_to_int_list(p2, ',')
        b = Block(begin, end)
        #print(f"DEBUG: block={b} ")
        blocks.append(b) 
    return blocks

def solve_part1(filename):
    blocks = get_blocks_from(filename)
    print(f"DEBUG: Initial blocks={blocks} ")

    for b in blocks:
        if b.is_grounded():
            continue

        while not (b.is_grounded() or b.is_supported_by_any_of(blocks)):
            print(f"DEBUG: Moving down: {b}")
            b.decrement_z()

    print(f"DEBUG: Final blocks={blocks} ")

    count = 0
    
    for b in blocks:
        if b.is_grounded():
            continue

        supporting_count = count_supporting(blocks, b)
        neighbour_count = count_neighbours(blocks, b)
        print(f"DEBUG: {supporting_count} {neighbour_count} {b}")

        if supporting_count == 0 or (supporting_count > 0 and neighbour_count > 0):
            #print(f"DEBUG: Block can be disintegrated: {b}")
            count += 1
    return count

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

