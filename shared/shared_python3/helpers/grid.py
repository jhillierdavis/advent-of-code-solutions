from helpers import point, fileutils, compass

# TODO: Update to follow style conventions (e.g. for class & method names) https://peps.python.org/pep-0008/

def lines_to_grid(input_lines):
    height = len(input_lines)
    width = len(input_lines[0])

    grid = Grid2D(width, height)

    y = 0
    for line in input_lines:
        for x in range(width):
            p = point.Point2D(x, y)
            grid.set_symbol(p, line[x])
        y += 1

    return grid

def lines_to_integer_grid(input_lines):
    height = len(input_lines)
    width = len(input_lines[0])

    grid = Grid2D(width, height)

    y = 0
    for line in input_lines:
        for x in range(width):
            p = point.Point2D(x, y)
            int_value = int(line[x])
            grid.set_symbol(p, int_value)
        y += 1

    return grid


def grid_to_lines(grid, separator:str=""):
    lines = []
    for h in range(grid.get_height()):
        line = ""
        for w in range(grid.get_width()):
            value = grid.get_symbol(point.Point2D(w,h))
            line += str(value) + separator
        lines.append(line)
    return lines
            
    
def display_grid(grid, separator:str=""):
    lines = grid_to_lines(grid, separator)
    for gl in lines:
        print(f"Grid line: {gl} ")


def get_multiple_grids_from(filename):
    list_of_grid_lines = fileutils.get_contiguous_non_empty_lines_from(filename)

    grids = []
    for lines in list_of_grid_lines:
        g = lines_to_grid(lines)
        grids.append(g)
    return grids


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
        return self.array[coord.get_x()][coord.get_y()]

    def set_symbol(self, coord:point.Point2D, symbol:chr):
        if not self.contains(coord):
            raise(ValueError(f"Point {coord} not within grid: {self}"))
        self.array[coord.get_x()][coord.get_y()] = symbol

    def contains(self, coord: point.Point2D) -> bool:
        if coord.get_x() < 0 or coord.get_x() >= self.get_width():
            return False

        if coord.get_y() < 0 or coord.get_y() >= self.get_height():
            return False

        return True
    
    def get_cardinal_point_neighbours(self, p:point.Point2D, wrapping:bool=False) -> set:
        neightbours = set()

        x = p.get_x()
        y = p.get_y()
        """
        cardinal_points = []
        if wrapping:
            x_max = self.get_width() -1
            y_max = self.get_height() -1
            cardinal_points.append((x-1 if x > 0 else x_max, y))
            cardinal_points.append((x+1 if x < x_max else 0, y))
            cardinal_points.append((x, y-1 if y > 0 else y_max))
            cardinal_points.append((x, y+1 if y < y_max else 0))
        else:
            cardinal_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        """
        cardinal_points = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        for (a,b) in cardinal_points:
            np = point.Point2D(a,b)
            if self.contains(np) or wrapping:
                neightbours.add(np)
        return neightbours  


    def get_unwrapped_coord(self, p:point.Point2D) -> set:
        x_max = self.get_width()
        y_max = self.get_height()
        x = p.get_x()
        y = p.get_y()
        x_unwrapped = x % x_max
        if x_unwrapped < 0:
            x_unwrapped = x_max - x_unwrapped
        y_unwrapped = y % y_max
        if y_unwrapped < 0:
            y_unwrapped = y_max - y_unwrapped
        #if x != x_unwrapped or y != y_unwrapped:
        #    print(f"DEBUG: x={x} x_unwrapped={x_unwrapped} x_max={x_max} y={y} y_unwrapped={y_unwrapped} y_max={y_max}")
        unwrapped_point = point.Point2D(x_unwrapped, y_unwrapped)
        return unwrapped_point


    def get_neighbour_east(self, p:point.Point2D) -> point.Point2D:
        x = p.get_x()
        y = p.get_y()

        np = point.Point2D(x+1 , y)

        if self.contains(np):
                return np
        return None  

    def get_neighbour_west(self, p:point.Point2D) -> point.Point2D:
        x = p.get_x()
        y = p.get_y()

        np = point.Point2D(x-1 , y)

        if self.contains(np):
                return np
        return None  

    def get_neighbour_north(self, p:point.Point2D) -> point.Point2D:
        x = p.get_x()
        y = p.get_y()

        np = point.Point2D(x , y-1)

        if self.contains(np):
                return np
        return None  

    def get_neighbour_south(self, p:point.Point2D) -> point.Point2D:
        x = p.get_x()
        y = p.get_y()

        np = point.Point2D(x , y+1)

        if self.contains(np):
                return np
        return None  

    def get_matching_symbol_coords(self, symbol:chr):
        locations = []
        for x in range(self.get_width()):
            for y in range(self.get_height()):
                p = point.Point2D(x,y)
                if self.get_symbol(p) == symbol:
                    locations.append(p)
        return locations


    def get_point_or_none(self, x:int, y:int) -> point.Point2D:
        p = point.Point2D(x,y)
        if self.contains(p):
            return p
        return None


    def get_neighbour_point_east(self, current:point.Point2D) -> point.Point2D:
        return self.get_point_or_none(current.get_x() + 1, current.get_y())

    def get_neighbour_point_west(self, current:point.Point2D) -> point.Point2D:
        return self.get_point_or_none(current.get_x() - 1, current.get_y())

    def get_neighbour_point_north(self, current:point.Point2D) -> point.Point2D:
        return self.get_point_or_none(current.get_x(), current.get_y() - 1)

    def get_neighbour_point_south(self, current:point.Point2D) -> point.Point2D:
        return self.get_point_or_none(current.get_x(), current.get_y() + 1)

    def get_surrounding_neighbours(self, p:point.Point2D) -> set:
        neightbours = set()

        x = p.get_x()
        y = p.get_y()

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
        if start.get_x() < 0 or start.get_x() >= self.get_width():    
            raise ValueError(f"Invalid start point X value: {start}")

        if start.get_y() < 0 or start.get_y() >= self.get_height():    
            raise ValueError(f"Invalid start point Y value: {start}")

        if end.get_x() < 0 or end.get_x() >= self.get_width():    
            raise ValueError(f"Invalid end point X value: {end}")

        if end.get_y() < 0 or end.get_y() >= self.get_height():    
            raise ValueError(f"Invalid end point Y value: {end}")
        
        if start.get_x() >= end.get_x():
            raise ValueError(f"Invalid start and end X values: {start} {end}")

        if start.get_y() >= end.get_y():
            raise ValueError(f"Invalid start and end Y values: {start} {end}")

        width = 1 + end.get_x() - start.get_x()
        height = 1 + end.get_y() - start.get_y()
        subgrid = Grid2D(width, height)

        for x in range(start.get_x(), 1 + end.get_x()):
            for y in range(start.get_y(), 1 + end.get_y()):                
                p = point.Point2D(x,y)
                value = self.get_symbol(p)

                sp = point.Point2D(x - start.get_x(), y - start.get_y())
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


    def get_rows_where_only_symbol(self, symbol:chr):
        matched = []
        for r in range(self.get_height()):
            is_matched = True
            for c in range(self.get_width()):
                s = self.get_symbol(point.Point2D(c, r))
                if s != symbol:
                    is_matched = False
                    break
            if is_matched:
                matched.append(r)
        return matched
    
        
    def get_columns_where_only_symbol(self, symbol:chr):
        matched = []
        for c in range(self.get_width()):
            is_matched = True
            for r in range(self.get_height()):
                s = self.get_symbol(point.Point2D(c, r))
                if s != symbol:
                    is_matched = False
                    break
            if is_matched:
                matched.append(c)
        return matched


    def get_reflected_row_locations(self, acceptable_symbol_difference:int=0):
        height = self.get_height(); width = self.get_width()

        row_locations = []
        for row in range(height-1):
            differences = 0
            for offset in range(height):
                left = row - offset
                right = row + 1 + offset

                if left >= 0 and right < height:
                    # Check similarity of row (point by point)
                    for rp in range(width):
                        if self.get_symbol(point.Point2D(rp, left)) != self.get_symbol(point.Point2D(rp, right)):
                            differences += 1

            if differences == acceptable_symbol_difference:
                location = row + 1
                #print(f"DEBUG: Vertical symmetry found at {location}")
                row_locations.append(location)
        return row_locations

    def get_reflected_column_locations(self, acceptable_symbol_differences:int=0):
        height = self.get_height(); width = self.get_width()

        col_locations = []
        for column in range(width-1):
            differences = 0
            for offset in range(width):
                top = column - offset
                bottom = column + 1 + offset

                if top >= 0 and bottom < width:
                    # Check similarity of column (point by point)
                    for cp in range(height):
                        if self.get_symbol(point.Point2D(top, cp)) != self.get_symbol(point.Point2D(bottom, cp)):
                            differences += 1

            if differences == acceptable_symbol_differences:
                location = column + 1
                #print(f"DEBUG: Horizontal symmetry found at {location}")
                col_locations.append(location)
            
        return col_locations 
    

    def get_symbols_in_direction(self, current_point:point.Point2D, offset:int, x_increment:int, y_increment:int):        
        str = ""
        for i in range(offset):            
            next_point = point.Point2D(current_point.get_x() + (i * x_increment), current_point.get_y() + (i * y_increment))
            if not self.contains(next_point):
                break
            str += self.get_symbol(next_point)
        return str

    def get_symbols_in_direction_north(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, 0, 1)

    def get_symbols_in_direction_east(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, 1, 0)

    def get_symbols_in_direction_south(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, 0, -1)

    def get_symbols_in_direction_west(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, -1, 0)

    def get_symbols_in_direction_northeast(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, -1, 1)

    def get_symbols_in_direction_southeast(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, 1, 1)

    def get_symbols_in_direction_southwest(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, 1, -1)

    def get_symbols_in_direction_northwest(self, current_point:point.Point2D, offset:int):
        return self.get_symbols_in_direction(current_point, offset, -1, -1)


    def clone(self):
        cloned_grid = Grid2D(self.get_width(), self.get_height())

        for w in range(cloned_grid.get_width()):
            for h in range(cloned_grid.get_height()):
                p = point.Point2D(w,h)
                cloned_grid.set_symbol(p, self.get_symbol(p))

        return cloned_grid
    
    def __eq__(self,other) -> bool:
        if other == None or self.get_width() != other.get_width() or self.get_height() != other.get_height():
            return False
        
        for w in range(self.get_width()):
            for h in range(self.get_height()):
                p = point.Point2D(w,h)
                if self.get_symbol(p) != other.get_symbol(p):
                    return False
                
        return True
    
    def __hash__(self):
        value  = ""
        for w in range(self.get_width()):
            for h in range(self.get_height()):
                p = point.Point2D(w,h)
                value += str(w) + str(h) + self.get_symbol(p)
        return hash(value)