from collections import defaultdict, deque

from helpers import fileutils, grid, point


def get_symbol_to_position_map(g:grid.Grid2D) -> defaultdict:
    map = defaultdict(list)

    for h in range(g.get_height()):
        for w in range(g.get_width()):
            p = point.Point2D(w,h)
            s = g.get_symbol(p)
            if s in map:
                continue

            sps = g.get_points_matching(s)
            map[s] = sps

    #print(f"DEBUG: map.keys={map.keys()}")
    #print(f"DEBUG: map={map}")
    return map    

def populate_continguous_region(g:grid.Grid2D, s, sp, region):
    
    nps = g.get_cardinal_point_neighbours(sp)
    for n in nps:
        if n in region:
            continue

        if g.get_symbol(n) == s:
            region.add(n)
            populate_continguous_region(g, s, n, region)
        

def get_contiguous_region_containing(g:grid.Grid2D, s, sp):
    region = set()
    region.add(sp)
    populate_continguous_region(g, s, sp, region)
    return region


def get_contiguous_regions(g:grid.Grid2D, s, sps):
    regions = []

    for p in sps:
        region = get_contiguous_region_containing(g, s, p)
        if region not in regions:
            regions.append(region)
    return regions



def count_regions(g:grid.Grid2D) -> int:
    map = get_symbol_to_position_map(g)

    count = 0
    for s, sps in map.items():
        #print(f"DEBUG; sps={sps}")
        # For each symbol count distinct regions
        regions = get_contiguous_regions(g, s, sps)
        region_count = len(regions)
        #print(f"DEBUG: s={s} region_count={region_count} regions={regions}")
        count += region_count

    return count


def calculate_area(region):
    return len(region)


def calculate_perimeter(g, s, region):
    size =  len(region)

    if size == 0:
        return 0
    
    if size == 1:
        return 4
    
    count = 0
    for p in region:
        nps = g.get_cardinal_point_neighbours(p)
        n_count = 0
        for n in nps:
            ns = g.get_symbol(n)
            if ns == s:
                n_count += 1
        count += 4 - n_count

    return count


def get_min_max_points_for_region_points(region, w, h):
    min_x = w
    min_y = h
    max_x = 0
    max_y = 0

    for r in region:
        x = r.get_x()
        y = r.get_y()

        if x < min_x:
            min_x = x

        if y < min_y:
            min_y = y

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y
    return min_x, min_y, 1+max_x, 1+max_y


def calculate_sides(g, s, region):
    size =  len(region)

    if size == 0:
        return 0
    
    if size == 1:
        return 4
    
    
    count = 0
    
    
    
    min_x, min_y, max_x, max_y = get_min_max_points_for_region_points(region, g.get_width(), g.get_height())

    count_sides_north = 0
    count_sides_south = 0
    
    # Count horizontal side
    for h in range(min_y,max_y):        
        in_side_north = False
        in_side_south = False
        for w in range(min_x,max_x):
            p = point.Point2D(w, h)
            if p in region:            
                n_north = g.get_neighbour_north(p)                
                if n_north in region:
                    in_side_north = False
                elif not in_side_north:
                    in_side_north = True                    
                    count_sides_north += 1

                n_south = g.get_neighbour_south(p)
                if n_south in region:
                    in_side_south = False
                elif not in_side_south:
                    in_side_south = True                    
                    count_sides_south += 1
            else:
                in_side_north = False
                in_side_south = False                    

    count_sides_east = 0
    count_sides_west = 0
    for w in range(min_x,max_x): 
        in_side_east = False
        in_side_west = False
        for h in range(min_y,max_y): 
            p = point.Point2D(w, h)
            if p in region:            
                n_east = g.get_neighbour_east(p)
                if n_east in region:
                    in_side_east = False
                elif not in_side_east:
                    #print(f"DEBUG: side east at p={p}")
                    in_side_east = True                    
                    count_sides_east += 1

                n_west  = g.get_neighbour_west(p)
                if n_west in region:
                    in_side_west = False
                elif not in_side_west:
                    in_side_west = True                    
                    count_sides_west += 1
            else:
                in_side_east = False
                in_side_west = False                    


    
    count = count_sides_north + count_sides_south + count_sides_east + count_sides_west
    #print(f"DEBUG: count={count} count_sides_north={count_sides_north} count_sides_south={count_sides_south} count_sides_east={count_sides_east} count_sides_west={count_sides_west}")    
    return count


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    map = get_symbol_to_position_map(g)

    ans = 0
    for s, sps in map.items():
        #print(f"DEBUG; sps={sps}")
        # For each symbol count distinct regions
        regions = get_contiguous_regions(g, s, sps)        

        for r in regions:
            area = calculate_area(r)
            perimeter = calculate_perimeter(g, s, r)
            price = area * perimeter
            #print(f"DEBUG: s={s} area={area} r={r}")
            #print(f"DEBUG: s={s} area={area} perimeter={perimeter} price={price}")
            ans += price
            
    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    #grid.display_grid(g)

    map = get_symbol_to_position_map(g)

    ans = 0
    for s, sps in map.items():
        #print(f"DEBUG; sps={sps}")
        # For each symbol count distinct regions
        regions = get_contiguous_regions(g, s, sps)        

        for r in regions:
            area = calculate_area(r)
            sides = calculate_sides(g, s, r)
            price = area * sides
            #print(f"DEBUG: s={s} area={area} r={r}")
            #print(f"DEBUG: s={s} area={area} sides={sides} price={price}")
            ans += price
            
    return ans