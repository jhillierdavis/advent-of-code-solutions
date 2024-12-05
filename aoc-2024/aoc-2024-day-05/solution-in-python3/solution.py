from helpers import fileutils
from collections import deque


def get_middle_value(int_array):
    middle = int(len(int_array)/2)
    return int_array[middle]

def is_valid_ordering(list_int, orderings):
    length = len(list_int)
    for i in range(length):
        current = list_int[i]
        for j in range((i+1),length):
            next = list_int[j]
            items = orderings.get(next)
            #print(f"DEBUG: current={current} next={next} items={items}")
            if items == None:
                continue
            if current in items:
                return False
    return True

def get_page_orderings_before_from(lines):
    orderings = dict()

    for l in lines:
        values = l.split('|')
        key = int(values[0])
        item = int(values[1])
        items = orderings.get(key)
        if None == items:
            items = []
        items.append(item)
        orderings.update({key: items})  

    return orderings

def get_page_orderings_after_from(lines):
    page_orderings_afer = dict()

    for l in lines:
        values = l.split('|')
        item = int(values[0])
        key = int(values[1])
        items = page_orderings_afer.get(key)
        if None == items:
            items = []
        items.append(item)
        page_orderings_afer.update({key: items})  

    return page_orderings_afer


def solve_part1(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    #print(f"DEBUG: Ordering lines={lines}")

    orderings = get_page_orderings_before_from(lines)
    #print(f"DEBUG: Orderings={orderings}")

    lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: Updates={lines}")

    count = 0
    for l in lines:
        values = l.split(',')
        list_int = []
        for v in values:
            entry = int(v)
            list_int.append(entry)
        #print(f"DEBUG: list_int={list_int}")   
        if is_valid_ordering(list_int, orderings):
             print(f"DEBUG: Valid list_int={list_int}")   
             count += get_middle_value(list_int)

    return count

def reorder_invalid_list(list_int, page_orderings_before, page_orderings_after):
    queue = deque(list_int)
    #print(f"DEBUG: queue={queue}")
    new_list = []

    while len(queue) > 0:
        item = queue.popleft()
        priority = True
        for other in queue:
            #print(f"DEBUG: item={item} other={other}")
            after = page_orderings_after.get(other)
            if after is not None and item in after:
                priority = False
                break
        if priority:
            new_list.append(item)
        else:
            queue.append(item)

    return new_list
        

def solve_part2(filename):
    lines = fileutils.get_lines_before_empty_from_file(filename)
    #print(f"DEBUG: Ordering lines={lines}")

    page_orderings_before = get_page_orderings_before_from(lines)
    page_orderings_after = get_page_orderings_after_from(lines)
    #print(f"DEBUG: Orderings={orderings}")

    lines = fileutils.get_lines_after_empty_from_file(filename)
    #print(f"DEBUG: Updates={lines}")

    count = 0
    for l in lines:
        values = l.split(',')
        list_int = []
        for v in values:
            entry = int(v)
            list_int.append(entry)
        #print(f"DEBUG: list_int={list_int}")   
        if not is_valid_ordering(list_int, page_orderings_before):
            #print(f"DEBUG: Invalid list_int={list_int}")   

            new_list = reorder_invalid_list(list_int, page_orderings_before, page_orderings_after)
            #print(f"DEBUG: Reordered new_list={new_list}")   
            count += get_middle_value(new_list)

    return count