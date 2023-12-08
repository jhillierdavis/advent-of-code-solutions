from collections import defaultdict

from helpers import fileutils

def process_steps(node_map, instructions):
    current_node = "AAA"
    count = 0
    while current_node != "ZZZ":        
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
    print(f"DEBUG: instructions={instructions}")
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
        print(f"DEBUG: p={p} left={left} right={right}")

        if not root_node:
            root_node = p

        if not p in node_map.keys():
            node_map[p] = (left, right)  
    return node_map    

def solve(filename):
    instructions = get_instructions(filename)
    node_map = get_node_map(filename)
    count = process_steps(node_map, instructions)
    return count

