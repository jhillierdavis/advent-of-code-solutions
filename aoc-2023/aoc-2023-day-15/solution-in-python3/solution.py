from collections import defaultdict

from helpers import fileutils

def hash_of(input):
    value = 0

    for i in range(len(input)):
        char = input[i]
        value += ord(char)
        value *= 17
        value = value % 256        
    return value

def solve_part1(filename):
    lines = fileutils.get_file_lines(filename)

    assert len(lines) == 1

    entries = lines[0].split(',')
    print(f"DEBUG: entries={entries}")

    sum = 0
    for e in entries:
        sum += hash_of(e)
    return sum

def focusing_power_of(input):
    # TODO
    return 0

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)

    assert len(lines) == 1

    entries = lines[0].split(',')
    print(f"DEBUG: entries={entries}")

    boxes = defaultdict(list)

    for e in entries:

        if e.endswith('-'):
            label = e[:-1]
            box = hash_of(label)
            print(f"DEBUG: label={label} box={box}")
            content = boxes[box]
            new_content = []
            for item in content:
                if item[0] == label:
                    print(f"DEBUG: Removing label={label} at box={box}")
                else:
                    new_content.append(item)
            boxes[box] = new_content
        else:
            (label,focal_length) = e.split('=')
            box = hash_of(label)
            print(f"DEBUG: label={label} focal_length={focal_length} box={box}")
            value = (label,int(focal_length))
            content = boxes[box]
            if content == []: # Empty
                boxes[box] = [value]
            else:
                new_content = []
                is_replacement = False
                for item in content:
                    if item[0] == label:
                        new_content.append(value)
                        is_replacement = True
                    else:
                        new_content.append(item)
                if is_replacement == False:
                    new_content.append(value)
                boxes[box] = new_content
        #sum += focusing_power_of(e)
        print(f"DEBUG: boxes={boxes}")

    sum = 0
    for box_number in range(0,256):
        content = boxes[box_number]

        slot = 1
        for item in content:
            focal_length = item[1]
            power = (1 + box_number) * slot * focal_length
            print(f"DEBUG: box_number={box_number} slot={slot} label={item[0]} focal_length={focal_length} power={power}")
            slot += 1
            sum += power
        
    return sum

