from helpers import fileutils

def mix(num, mixin):
    return mixin ^ num 

def prune(num):
    return num % 16777216

def generate_next_secret_number(initial):
    next = initial

    mixin = 64 * initial
    next = mix(next, mixin)
    next = prune(next)

    mixin = next // 32
    next = mix(next, mixin)
    next = prune(next)

    mixin = next * 2048
    next = mix(next, mixin)
    next = prune(next)

    return next


def generate_secret_number_sequence(initial, max):
    sequence = []
    next = initial
    for _ in range(max):
        next = generate_next_secret_number(next)
        sequence.append(next)
    return sequence

def generate_nth_secret_number(initial, n):
    next = initial
    for _ in range(n):
        next = generate_next_secret_number(next)
    return next


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    count = 0
    for l in lines:
        num = int(l)
        count += generate_nth_secret_number(num, 2000)

    return count


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    return -1