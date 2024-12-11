from helpers import fileutils

def count(values):
    stones = values.split(' ')
    return len(stones)

def split_value(value):
    size = len(value)
    midpoint = (size // 2)
    left = value[0:midpoint]
    right = value[midpoint:]
    #while right.startswith('0') and len(right) > 1:
    #    right = right[1:]
    return left + " " + str(int(right))

def transform(value):
    if value == '0':
        return '1'
    
    size = len(value)
    if size % 2  == 0: # Even
        return split_value(value)
    
    num = int(value)
    return str(2024 * num)


def transform_stones(values):
    stones = values.split(' ')
    evolved = ''
    for s in stones:
        evolved += transform(s) + ' '
    return evolved.strip()

def evolve_stones(values, blinks):
    evolved = values
    for _ in range(blinks):
        evolved = transform_stones(evolved)
    return evolved

def solve_part1(filename):
    line = fileutils.get_text_from(filename)
    evolved = evolve_stones(line, 25)
    return count(evolved)


def solve_part2(filename):
    line = fileutils.get_text_from(filename)
    evolved = evolve_stones(line, 75)
    return count(evolved)