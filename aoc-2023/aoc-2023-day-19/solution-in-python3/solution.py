from collections import defaultdict

from helpers import fileutils


def get_workflow_mappings_from(filename):
    workflow_mapping = {}

    workflow_lines = fileutils.get_lines_before_empty_from_file(filename)

    for wl in workflow_lines:
        
        name, instructions = wl.split('{')
        #print(f"DEBUG: name={name} instructions={instructions}")
        instruction_list = instructions[:-1].split(',')
        workflow_mapping[name] = instruction_list
    
    print(f"DEBUG: workflow_mapping={workflow_mapping}")
    return workflow_mapping

def get_part_mapping_from(part_input):
    part_mapping = defaultdict(int)

    s = part_input[1:-1] # Remove parenthesis
    ratings = s.split(',')
    for r in ratings:
        category, value = r.split("=")
        part_mapping[category] = int(value)

    print(f"DEBUG: part_mapping={part_mapping}")
    return part_mapping

def process_next_workflow_instruction(workflow_mapping, part_mapping, next):
    instructions = workflow_mapping[next]
    for ins in instructions:
        if '>' in ins:
            w,d = ins.split(':')
            category,value = w.split('>')
            value = int(value)
            if part_mapping[category] > value:
                next = d
                break                
        elif '<' in ins:
            w,d = ins.split(':')
            category,value = w.split('<')
            value = int(value)
            if part_mapping[category] < value:
                next = d
                break
        else:
            next = ins
            break
        
    #print(f"DEBUG: next={next}")
    return next


def workflow_processing_for_part(workflow_mappings, part_input):
    part_mapping = get_part_mapping_from(part_input)
    return workflow_processing_for_part_mapping(workflow_mappings, part_mapping)


def workflow_processing_for_part_mapping(workflow_mappings, part_mapping):
    next = 'in'
    while 'R' != next and 'A' != next:
        next = process_next_workflow_instruction(workflow_mappings, part_mapping, next)
    return next


def solve_part1(filename):
    workflow_mappings = get_workflow_mappings_from(filename)

    part_lines = fileutils.get_lines_after_empty_from_file(filename)

    sum = 0
    for pl in part_lines:
        x = 0; m = 0; a = 0; s = 0
        print(f"DEBUG: pl={pl}")
        part_mapping = get_part_mapping_from(pl)
        if 'A' == workflow_processing_for_part_mapping(workflow_mappings, part_mapping):
            x = part_mapping['x']
            m = part_mapping['m']
            a = part_mapping['a']
            s = part_mapping['s']
            subtotal = x + m + a + s
            print(f"DEBUG: subtotal={subtotal} x={x} m={m} a={a} s={s}")
            sum += subtotal

    return sum

def solve_part2(filename):
    lines = fileutils.get_file_lines(filename)
    return 0 # TODO

