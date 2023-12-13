from helpers import grid, point

def solve(filename, acceptable_differences:int=0):
    grids = grid.get_multiple_grids_from(filename)

    total = 0
    for g in grids:
        locations = g.get_reflected_column_locations(acceptable_differences)   
        #print(f"DEBUG: Column locations={locations}")     
        if len(locations) <= 0:
            locations = g.get_reflected_row_locations(acceptable_differences)
            #print(f"DEBUG: Row locations={locations}")     
            total += locations[0] * 100
        else:
            total += locations[0]

    return total


def solve_part1(filename):
    return solve(filename)

def solve_part2(filename):
    return solve(filename, 1)