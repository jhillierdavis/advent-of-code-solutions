from collections import defaultdict
import math

from helpers import fileutils

def process_steps(start, target_ending, node_map, instructions):
    current_node = start
    count = 0
    while not current_node.endswith(target_ending):        
        step = instructions[count % len(instructions)]
        if step == "L":
            current_node = node_map[current_node][0]
        elif step == 'R':
            current_node = node_map[current_node][1]
        else:
            raise Exception(f"Unknown step={step}!")
        count += 1
    return count

def get_instructions(filename):
    instruction_lines = fileutils.get_lines_before_empty_from_file(filename)
    instructions = instruction_lines[0]
    #print(f"DEBUG: instructions={instructions}")
    return instructions

def get_node_map(filename):
    node_map = {}
    lines = fileutils.get_lines_after_empty_from_file(filename)
    root_node = None
    for l in lines:
        (p,c) = l.split("=")
        p = p.replace(' ', '') 
        c = c.replace(" ", "")
        c = c.replace("(", "")
        c = c.replace(")", "")
        (left,right) = c.split(",")
        left = left.replace(" ", "")
        right = right.replace(" ", "")
        #print(f"DEBUG: p={p} left={left} right={right}")

        if not root_node:
            root_node = p

        if not p in node_map.keys():
            node_map[p] = (left, right)  
    return node_map    

def solve_part1(filename):
    instructions = get_instructions(filename)
    node_map = get_node_map(filename)
    count = process_steps('AAA', 'ZZZ', node_map, instructions)
    return count

def get_start_nodes(node_map):
    # Obtain the starting nodes (ending with 'A')

    start_nodes = []
    for k in node_map.keys():
        if k[-1] == 'A':
            start_nodes.append(k)

    #print(f"DEBUG: start_nodes={start_nodes}")
    assert len(start_nodes) > 0            
    return start_nodes

def solve_part2(filename):
    instructions = get_instructions(filename)
    node_map = get_node_map(filename)

    start_nodes = get_start_nodes(node_map)

    map_start_to_finish = {}
    for start in start_nodes:
        count = process_steps(start, 'Z', node_map, instructions)
        map_start_to_finish[start] = count

    #print(f"DEBUG: map_start_to_finish={map_start_to_finish}")
    return math.lcm(*map_start_to_finish.values()) # Get lowest common multiple of all step counts