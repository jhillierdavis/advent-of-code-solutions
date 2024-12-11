import re

from helpers import fileutils


def count_multiplications_in(text, is_enabler_active=False):
    # Match via groups (with sub-groups for integer values)
    pattern = re.compile(r'mul\((\d+),(\d+)\)')

    enabler_text = 'do()'
    enabler_size = len(enabler_text)

    disabler_text = "don't()"
    disabler_size = len(disabler_text)
   
    count = 0    
    enabled = True
    for i in range(len(text)):
        if is_enabler_active:
            if text[i:].startswith(enabler_text):
                enabled = True
                i += enabler_size
                continue
            elif text[i:].startswith(disabler_text):
                enabled = False
                i += disabler_size
                continue

        match = pattern.match(text[i:])
        if match is not None and enabled:
            count += int(match.group(1)) * int(match.group(2)) 

    return count    


def solve_part1(filename):
    text = fileutils.get_text_from(filename)
    return count_multiplications_in(text)

    # Alt.: more succinct solution approach (from others following review after solved)
    #return sum( int(x) * int(y) for x,y in re.findall(r"mul\((\d+),(\d+)\)", text))


def solve_part2(filename):
    text = fileutils.get_text_from(filename)
    return count_multiplications_in(text, True)