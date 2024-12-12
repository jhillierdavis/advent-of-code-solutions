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

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    grid.display_grid(g)

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
            print(f"DEBUG: s={s} area={area} perimeter={perimeter} price={price}")
            ans += price
            
    return ans


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    g = grid.lines_to_grid(lines)
    grid.display_grid(g)
    return "TODO"