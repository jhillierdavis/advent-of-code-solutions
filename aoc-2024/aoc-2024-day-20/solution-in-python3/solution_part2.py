from helpers import fileutils, grid, pathutils


def get_path(filename):
    lines = fileutils.get_file_lines(filename)
    g = grid.lines_to_grid(lines)

    sp = grid.find_single_symbol_point_and_replace(g, 'S', pathutils.DEFAULT_PATH_SYMBOL)
    #ep = grid.find_single_symbol_point_and_replace(g, 'E', pathutils.DEFAULT_PATH_SYMBOL)
    points = g.get_points_matching('1')
    if len(points) > 0:
        grid.find_single_symbol_point_and_replace(g,'1', pathutils.DEFAULT_PATH_SYMBOL)

    points = g.get_points_matching('2')
    if len(points) > 0:
        ep = grid.find_single_symbol_point_and_replace(g,'2', pathutils.DEFAULT_PATH_SYMBOL)

    points = g.get_points_matching('E')
    #print(f"DEBUG: points={points}")
    if len(points) > 0:
        ep = grid.find_single_symbol_point_and_replace(g, 'E', pathutils.DEFAULT_PATH_SYMBOL)    

    path = pathutils.get_quickest_path(g, sp, ep)
    #print(f"DEBUG: path={path}")    
    return path


def create_path_position_to_distance_map(path):
    path_dist_map = {}
    for e in enumerate(path):
        d, p = e
        #print(f"DEBUG: i={i} p={p}")
        path_dist_map[p] = d

    #print(f"DEBUG: path_dist_map={path_dist_map}")
    return path_dist_map


def get_best_chart_path_length(filename, cheat_duration=2):
    path = get_path(filename)
    if path == None:
        return 0
    
    path_dist_map = create_path_position_to_distance_map(path)

    size = len(path)
    min_length = size
    for i in range(size - 2):
        p1 = path[i]
        for j in range(i+2, size):
            p2 = path[j]

            if p1 == p2:
                continue

            md =  p1.get_manhatten_distance_to(p2)
            if md >= 2 and md <= cheat_duration and path_dist_map[p2] > path_dist_map[p1]:
                diff = path_dist_map[p2] - path_dist_map[p1]
                if size + md - diff < min_length:
                    min_length = size + md - diff

    return min_length


def count_number_of_cheats_for_exact_saving(filename, min_saving, cheat_duration):
    path = get_path(filename)
    path_dist_map = create_path_position_to_distance_map(path)

    count = 0
    size = len(path)
    for i in range(size - 2):
        p1 = path[i]
        for j in range(i+2, size):
            p2 = path[j]

            if p1 == p2:
                continue

            md =  p1.get_manhatten_distance_to(p2)
            if md >= 2 and md <= cheat_duration and path_dist_map[p2] > path_dist_map[p1]:
                diff = path_dist_map[p2] - path_dist_map[p1]
                if diff == min_saving + md:
                    count += 1

    return count


def count_number_of_cheats_for_saving_or_less(filename, min_saving, cheat_duration):
    path = get_path(filename)
    path_dist_map = create_path_position_to_distance_map(path)

    count = 0
    size = len(path)
    for i in range(size - 2):
        p1 = path[i]
        for j in range(i+2, size):
            p2 = path[j]

            if p1 == p2:
                continue

            md =  p1.get_manhatten_distance_to(p2)
            if md >= 2 and md <= cheat_duration and path_dist_map[p2] > path_dist_map[p1]:
                diff = path_dist_map[p2] - path_dist_map[p1]
                if diff >= min_saving + md:
                    count += 1

    return count