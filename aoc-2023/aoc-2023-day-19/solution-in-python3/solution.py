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
    rating_min:int = 1
    rating_max:int = 4000
    todo_queue = deque([('in',rating_min,rating_max,rating_min,rating_max,rating_min,rating_max,rating_min,rating_max)])

    combos = 0
    while todo_queue:
        step, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max = todo_queue.pop() 
        #print(f"DEBUG: Process step={step} x_min={x_min} x_max={x_max} m_min={m_min} m_max={m_max} a_min={a_min} a_max={a_max} s_min={s_min} s_max={s_max}")

        if step == 'A':            
            possibilities = (1 + x_max - x_min) * (1 + m_max - m_min) * (1 + a_max - a_min) * (1 + s_max - s_min)
            print(f"DEBUG: At step={step} x_min={x_min} x_max={x_max} m_min={m_min} m_max={m_max} a_min={a_min} a_max={a_max} s_min={s_min} s_max={s_max} possibilies={possibilities}")
            assert possibilities > 0, f"possiblities={possibilities}"
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

                    # e.g. x > 1000 -> True: (1001, 4000) & False: (1,1000)

                    if category == 'x':
                        add_state(todo_queue, d, max(value+1, x_min), x_max, m_min, m_max, a_min, a_max, s_min, s_max)
                        x_max = min(x_max, value)
                        #x_max = value
                    if category == 'm':                        
                        add_state(todo_queue, d, x_min, x_max, max(value+1, m_min), m_max, a_min, a_max, s_min, s_max)
                        m_max = min(m_max, value)
                        #m_max = value
                    if category == 'a':
                        add_state(todo_queue, d, x_min, x_max, m_min, m_max, max(value+1, a_min), a_max, s_min, s_max)
                        a_max = min(a_max, value)
                        #a_max = value
                    if category == 's':
                        add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, a_max, max(value+1, s_min), s_max)   
                        s_max = min(s_max, value)                
                        #s_max = value
                    
                elif '<' in ins:
                    w,d = ins.split(':')
                    category,value = w.split('<')
                    value = int(value)

                    # e.g. x < 1000 -> True: (1, 9999) & False: (1000,4000)

                    if category == 'x':
                        add_state(todo_queue, d, x_min, min(value-1, x_max), m_min, m_max, a_min, a_max, s_min, s_max)
                        #x_min = min(value, x_max)
                        x_min = max(value, x_min)
                    if category == 'm':
                        add_state(todo_queue, d, x_min, x_max, m_min, min(value-1, m_max), a_min, a_max, s_min, s_max)
                        #m_min = min(value, m_max)
                        m_min = max(value, m_min)
                    if category == 'a':
                        add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, min(value-1, a_max), s_min, s_max)
                        #a_min = min(value, a_max)
                        a_min = max(value, a_min)
                    if category == 's':
                        add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, a_max, s_min, min(value-1, s_max))
                        #s_min = min(value, s_max)  
                        s_min = max(value, s_min)
                else:
                    d = ins
                    add_state(todo_queue, d, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max)
    return combos

