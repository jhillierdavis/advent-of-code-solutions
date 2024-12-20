from helpers import fileutils, grid, point, dijkstra


def find_single_symbol_point_and_clear(g, symbol):
    p = grid.get_single_symbol_point(g, symbol)
    g.set_symbol(p, '.')
    return p 


def get_cheat_paths(g:grid.Grid2D, max_size:int=1):
    spaces = g.get_points_matching('.') 

    cheat_paths = set()
    for sp in spaces:
        nps = g.get_cardinal_point_neighbours(sp)
        for np in nps:
            ns = g.get_symbol(np)
            if ns == '.':
                continue

            nnps = g.get_cardinal_point_neighbours(np)
            for nnp in nnps:
                nns = g.get_symbol(nnp)
                if nns == '#' or nnp == sp:
                    continue

                cheat_paths.add( (sp, nnp, 1, np))

    return cheat_paths




def get_shortest_path(filename) -> int:

    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = find_single_symbol_point_and_clear(g,'S')
    ep = find_single_symbol_point_and_clear(g,'E')
    
    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")
    
    count = dijkstra.get_least_steps(g, '#', sp, ep)
    return count


def get_shortest_path_with_cheat(filename) -> int:
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    sp = find_single_symbol_point_and_clear(g,'S')
    find_single_symbol_point_and_clear(g,'1')
    ep = find_single_symbol_point_and_clear(g,'2')

    points = g.get_points_matching('E')
    #print(f"DEBUG: points={points}")
    if len(points) > 0:
        ep = find_single_symbol_point_and_clear(g,'E')        

    #grid.display_grid(g)
    #print(f"DEBUG: sp={sp} ep={ep}")

    count = dijkstra.get_least_steps(g, '#', sp, ep)
    return count


def count_number_of_cheats_for_saving(filename, saving):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    sp = find_single_symbol_point_and_clear(g,'S')
    ep = find_single_symbol_point_and_clear(g,'E')
    
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

    sp = find_single_symbol_point_and_clear(g,'S')
    ep = find_single_symbol_point_and_clear(g,'E')
    
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


def count_number_of_cheats_for_saving_alt_approach(filename, saving):
    lines = fileutils.get_file_lines_from(filename)
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    sp = find_single_symbol_point_and_clear(g,'S')
    ep = find_single_symbol_point_and_clear(g,'E')
    count_original = dijkstra.get_least_steps(g, '#', sp, ep)

    cheat_paths = get_cheat_paths(g)

    map_d2s = dict()
    map_d2e = dict()

    spaces = g.get_points_matching('.')
    #print(f"DEBUG: spaces={spaces}")

    for p in spaces:        
        count = dijkstra.get_least_steps(g, '#', p, sp)
        map_d2s[p] = count

        count = dijkstra.get_least_steps(g, '#', p, ep)    
        map_d2e[p] = count            
       
    #print(f"DEBUG: map_d2s={map_d2s}")
    #print(f"DEBUG: map_d2e={map_d2e}")

    assert count_original == map_d2e[sp]
    assert count_original == map_d2s[ep]

    

    cheat_points = set()
    for entry in cheat_paths:
        cps, cpe, cpl, cpp = entry
        #print(f"DEBUG: entry={entry}")
        #print(f"DEBUG: cheat path: cps={cps} {g.get_symbol(cps)} cpe={cpe} {g.get_symbol(cpe)}")

        #if cps not in map_d2s.keys() or cpe not in map_d2e.keys():
        #    continue

        count_to_start = map_d2s[cps]
        count_to_end = map_d2e[cpe]

        count = count_to_start + cpl +  count_to_end + 1


        if count < count_original:
            diff = count_original - count 
            if diff == saving:
                #print(f"Saving diff={diff} count={count} count_original={count_original} for entry={entry}")
                cheat_points.add((cps, cpe))

    #print(cheat_points)
    return len(cheat_points)



def solve_part2(filename, saving):
    lines = fileutils.get_file_lines_from(filename)
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)

    sp = find_single_symbol_point_and_clear(g,'S')
    ep = find_single_symbol_point_and_clear(g,'E')
    count_original = dijkstra.get_least_steps(g, '#', sp, ep)

    cheat_paths = get_cheat_paths(g)

    map_d2s = dict()
    map_d2e = dict()

    spaces = g.get_points_matching('.')
    #print(f"DEBUG: spaces={spaces}")

    for p in spaces:        
        count = dijkstra.get_least_steps(g, '#', p, sp)
        map_d2s[p] = count

        count = dijkstra.get_least_steps(g, '#', p, ep)    
        map_d2e[p] = count            
       
    #print(f"DEBUG: map_d2s={map_d2s}")
    #print(f"DEBUG: map_d2e={map_d2e}")

    assert count_original == map_d2e[sp]
    assert count_original == map_d2s[ep]

    

    cheat_points = set()
    for entry in cheat_paths:
        cps, cpe, cpl, cpp = entry
        #print(f"DEBUG: entry={entry}")
        #print(f"DEBUG: cheat path: cps={cps} {g.get_symbol(cps)} cpe={cpe} {g.get_symbol(cpe)}")

        #if cps not in map_d2s.keys() or cpe not in map_d2e.keys():
        #    continue

        count_to_start = map_d2s[cps]
        count_to_end = map_d2e[cpe]

        count = count_to_start + cpl +  count_to_end + 1


        if count < count_original:
            diff = count_original - count 
            if diff >= saving:
                #print(f"Saving diff={diff} count={count} count_original={count_original} for entry={entry}")
                cheat_points.add((cps, cpe))

    #print(cheat_points)
    return len(cheat_points)