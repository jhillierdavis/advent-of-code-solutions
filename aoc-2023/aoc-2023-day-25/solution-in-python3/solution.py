#from collections import defaultdict

from helpers import fileutils

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    wiring_map = {}
    for l in lines:
        k, vl = l.split(': ')
        v = vl.split()
        wiring_map[k] = v

    print(f"DEBUG: wiring_map={wiring_map}")

    return 0 # TODO

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

