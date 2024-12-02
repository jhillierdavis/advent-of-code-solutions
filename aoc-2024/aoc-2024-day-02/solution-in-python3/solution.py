from helpers import fileutils

def is_safe_gradually_increasing(diff):
    for d in diff:
        if d < 1 or d > 3:
            return False
    return True


def is_safe_gradually_decreasing(diff):
    for d in diff:
        if d > -1 or d < -3:
            return False
    return True


def to_int_array_from(array_str):
    values = [int(numeric_string) for numeric_string in array_str]
    return values


def get_diff_array_from(array_int):
    
    array_diffs = []
    last = -1
    for e in array_int:        
        if last != -1:
            array_diffs.append(e - last)
        last = e    
    return array_diffs


def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    count_safe = 0
    for l in lines:
        #print(f'DEBUG: l={l}')
        values = to_int_array_from(l.split(' '))

        diff = get_diff_array_from(values)
        #print(f'DEBUG: diff={diff}')

        if is_safe_gradually_decreasing(diff) or is_safe_gradually_increasing(diff):
            count_safe += 1

    return count_safe


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    count_safe = 0
    for l in lines:
        #print(f'DEBUG: l={l}')
        values = to_int_array_from(l.split(' '))

        for i in range(len(values)):
            partial_copy = []
            for j in range(len(values)):
                if i == j:
                    continue
                partial_copy.append(values[j])

            diff = get_diff_array_from(partial_copy)

            if is_safe_gradually_increasing(diff) or is_safe_gradually_decreasing(diff):
                #print(f'DEBUG: Safe: diff={diff}')
                count_safe += 1
                break

    return count_safe