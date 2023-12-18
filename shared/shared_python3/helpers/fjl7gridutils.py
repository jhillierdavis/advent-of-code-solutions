from helpers.grid import grid_to_lines, Grid2D

""" 

An 'FJL7' grid use the characters F,L,J,S and 7, plus '-' and '|' to depict a (e.g. looping) path in a 2D grid e.g.:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

S = Start
- = horizontal
| = vertical 
J = right angle turn: right to up / north or down to left / west
7 = right angle turn: right to down / south or up to left / west
F = right angle turn: left to down / south or up to right / east
L = right angle turn: left to up / north or down to right / east

"""

def count_contained_squares_from_fjl7_grid_line(line:str) -> int:
    # Use ray casting approach from AOC 2023 Day 10 Part 2
    
    is_within = False

    line = line.replace('-', '')
    line = line.replace('S', '|') # TODO: Is this a valid assumption?
    line = line.replace('LJ', '||') # NB: escape '|' (vertical pipe) by using another in Python
    line = line.replace('L7', '|')
    line = line.replace('FJ', '|')
    line = line.replace('F7', '||')
    #print(f"DEBUG: line={line}")
    wall_count = 0
    tmp_count = 0
    total_count = 0
    for i in range(len(line)):
        chr = line[i]
        if chr in '|':
            is_within = False if is_within else True
            wall_count += 1
            if wall_count % 2 == 0:
                total_count += tmp_count
                tmp_count = 0
        elif '.' == chr and i > 0 and is_within:
            tmp_count += 1
    return total_count


def count_contained_squares_from_fjl7_grid(fjl7_grid:Grid2D):
    lines = grid_to_lines(fjl7_grid)
    count = 0
    for l in lines:
        count += count_contained_squares_from_fjl7_grid_line(l)
    return count
