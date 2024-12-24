from collections import deque

from helpers import fileutils

def get_wire_value_map(filename):
    wire_value_map = dict()
    lines = fileutils.get_lines_before_empty_from_file(filename)    
    for l in lines:
        wire, initial = l.split(': ')
        wire_value_map[wire] = int(initial)
    return wire_value_map


def get_zwire_result(wire_value_map):
    binary_ans = ''
    for i in range(1000):
        zwire = 'z' + str(i).zfill(2)
        if zwire not in wire_value_map:
            break 
        binary_ans = str(wire_value_map[zwire]) + binary_ans

    return int(binary_ans, 2)


def process_wire_signals(wire_value_map, wire_left, operation, wire_right, wire_result):
    if 'AND' == operation:
        wire_value_map[wire_result] = wire_value_map[wire_left] & wire_value_map[wire_right]
    elif 'XOR' == operation:
        wire_value_map[wire_result] = wire_value_map[wire_left] ^ wire_value_map[wire_right]
    elif 'OR' == operation:
        wire_value_map[wire_result] = wire_value_map[wire_left] | wire_value_map[wire_right]
    else:
        raise Exception(f'Unknown operation: {operation}')


def solve_part1(filename):
    #lines = fileutils.get_file_lines_from(filename)

    wire_value_map = get_wire_value_map(filename)
    #print(f"DEBUG: wire_value_map={wire_value_map}")

    queue = deque()
    lines = fileutils.get_lines_after_empty_from_file(filename)
    for l in lines:
        values = l.split(' ')
        wire_left = values[0]
        operation = values[1]
        wire_right = values[2]
        wire_result = values[4]

        #print(f"DEBUG: {wire_left} {operation} {wire_right} {wire_result}")

        entry = (wire_left, operation, wire_right, wire_result)
        queue.append(entry)


    while queue:
        entry = queue.pop()
        wire_left, operation, wire_right, wire_result = entry
        if wire_left not in wire_value_map or wire_right not in wire_value_map:
            queue.appendleft(entry)
        else:
            process_wire_signals(wire_value_map, wire_left, operation, wire_right, wire_result)
    
    #print(f"DEBUG: wire_value_map={wire_value_map}")

    return get_zwire_result(wire_value_map)

def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)
    return -1