from helpers import fileutils, grid, point

def same_position(pa, pb) -> bool:
    return pa.get_x() == pb.get_x() and pa.get_y() == pb.get_y()    


def get_count_of_robots_at_position(robots, pos):
    count = 0
    for r in robots:
        p,_ = r
        if same_position(pos, p):
            count += 1
    return count


def get_robots_on_grid(robots, width, height):
    g = grid.Grid2D(width, height)
    for r in robots:
        p,v = r
        c = get_count_of_robots_at_position(robots, p)
        g.set_symbol(p,  str(c))
    return g


def get_moved_robots(robots, width, height):
    moved = []
    for r in robots:
        p,v = r
        x = p.get_x() + v.get_x() 
        if x < 0:
            x = width + x
        elif x >= width:
            x = x % width

        y = p.get_y() + v.get_y() 
        if y < 0:
            y = height + y
        elif y >= height:
            y = y % height

        np = point.Point2D(x,y)
        moved.append((np,v))
    return moved


def count_robots_on_grid_section(g, start_x, end_x, start_y, end_y):
    count = 0
    for h in range(start_y, end_y):
        for w in range(start_x, end_x):
            s = g.get_symbol(point.Point2D(w,h))
            if s != '.':
                count += int(s)
    #print(f"DEBUG: count={count}")
    return count
    

def get_robots_from(filename):
    lines = fileutils.get_file_lines_from(filename)
    robots = []
    for l in lines:
        left, right  = l.split()
        x,y = left[2:].split(',')
        p = point.Point2D(int(x),int(y))
        x,y = right[2:].split(',')
        v = point.Point2D(int(x),int(y))
        #print(f"DEBUG: p={p} v={v}")
        robots.append((p,v))
    return robots


def solve_part1(filename, width, height):
    robots = get_robots_from(filename)
    g = get_robots_on_grid(robots, width, height)
    
    grid.display_grid(g)
    print('')

    time_in_sec = 100
    for i in range(time_in_sec):
        robots = get_moved_robots(robots, width, height)
        g = get_robots_on_grid(robots, width, height)        
        
    grid.display_grid(g)
   
    count = 1
    #print(width//2, height//2)
    count *= count_robots_on_grid_section(g, 0, width//2, 0, height//2)
    count *= count_robots_on_grid_section(g, 1 + width//2, width, 0, height//2)
    count *= count_robots_on_grid_section(g, 0, width//2, 1 + height//2, height)
    count *= count_robots_on_grid_section(g, 1 + width//2, width, 1 + height//2, height)
    return count


def solve_part2(filename, width, height):
    #
    # NB: Intructions were not specific on how to identify the Xmas Tree depiction (or it's orientation)
    # 
    # Initialled I assumed a Xmas tree display upright and symmetically placed on the grid, 
    # so tried matching grid quadrants (from Part 1), but that approach failed to produce a match (over large iterations)
    #
    # THen I tried finding the grid display when all robots are in distinct unique positions, which contained the following embedded image:
    #
    # 1111111111111111111111111111111
    # 1.............................1
    # 1.............................1
    # 1.............................1
    # 1.............................1
    # 1..............1..............1
    # 1.............111.............1
    # 1............11111............1
    # 1...........1111111...........1
    # 1..........111111111..........1
    # 1............11111............1
    # 1...........1111111...........1
    # 1..........111111111..........1
    # 1.........11111111111.........1
    # 1........1111111111111........1
    # 1..........111111111..........1
    # 1.........11111111111.........1
    # 1........1111111111111........1
    # 1.......111111111111111.......1
    # 1......11111111111111111......1
    # 1........1111111111111........1
    # 1.......111111111111111.......1
    # 1......11111111111111111......1
    # 1.....1111111111111111111.....1
    # 1....111111111111111111111....1
    # 1.............111.............1
    # 1.............111.............1
    # 1.............111.............1
    # 1.............................1
    # 1.............................1
    # 1.............................1
    # 1.............................1
    # 1111111111111111111111111111111
    #

    robots = get_robots_from(filename)
    g = get_robots_on_grid(robots, width, height)
    
    grid.display_grid(g)
    print('')

    # Christmas Tree displayed when all robot positions are unique 
    time_in_sec = 10000
    for t in range(1, time_in_sec):
        robots = get_moved_robots(robots, width, height)

        all_unique_positions = True
        for r in robots:
            p,_ = r
            if get_count_of_robots_at_position(robots, p) > 1:
                all_unique_positions = False
                break
    
        if t > 0 and all_unique_positions:
            g = get_robots_on_grid(robots, width, height)   
            grid.display_grid(g)
            print(f'DEBUG: Number of seconds={t}\n\n')
            break

    return t