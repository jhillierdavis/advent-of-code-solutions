from collections import defaultdict
import math, re

from helpers import fileutils


def get_number_of_steps_from_start_to_finish(start, target_ending, node_map, instructions):
    # Obtain the number of steps from start to finish, repeating instructions if necesssary

    current_node = start
    count = 0
    while not current_node.endswith(target_ending):        
        step = instructions[count % len(instructions)] # Repeat
        if step == 'L': # Left
            current_node = node_map[current_node][0]
        elif step == 'R': # Right
            current_node = node_map[current_node][1]
        else:
            raise Exception(f"Unexpected unknown instruction step={step}!") # Not left or right
        count += 1
    return count


def get_instructions(filename):
    # Obtain the sequence of 'L' (left) or 'R' (right) instructions

    instruction_lines = fileutils.get_lines_before_empty_from_file(filename)
    instructions = instruction_lines[0]
    #print(f"DEBUG: instructions={instructions}")
    return instructions

def get_node_map(filename):  
    # Obtain the mapping of source node to left and right (tuple) destination nodes  

    lines = fileutils.get_lines_after_empty_from_file(filename)

    regexp_pattern = r'(...) = \((...), (...)\)'

    node_map = {}
    for l in lines:
        parent, left, right = re.search(regexp_pattern, l).groups(0)
        node_map[parent] = (left, right)  
    return node_map    


def solve_part1(filename):
    instructions = get_instructions(filename)
    node_map = get_node_map(filename)
    count = get_number_of_steps_from_start_to_finish('AAA', 'ZZZ', node_map, instructions)
    return count


def get_start_nodes(node_map):
    # Obtain the starting nodes (ending with 'A')

    start_nodes = []
    for k in node_map.keys():
        if k[-1] == 'A': # Last char match
            start_nodes.append(k)

    #print(f"DEBUG: start_nodes={start_nodes}")
    assert len(start_nodes) > 0            
    return start_nodes


def solve_part2(filename):
    instructions = get_instructions(filename)
    node_map = get_node_map(filename)

    start_nodes = get_start_nodes(node_map)

    map_start_to_finish_step_count = {}
    for start in start_nodes:
        count = get_number_of_steps_from_start_to_finish(start, 'Z', node_map, instructions)
        map_start_to_finish_step_count[start] = count

    #print(f"DEBUG: map_start_to_step_count={map_start_to_finish_step_count}")

    # Get LCM (Lowest Common Multiple) of all step counts (in the list of all start to finish paths)
    return math.lcm(*map_start_to_finish_step_count.values()) 