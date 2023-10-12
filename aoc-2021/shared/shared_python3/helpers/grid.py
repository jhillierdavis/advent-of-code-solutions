from helpers import point

# TODO: Update to follow style conventions (e.g. for class & method names) https://peps.python.org/pep-0008/

def lines_to_grid(input_lines):
    height = len(input_lines)
    width = len(input_lines[0])

    grid = Grid2D(width, height)

    y = 0
    for line in input_lines:
        for x in range(width):
            p = point.Point2D(x, y)
            grid.setSymbol(p, line[x])
        y += 1

    return grid


def grid_to_lines(grid):
    lines = []
    for h in range(grid.get_height()):
        line = ""
        for w in range(grid.get_width()):
            value = grid.getSymbol(point.Point2D(w,h))
            line += str(value)
        lines.append(line)
    return lines
            
    
def display_grid(grid):
    lines = grid_to_lines(grid)
    for gl in lines:
        print(f"Grid line: {gl}")


class Grid2D():

    def __init__(self, width:int, height:int):
        if width < 1:
            raise ValueError(f"Invalid width: {width}")

        if height < 1:
            raise ValueError(f"Invalid height: {height}")

        self.width = width 
        self.height = height
        self.array = [['.' for i in range(height)] for j in  range(width)]

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_symbol(self, coord:point.Point2D) -> chr:
        if not self.contains(coord):
            raise(ValueError(f"Point {coord} not within grid: {self}"))
        return self.array[coord.getX()][coord.getY()]

    def set_symbol(self, coord:point.Point2D, symbol:chr):
        if not self.contains(coord):
            raise(ValueError(f"Point {coord} not within grid: {self}"))
        self.array[coord.getX()][coord.getY()] = symbol

    def contains(self, coord: point.Point2D) -> bool:
        if coord.getX() < 0 or coord.getX() >= self.get_width():
            return False

        if coord.getY() < 0 or coord.getY() >= self.get_height():
            return False

        return True
    
    def get_cardinal_point_neighbours(self, p:point.Point2D) -> set:
        neightbours = set()

        x = p.getX()
        y = p.getY()

        cardinal_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        for (a,b) in cardinal_points:
            np = point.Point2D(a,b)
            if self.contains(np):
                neightbours.add(np)
        return neightbours  

    def get_surrounding_neighbours(self, p:point.Point2D) -> set:
        neightbours = set()

        x = p.getX()
        y = p.getY()

        surrounding_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1),(x-1,y-1), (x+1,y+1), (x+1,y-1), (x-1,y+1)]

        for (a,b) in surrounding_points:
            np = point.Point2D(a,b)
            if self.contains(np):
                neightbours.add(np)
        return neightbours    

    def __str__(self):
        return f"Grid2D(id={id(self)} , width: {self.get_width()}, height: {self.get_height()})"
    
    def get_subgrid_from_origin(self, width:int, height:int):
        if width > self.get_width():
            raise ValueError(f"width:{width} greater than grid width of {self.get_width()}")
        
        if height > self.get_height():
            raise ValueError(f"height:{height} greater than grid width of {self.get_height()}")
        
        subgrid = Grid2D(width,height)

        for x in range(width):
            for y in range(height):
                p = point.Point2D(x,y)
                subgrid.set_symbol(p, self.get_symbol(p))

        return subgrid
    
    def get_subgrid_inclusive(self, start, end):
        if start.getX() < 0 or start.getX() >= self.get_width():    
            raise ValueError(f"Invalid start point X value: {start}")

        if start.getY() < 0 or start.getY() >= self.get_height():    
            raise ValueError(f"Invalid start point Y value: {start}")

        if end.getX() < 0 or end.getX() >= self.get_width():    
            raise ValueError(f"Invalid end point X value: {end}")

        if end.getY() < 0 or end.getY() >= self.get_height():    
            raise ValueError(f"Invalid end point Y value: {end}")
        
        if start.getX() >= end.getX():
            raise ValueError(f"Invalid start and end X values: {start} {end}")

        if start.getY() >= end.getY():
            raise ValueError(f"Invalid start and end Y values: {start} {end}")

        width = 1 + end.getX() - start.getX()
        height = 1 + end.getY() - start.getY()
        subgrid = Grid2D(width, height)

        for x in range(start.getX(), 1 + end.getX()):
            for y in range(start.getY(), 1 + end.getY()):                
                p = point.Point2D(x,y)
                value = self.get_symbol(p)

                sp = point.Point2D(x - start.getX(), y - start.getY())
                #print(f"DEBUG: p={p} sp={sp}")                
                subgrid.set_symbol(sp, value)

        return subgrid    
    
    def get_inverted_vertically(self):
        ig = Grid2D(self.get_width(), self.get_height())

        
        h = self.get_height()
        for x in range(self.get_width()):
            for y in range(h):
                p = point.Point2D(x,y)
                ip = point.Point2D(x, (h - 1) - y)
                ig.set_symbol(ip, self.get_symbol(p))
        return ig

    def get_inverted_horizontally(self):
        ig = Grid2D(self.get_width(), self.get_height())

        w = self.get_width()        
        for x in range(w):
            for y in range(self.get_height()):
                p = point.Point2D(x,y)
                ip = point.Point2D((w-1) -x, y)
                ig.set_symbol(ip, self.get_symbol(p))
        return ig
    
    def count_symbol(self, symbol):
        count = 0
        for x in range(self.get_width()):
            for y in range(self.get_height()):
                value = self.get_symbol(point.Point2D(x,y))
                if value == symbol:
                    count +=1
        return count
    
    def merge_symbol(self, grid, symbol):
        min_w = min(self.get_width(), grid.get_width())
        min_h = min(self.get_height(), grid.get_height())

        for x in range(min_w):
            for y in range(min_h):
                p = point.Point2D(x,y)
                value = grid.get_symbol(p)
                if value == symbol:
                    self.set_symbol(p, symbol)

        return self