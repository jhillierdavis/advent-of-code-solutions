# Ref.: https://adventofcode.com/2021/day/2

import utils

def calculate_position_from_file(filename):
    position_depth:int = 0
    position_horizontal:int = 0

    lines = utils.get_file_lines(filename)
    #print(f"DEBUG: {lines}")

    for line in lines:
        entries = line.split()
        value = int(entries[1])
        if entries[0] == 'forward':
            position_horizontal += value
        elif entries[0] == 'down':
            position_depth += value
        elif entries[0] == 'up':
            position_depth -= value

    return position_depth * position_horizontal

def calculate_position_using_aim_from_file(filename):
    position_depth:int = 0
    position_horizontal:int = 0
    aim:int = 0

    lines = utils.get_file_lines(filename)
    #print(f"DEBUG: {lines}")

    for line in lines:
        entries = line.split()
        value = int(entries[1])
        if entries[0] == 'forward':
            position_horizontal += value
            position_depth += aim * value
        elif entries[0] == 'down':
            aim += value
        elif entries[0] == 'up':
            aim -= value

    return position_depth * position_horizontal
