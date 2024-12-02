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

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)

    count_safe = 0
    for l in lines:
        #print(f'DEBUG: l={l}')
        a = l.split(' ')
        last = -1
        diff = []
        for v in a:        
            value = int(v)
            if last != -1:
                diff.append(value - last)
            last = value
        #print(f'DEBUG: diff={diff}')
        if is_safe_gradually_decreasing(diff) or is_safe_gradually_increasing(diff):
            count_safe += 1

    return count_safe

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    count_safe = 0
    for l in lines:
        #print(f'DEBUG: l={l}')
        a = l.split(' ')
        values = []
        for v in a:        
            values.append(int(v))

        for i in range(len(values)):
            partial_copy = []
            for j in range(len(values)):
                if i == j:
                    continue
                partial_copy.append(values[j])

            last = -1
            diff = []
            for e in partial_copy:        
                if last != -1:
                    diff.append(e - last)
                last = e
            
            if is_safe_gradually_increasing(diff) or is_safe_gradually_decreasing(diff):
                #print(f'DEBUG: Safe: diff={diff}')
                count_safe += 1
                break

    return count_safe