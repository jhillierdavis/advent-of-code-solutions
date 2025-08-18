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

def add_and_reduce(snailfish_number_x, snailfish_number_y):
    # TODO
    return []

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
            result.append(split(e, modified))
    return result


"""
def calculate_eplosion(snailfish_number, depth):
    if depth == 4:
        return 0
    return snailfish_number

def generate_explosion(snailfish_number):
    #print(f"DEBUG: {snailfish_number}")
    left = snailfish_number[0]
    right = snailfish_number[1]
    if type(left) == list and type(right) == int:
        return [0, left[1] + right]
    if type(right) == list and type(left) == int:
        return [left + right[0], 0]
    raise Exception(f"Failed to explode unexpected snailfish_number={snailfish_number}")
    #return [] # Not expected!
    

def explode(snailfish_number, depth=0):
    result = []

    for e in snailfish_number:
        #print(f"DEBUG: e={e}, depth={depth}, result={result}")
        if type(e) == int:
            result.append(e)
        else:
            if depth < 3:
                result.append(explode(e, depth+1))
            else:
                #result.append(generate_explosion(e))
                result.append(0)
    return result
"""

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
    if parent.has_parent() and parent.left == current:
        # Avoid backtracking & keep accessing towards root 
        add_left(parent, parent.parent, value)
        return

    if False == parent.left.has_children():
        #print(f"DEBUG: Added parent.left.value={parent.left.value} value={value}")
        parent.left.value = parent.left.value + value


def get_leftmost_node(parent):
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
    #print(f"DEBUG: current.value={current.value} parent.value={parent.value} value={value}")
    if parent.has_parent() and parent.right == current:
        # Avoid backtracking & keep accessing towards root 
        add_right(parent, parent.parent, value)
        return
    
    elif parent.is_root() and current == parent.left:
        #print(f"DEBUG: TODO: Implement - find leftmost node!")
        current = get_leftmost_node(parent.right)
        if None != current:
            if False == current.has_children():
                print(f"DEBUG: Added current.value={current.value} value={value}")
                current.value = current.value + value
            else:
                add_right(current, current.parent, value)
            return
        

    if False == parent.right.has_children():
        #print(f"DEBUG: Added parent.right.value={parent.right.value} value={value}")
        parent.right.value = parent.right.value + value
    

def explode_leftmost_node(node, depth=0):
    if node.has_children():
        if depth > 3:
            #print(f"DEBUG: Exploding node: node.left.value={node.left.value} node.right.value={node.right.value}")
            node.value = 0
            add_left(node, node.parent, node.left.value)
            node.left = None
            add_right(node, node.parent, node.right.value)
            node.right = None
            return True
        else:            
            has_explosion = explode_leftmost_node(node.left, 1+depth)
            if has_explosion:
                return True
            return explode_leftmost_node(node.right, 1+depth)
    return False


def explode_leftmost_node(node, depth=0):
    if node.has_children():
        if depth > 3:
            #print(f"DEBUG: Exploding node: node.left.value={node.left.value} node.right.value={node.right.value}")
            node.value = 0
            add_left(node, node.parent, node.left.value)
            node.left = None
            add_right(node, node.parent, node.right.value)
            node.right = None
            return True
        else:            
            has_explosion = explode_leftmost_node(node.left, 1+depth)
            if has_explosion:
                return True
            return explode_leftmost_node(node.right, 1+depth)
    return False


def explode(snailfish_number):
    #result, left, right = find_and_explode(snailfish_number)

    #return result

    node = binary_tree_node.create_binary_tree_node_from_list(snailfish_number)
    explode_leftmost_node(node)
    return node.to_list()