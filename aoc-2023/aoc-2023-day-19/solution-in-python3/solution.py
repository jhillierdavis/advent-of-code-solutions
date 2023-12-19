from collections import defaultdict, deque

from helpers import fileutils


def get_workflow_mappings_from(filename):
    workflow_mappings = {}

    workflow_lines = fileutils.get_lines_before_empty_from_file(filename)

    for wl in workflow_lines:
        
        name, instructions = wl.split('{')
        #print(f"DEBUG: name={name} instructions={instructions}")
        instruction_list = instructions[:-1].split(',')
        workflow_mappings[name] = instruction_list
    
    print(f"DEBUG: workflow_mappings={workflow_mappings}")
    return workflow_mappings

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

def add_state(queue, step, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max):
    queue.append((step, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max))


def solve_part2(filename):
    workflow_mappings = get_workflow_mappings_from(filename)

    # Determine the valid ranges for part categories (to then determine possible valid combinations)

    # Maintain a queue to process of workflow step and valid ranges of each category (for categories 'x','m','a','s')
    todo_queue = deque([('in',1,9999,1,9999,1,9999,1,9999)])

    combos = 0
    while todo_queue:
        step, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max = todo_queue.pop() 
        print(f"DEBUG: Process step={step} x_min={x_min} x_max={x_max} m_min={m_min} m_max={m_max} a_min={a_min} a_max={a_max} s_min={s_min} s_max={s_max}")

        if step == 'A':
            possibilities = (x_max - x_min) * (m_max - m_min) * (a_max - m_min) * (s_max - s_min)
            if possibilities > 0:
                combos += possibilities
        elif step == 'R':
            pass
        else:
            instructions = workflow_mappings[step]
            for ins in instructions:
                if '>' in ins:
                    w,d = ins.split(':')
                    category,value = w.split('>')
                    value = int(value)

                    if category == 'x':
                        if x_max > value:
                            add_state(todo_queue, d, value+1, x_max, m_min, m_max, a_min, a_max, s_min, s_max)
                        x_max = max(x_min, value)
                    if category == 'm':
                        if m_max > value:
                            add_state(todo_queue, d, x_min, x_max, value+1, m_max, a_min, a_max, s_min, s_max)
                        m_max = max(m_min, value)
                    if category == 'a':
                        if a_max > value:
                            add_state(todo_queue, d, x_min, x_max, m_min, m_max, value+1, x_max, s_min, s_max)
                        a_max = max(a_min, value)
                    if category == 's':
                        if s_max > value:
                            add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, a_max, value+1, s_max)   
                        s_max = max(s_min, value)                
                    
                elif '<' in ins:
                    w,d = ins.split(':')
                    category,value = w.split('<')
                    value = int(value)

                    if category == 'x':
                        if x_min < value:
                            add_state(todo_queue, d, x_min, value-1, m_min, m_max, a_min, a_max, s_min, s_max)
                        x_min = min(value, x_max)
                    if category == 'm':
                        if m_min < value-1:
                            add_state(todo_queue, d, x_min, x_max, m_min, value-1, a_min, a_max, s_min, s_max)
                        m_min = min(value, m_max)
                    if category == 'a':
                        if a_min < value-1:
                            add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, value-1, s_min, s_max)
                        a_min = min(value, a_max)
                    if category == 's':
                        if s_min < value-1:
                            add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, a_max, s_min, value-1)
                        s_min = min(value, s_max)  
                else:
                    add_state(todo_queue, ins, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max)
    return combos

