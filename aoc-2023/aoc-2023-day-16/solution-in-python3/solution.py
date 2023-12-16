from collections import defaultdict

from helpers import fileutils, grid, point

def move_beam(g:grid.Grid2D, emap, cp:point.Point2D, direction:chr):
    es = emap[cp]
    assert not ('|' in es)

    # Terminating case    
    if direction in es:
        grid.display_grid(g)
        print(f"DEBUG: Move beam: Terminating at cp={cp} with es={es} direction={direction}")
        return
    
    emap[cp] = es + direction # Store coords and their direction traversed
    print(f"DEBUG: Move beam: cp={cp} direction={direction} es={es}")    

    if direction == '>':
        # Move right
        np = point.Point2D(1 + cp.get_x(), cp.get_y()) # Next point
        if g.contains(np):            
            ns = g.get_symbol(np)
            if ns == '.' or ns == '-':
                move_beam(g, emap, np, '>')
            else:
                if ns == '|':
                    move_beam(g, emap, np, '^')
                    move_beam(g, emap, np, 'v')
                elif ns == '/':
                    move_beam(g, emap, np, '^')
                elif ns == '\\':
                    move_beam(g, emap, np, 'v')

    if direction == '<':
        # Move left
        np = point.Point2D(cp.get_x() - 1, cp.get_y()) # Next point
        if g.contains(np):            
            ns = g.get_symbol(np)
            if ns == '.' or ns == '-':
                move_beam(g, emap, np, '<')
            else:
                if ns == '|':
                    move_beam(g, emap, np, '^')
                    move_beam(g, emap, np, 'v')
                elif ns == '/':
                    move_beam(g, emap, np, 'v')
                elif ns == '\\':
                    move_beam(g, emap, np, '^')

    elif direction == 'v':
        # Move down
        np = point.Point2D(cp.get_x(), 1 + cp.get_y()) # Next point
        if g.contains(np):            
            ns = g.get_symbol(np)
            if ns == '.' or ns == '|':
                move_beam(g, emap, np, 'v')
            else:
                if ns == '-':
                    move_beam(g, emap, np, '<')
                    move_beam(g, emap, np, '>')
                elif ns == '/':
                    move_beam(g, emap, np, '<')
                elif ns == '\\':
                    move_beam(g, emap, np, '>')

    elif direction == '^':
        # Move up
        np = point.Point2D(cp.get_x(), cp.get_y() - 1) # Next point
        if g.contains(np):            
            ns = g.get_symbol(np)
            if ns == '.' or ns == '|':
                move_beam(g, emap, np, '^')
            else:
                if ns == '-':
                    move_beam(g, emap, np, '<')
                    move_beam(g, emap, np, '>')
                elif ns == '/':
                    move_beam(g, emap, np, '>')
                elif ns == '\\':
                    move_beam(g, emap, np, '<')
        


def get_energised_coords(g:grid.Grid2D):
    emap = defaultdict(str)
    cp = point.Point2D(0,0)

    move_beam(g, emap, cp, '>')

    print(f"DEBUG: emap={emap}")
    return emap.keys()

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    g = grid.lines_to_grid(lines)
    #eg = g.clone()
    #grid.display_grid(eg)

    energised = get_energised_coords(g)
    return len(energised)






def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

