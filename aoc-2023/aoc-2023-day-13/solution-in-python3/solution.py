from collections import defaultdict

from helpers import fileutils, grid, point

def get_symmetry_row(g, target_mismatch:int=0):
    height = g.get_height()
    width = g.get_width()

    for row in range(height-1):
        mismatch = 0
        for offset in range(height):
            left = row - offset
            right = row + 1 + offset

            if left >= 0 and right < height:
                # Check similarity of row (point by point)
                for rp in range(width):
                    if g.get_symbol(point.Point2D(rp, left)) != g.get_symbol(point.Point2D(rp, right)):
                        mismatch += 1

        if mismatch == target_mismatch:
            location = row + 1
            print(f"DEBUG: Vertical symmetry found at {location}")
            return location
        
    return -1 # Symmetry mot found

def get_symmetry_column(g, target_mismatch:int=0):
    height = g.get_height()
    width = g.get_width()

    for column in range(width-1):
        mismatch = 0
        for offset in range(width):
            top = column - offset
            bottom = column + 1 + offset

            if top >= 0 and bottom < width:
                # Check similarity of column (point by point)
                for cp in range(height):
                    if g.get_symbol(point.Point2D(top, cp)) != g.get_symbol(point.Point2D(bottom, cp)):
                        mismatch += 1

        if mismatch == target_mismatch:
            location = column + 1
            print(f"DEBUG: Horizontal symmetry found at {location}")
            return location
        
    return -1  # Symmetry mot found 


def solve(filename, target_mismatch:int=0):
    grids = grid.get_multiple_grids_from(filename)

    index = 0
    total = 0
    for g in grids:
        index += 1
        #print(f"DEBUG: Finding relection point for grid")
        location = get_symmetry_column(g, target_mismatch)
        if location < 0:
            location = get_symmetry_row(g, target_mismatch) * 100
        
        assert location > 0 , f"No symmetry found for index={index} grid={g}"        
        
        total += location


    return total


def solve_part1(filename):
    return solve(filename)

def solve_part2(filename):
    return solve(filename, 1)