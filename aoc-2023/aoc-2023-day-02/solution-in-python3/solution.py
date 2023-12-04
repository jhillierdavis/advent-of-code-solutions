from helpers import fileutils

from collections import defaultdict



def solve_part1(filename):
    valid_game_count = 0

    lines = fileutils.get_file_lines(filename)
    for l in lines:
        is_valid = True
        (g,r) = l.split(":")
        print(f"DEBUG: {g}")
        game_number = int(g.split()[1].strip())

        sets = r.split(';')

        for s in sets:
            values = s.split(",")

            map_colours = defaultdict(int)
            for v in values:
                (n,c) = v.strip().split()
                if c in map_colours.keys():
                    map_colours[c] = map_colours[c] + int(n)
                else:
                    map_colours[c] = int(n)

            if map_colours['red'] > 12 or map_colours['green'] > 13 or map_colours['blue'] > 14:
                 is_valid = False

        if is_valid:
                print(f"DEBUG: Valid game line = {l}")
                valid_game_count += game_number
        print(f"DEBUG: {map_colours}")
    return valid_game_count

def solve_part2(filename):    
    total_power = 0

    lines = fileutils.get_file_lines(filename)
    for l in lines:
        (g,r) = l.split(":")
        print(f"DEBUG: {g}")
    
        sets = r.split(';')

        map_colours = defaultdict(int)
        for s in sets:
            values = s.split(",")


            for v in values:                
                (n,c) = v.strip().split()
                colour_value = int(n)
                if c in map_colours.keys():                    
                    if colour_value > map_colours[c]:
                        map_colours[c] = colour_value
                else:
                    map_colours[c] = colour_value


        power = map_colours['red'] * map_colours['green'] * map_colours['blue']
        total_power += power

        print(f"DEBUG: {map_colours} power={power}")
    return total_power