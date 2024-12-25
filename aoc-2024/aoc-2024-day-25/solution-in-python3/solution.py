from helpers import fileutils, grid, point


def is_lock(g):
    p = point.Point2D(0, 0)
    s = g.get_symbol(p)
    if s == '#':
        return True
    return False


def count_column_blocks(g):
    blocks = []

    for w in range(g.get_width()):
        size = 0
        for h in range(1, g.get_height()-1):
            p = point.Point2D(w, h)
            s = g.get_symbol(p)
            if s == '#':
                size += 1
        blocks.append(size)
    return blocks


def to_key(g):
    if is_lock(g):
        return None
    return count_column_blocks(g)


def to_lock(g):
    if not is_lock(g):
        return None
    return count_column_blocks(g)


def is_fit(lock, key):
    
    for i in range(5):
        sum = lock[i] + key[i]
        #print(f"DEBUG: sum={sum} {lock[i]} {key[i]}" )
        if sum > 5:
            return False
    return True


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    grid_list = list()

    glines_list = []
    for l in lines:
        if len(l.strip()) == 0 :
            g = grid.lines_to_grid(glines_list)
            grid_list.append(g)
            glines_list.clear()
        else:
            glines_list.append(l)

    g = grid.lines_to_grid(glines_list)
    grid_list.append(g)

    lock_list = []
    key_list = []
    for g in grid_list:
        grid.display_grid(g)
        if is_lock(g):
            lock = to_lock(g)
            print(f'DEBUG: lock={lock}')
            lock_list.append(lock)
        else:
            key = to_key(g)
            print(f'DEBUG: key={key}')
            key_list.append(key)
        print()

    ans = 0
    for lock in lock_list:
        for key in key_list:
            does_fit = is_fit(lock, key)
            if does_fit:
                ans += 1
            #print(f"DEBUG: lock={lock} key={key} fit={does_fit}")

    return ans