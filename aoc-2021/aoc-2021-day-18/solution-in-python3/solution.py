import math

def get_magnitude(snailfish_number:list) -> int:   
    # obtain the calculated magnitude of a snailfish number 
    left = snailfish_number[0]
    right = snailfish_number[1]
    if type(left) == list:
        left = get_magnitude(left)
    if type(right) == list:
        right = get_magnitude(right)
    return (3 * left) + (2 * right)

def add(snailfish_number_x, snailfish_number_y):
    # add 2 snailfish numbers
    result = []
    result.append(snailfish_number_x)
    result.append(snailfish_number_y)
    return result

def reduce(snailfish_number):
    result = snailfish_number
    is_reduced = False
    step = 1

    while not is_reduced:
        was_exploded = True
        was_split = False

        while was_exploded:
            exploded = explode(result)
            if exploded != result:
                #print(f"DEBUG: reduce:  step={step} exploded={exploded}")
                result = exploded
            else:
                was_exploded = False
            
                    
        result, was_split = split(result)
        #if was_split:
        #    print(f"DEBUG: reduce: step={step} split={result}")

        if not was_exploded and not was_split:
            is_reduced = True
        step += 1

    return result


def add_and_reduce(snailfish_number_x, snailfish_number_y):
    result = add(snailfish_number_x, snailfish_number_y)
    #print(f"DEBUG: add_and_reduce: sum={result}")

    return reduce(result)

def split_number(number:int):
    if number > 9:
        half = number/2
        return [math.floor(half), math.ceil(half)]
    return number

def split(snailfish_number, modified=False):
    result = []
    for e in snailfish_number:
        if type(e) is int:
            if modified == True:
                result.append(e)
            else:
                a = split_number(e)        
                result.append(a)
                if a != e:
                    #print(f"DEBUG: Modification: e={e} a={a}")
                    modified = True
        elif type(e) is list:
            sub_result, modified = split(e, modified)
            result.append(sub_result)

    return result, modified


def find_and_explode(snailfish_number, depth=0):
    result = []
    left = 0
    right = 0

    for e in snailfish_number:
        #print(f"DEBUG: e={e}, depth={depth}, result={result}")
        if type(e) == int:
            if right > 0:
                result.append(e + right)
                right = 0
            else:
                result.append(e)
        else:
            if depth < 3:
                subresult, left, right = find_and_explode(e, depth+1)
                result.append(subresult)
            else:
                #result.append(generate_explosion(e))
                left = e[0]
                right = e[1]
                result.append(0)
    return result, left, right

import binary_tree_node

def add_left(current, parent, value):
    #print(f"DEBUG: add_left: current.value={current.value} parent.value={parent.value} value={value}")
    if parent.has_parent() and parent.left == current:
        # Avoid backtracking & keep accessing towards root 
        add_left(parent, parent.parent, value)
        return

    if False == parent.left.has_children():
        #print(f"DEBUG: Added parent.left.value={parent.left.value} value={value}")
        parent.left.value = parent.left.value + value


def get_leftmost_node(parent):
    #print(f"DEBUG: get_leftmost_node: parent={parent}")
    leftmost = parent.left
    current = leftmost
    while leftmost != None:
        #print(f"DEBUG: leftmost.value={leftmost.value}")
        leftmost = leftmost.left
        if leftmost != None:
            current = leftmost
    #print(f"DEBUG: current.value={current.value}")
    return current

def add_right(current, parent, value):
    #print(f"DEBUG: add_right: current.value={current.value} parent.value={parent.value} value={value}")
    if parent.has_parent() and parent.right == current:
        # Avoid backtracking & keep accessing towards root 
        add_right(parent, parent.parent, value)
        return
    
    elif parent.is_root() and current == parent.left:        
        current = get_leftmost_node(parent.right)
        if None != current:
            if False == current.has_children():
                #print(f"DEBUG: add_right: added current.value={current.value} value={value}")
                current.value = current.value + value
            else:
                add_right(current, current.parent, value)
            return
        

    if False == parent.right.has_children():
        #print(f"DEBUG: add_right: added parent.right.value={parent.right.value} value={value}")
        current = get_leftmost_node(parent.right)
        if current:
            if current.is_parent():
                current.left.value = current.left.value + value
            else:
                current.value = current.value + value
    

def is_explodable_pair_node(node):
    if node.get_depth() > 3 and not node.left.has_children() and not node.right.has_children():
        return True
    return False

def get_next_left_branching_parent_node(parent):
    if not parent:
        return None    
    return parent.left

def get_rightmost_leaf_node(node):
    if node.is_leaf():
        return node    
    return get_rightmost_leaf_node(node.right)

def add_towards_left(node, parent, value):
    target_node = get_next_left_branching_parent_node(parent)
    if None == target_node:
        return

    if target_node != node:
        target_node = get_rightmost_leaf_node(target_node)
        target_node.value += value
    else:
        add_towards_left(parent, parent.parent, value)


def get_next_right_branching_parent_node(parent):
    if not parent:
        return None    
    return parent.right

def get_leftmost_leaf_node(node):
    if node.is_leaf():
        return node    
    return get_leftmost_leaf_node(node.left)

def add_towards_right(node, parent, value):
    #print(f"DEBUG: add_towards_right: node={node} parent={parent} value={value}")
    target_node = get_next_right_branching_parent_node(parent)
    #print(f"DEBUG: add_towards_right: target_node={target_node}")
    if not target_node:
        return
    
    if target_node != node:
        target_node = get_leftmost_leaf_node(target_node)
        target_node.value += value
    else:
        add_towards_right(parent, parent.parent, value)

def explode_leftmost_node(node):
    if not node.has_children():
        return False
    
    if is_explodable_pair_node(node):
        left_value = node.left.value
        right_value = node.right.value

        node.value = 0
        node.left = None
        node.right = None

        #print(f"DEBUG: Exploded node: {node} left_value={left_value} right_value={right_value}")
        add_towards_left(node, node.parent, left_value)
        add_towards_right(node, node.parent, right_value)

        return True
    else:            
        has_explosion = explode_leftmost_node(node.left)
        if has_explosion:
            return True
        return explode_leftmost_node(node.right)
    return False


def explode(snailfish_number):
    node = binary_tree_node.create_binary_tree_node_from_list(snailfish_number)
    explode_leftmost_node(node)
    return node.to_list()

import ast
from helpers import fileutils

def solve_part1(filename):
    lines = fileutils.get_file_lines_from(filename)
    result = None

    for l in lines:
        sfnum = ast.literal_eval(l)
        if None == sfnum:
            continue
        if result:            
            output = add_and_reduce(result, sfnum)
            #print(f"DEBUG: Adding: {result} + {sfnum} = {output}")
            result = output
        else:
            result = sfnum

    return result


def solve_part2(filename):
    lines = fileutils.get_file_lines_from(filename)

    snailfish_numbers = []
    for l in lines:
        sfnum = ast.literal_eval(l)
        if sfnum:
            snailfish_numbers.append(sfnum)

    max_result = None
    max_magnitude = 0
    for x in snailfish_numbers:
        for y in snailfish_numbers:
            if x == y:
                continue

            result = add_and_reduce(x, y)
            magnitude = get_magnitude(result)
            if magnitude > max_magnitude:
                max_magnitude = magnitude
                max_result = result

    return max_result, max_magnitude