from helpers import fileutils, grid, point, dijkstra


def get_shortest_path(filename) -> int:
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = grid.get_single_symbol_point(g,'S')
    g.set_symbol(sp, '.')

    ep = grid.get_single_symbol_point(g,'E')
    g.set_symbol(ep, '.')
    
    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")
    
    count = dijkstra.get_least_steps(g, '#', sp, ep)
    return count


def get_shortest_path_with_cheat(filename) -> int:
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    cp = grid.get_single_symbol_point(g,'1')
    g.set_symbol(cp, '.')

    cp = grid.get_single_symbol_point(g,'2')
    g.set_symbol(cp, '.')
    ep = cp

    sp = grid.get_single_symbol_point(g,'S')
    g.set_symbol(sp, '.')

    points = g.get_points_matching('E')
    #print(f"DEBUG: points={points}")
    if len(points) > 0:
        ep = grid.get_single_symbol_point(g,'E')
        g.set_symbol(ep, '.')    

    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")

    count = dijkstra.get_least_steps(g, '#', sp, ep)
    return count


def count_number_of_cheats_for_saving(filename, saving):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = grid.get_single_symbol_point(g,'S')
    g.set_symbol(sp, '.')

    ep = grid.get_single_symbol_point(g,'E')
    g.set_symbol(ep, '.')
    
    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")

    count = dijkstra.get_least_steps(g, '#', sp, ep)
    target = count - saving
    print(f"DEBUG: target={target} count={count} saving={saving}")

    spaces = g.get_points_matching('.') 
    total_count = 0
    cheat_point_set = set()
    for pp in spaces:
        nps = g.get_cardinal_point_neighbours(pp)
        for np in nps:
            if np in cheat_point_set:
                continue

            ns = g.get_symbol(np)
            if ns == '#':
                gc = g.clone()
                gc.set_symbol(np, '.') # Cheat
                count = dijkstra.get_least_steps(gc, '#', sp, ep)
                if count > 0 and count == target :
                    cheat_point_set.add(np)
                    total_count += 1
    

    return total_count


def solve_part1(filename, saving):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = grid.get_single_symbol_point(g,'S')
    g.set_symbol(sp, '.')

    ep = grid.get_single_symbol_point(g,'E')
    g.set_symbol(ep, '.')
    
    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")

    count = dijkstra.get_least_steps(g, '#', sp, ep)
    target = count - saving
    print(f"DEBUG: target={target} count={count} saving={saving}")

    spaces = g.get_points_matching('.') 
    total_count = 0
    cheat_point_set = set()
    for pp in spaces:
        nps = g.get_cardinal_point_neighbours(pp)
        for np in nps:
            if np in cheat_point_set:
                continue

            # Check that provides a usable cheat path
            nnps = g.get_cardinal_point_neighbours(pp)
            num = 0
            for nnp in nnps:
                nns = g.get_symbol(nnp)
                if nns == '.':
                    num += 1
            if num <= 1:
                continue

            ns = g.get_symbol(np)
            if ns == '#':
                gc = g.clone()
                gc.set_symbol(np, '.') # Cheat
                count = dijkstra.get_least_steps(gc, '#', sp, ep)
                if count > 0 and count <= target:
                    cheat_point_set.add(np)
                    total_count += 1
    

    return total_count


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    return "TODO"