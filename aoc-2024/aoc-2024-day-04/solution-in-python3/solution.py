from helpers import fileutils, grid, point


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    #grid.display_grid(g)

    count = 0
    height = g.get_height()
    width = g.get_width()
    for h in range(height):
        for w in range(width):
            p  = point.Point2D(w,h)
            if g.get_symbol(p) == 'X':

                # Forward
                next = point.Point2D(p.get_x() + 1, p.get_y())
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() + 2, p.get_y())
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() + 3, p.get_y())
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x() -1, p.get_y())
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() -2, p.get_y())
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() -3, p.get_y())
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x(), p.get_y() + 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x(), p.get_y() + 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x(), p.get_y() + 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x(), p.get_y() - 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x(), p.get_y() - 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x(), p.get_y() - 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x() +1, p.get_y() + 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() +2, p.get_y() + 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() +3, p.get_y() + 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x() - 1, p.get_y() - 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() - 2, p.get_y() - 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() - 3, p.get_y() - 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x() + 1, p.get_y() - 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() + 2, p.get_y() - 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() + 3, p.get_y() - 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

                next = point.Point2D(p.get_x() - 1, p.get_y() + 1)
                if g.contains(next) and g.get_symbol(next) == 'M':
                    next = point.Point2D(p.get_x() - 2, p.get_y() + 2)
                    if g.contains(next) and g.get_symbol(next) == 'A':
                        next = point.Point2D(p.get_x() - 3, p.get_y() + 3)
                        if g.contains(next) and g.get_symbol(next) == 'S':
                             count += 1

    return count


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    count = 0
    height = g.get_height()
    width = g.get_width()
    for h in range(height):
        for w in range(width):
            p  = point.Point2D(w,h)
            if g.get_symbol(p) == 'A':
                ne = point.Point2D(p.get_x() - 1, p.get_y() - 1)
                nw = point.Point2D(p.get_x() + 1, p.get_y() - 1)
                se = point.Point2D(p.get_x() - 1, p.get_y() + 1)
                sw = point.Point2D(p.get_x() + 1, p.get_y() + 1)
                if g.contains(ne) and g.contains(nw) and g.contains(se) and g.contains(sw):
                    nes = g.get_symbol(ne)
                    nws = g.get_symbol(nw)
                    ses = g.get_symbol(se)
                    sws = g.get_symbol(sw)

                    if nes == 'M' and sws == 'S' and nws == 'M' and ses == 'S':
                        count += 1              
                    elif nes == 'S' and sws == 'M' and nws == 'M' and ses == 'S':
                        count += 1              
                    elif nes == 'S' and sws == 'M' and nws == 'S' and ses == 'M':
                        count += 1              
                    elif nes == 'M' and sws == 'S' and nws == 'S' and ses == 'M':
                        count += 1              

    return count