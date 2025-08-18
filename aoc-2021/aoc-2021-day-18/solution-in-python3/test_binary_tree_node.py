import pytest

import binary_tree_node    

def test_root_node():
    node = binary_tree_node.BinaryTreeNode(None)

    assert node.has_parent() == False
    assert node.is_root() == True
    

def test_change_value():
    node = binary_tree_node.BinaryTreeNode(None)

    assert node.value == None

    node.value = 9
    assert node.value == 9


def test_has_children_and_has_parent():
    root_node = binary_tree_node.BinaryTreeNode(None)

    root_node.has_children() == False

    left_child = binary_tree_node.BinaryTreeNode(1)
    left_child.has_parent() == False

    root_node.set_left(left_child)
    root_node.has_children() == True
    left_child.has_parent() == True

    right_child = binary_tree_node.BinaryTreeNode(9)
    root_node.set_right(right_child)
    root_node.has_children() == True
    right_child.has_parent() == True

    root_node.set_left(None)
    root_node.has_children() == True
    left_child.has_parent() == False

    root_node.set_right(None)
    root_node.has_children() == False
    right_child.has_parent() == False


def test_shallow_to_list():
    root_node = binary_tree_node.BinaryTreeNode(None)

    assert root_node.to_list() == []

    left_child = binary_tree_node.BinaryTreeNode(1)
    root_node.set_left(left_child)
    right_child = binary_tree_node.BinaryTreeNode(9)
    root_node.set_right(right_child)
    assert root_node.to_list() == [1,9]

def test_deeper_to_list():
    node = binary_tree_node.BinaryTreeNode(None, binary_tree_node.BinaryTreeNode(9), binary_tree_node.BinaryTreeNode(8))
    assert node.to_list() == [9,8]

    node = binary_tree_node.BinaryTreeNode(None, node,  binary_tree_node.BinaryTreeNode(1))
    assert node.to_list() == [[9,8],1]


    node = binary_tree_node.BinaryTreeNode(None, node,  binary_tree_node.BinaryTreeNode(2))
    assert node.to_list() == [[[9,8],1],2]

    node = binary_tree_node.BinaryTreeNode(None, node,  binary_tree_node.BinaryTreeNode(3))
    assert node.to_list() == [[[[9,8],1],2],3]

    node = binary_tree_node.BinaryTreeNode(None, node,  binary_tree_node.BinaryTreeNode(4))
    assert node.to_list() == [[[[[9,8],1],2],3],4]

    #assert root_node.to_list() == [[[[[9,8],1],2],3],4]
    
    

def test_shallow_from_list():
    input_list = [9,8]
    node = binary_tree_node.create_binary_tree_node_from_list(input_list)

    assert node.to_list() == input_list

@pytest.mark.parametrize(
    "input_list",
    [
        pytest.param([[[[[9,8],1],2],3],4]),
        pytest.param([7,[6,[5,[4,[3,2]]]]]),
        pytest.param([[6,[5,[4,[3,2]]]],1]),
    ],    
)
def test_deeper_from_list(input_list):
    node = binary_tree_node.create_binary_tree_node_from_list(input_list)
    node.is_root() == True

    assert node.to_list() == input_list

"""
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



@pytest.mark.parametrize(
    "original, expected",
    [
        pytest.param([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),        
        pytest.param([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
        pytest.param([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
        pytest.param([1,[6,[5,[4,[3,2]]]]], [1,[6,[5,[7,0]]]]),
        pytest.param([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] , [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
        pytest.param([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],[[3,[2,[8,0]]],[9,[5,[7,0]]]]),     
        pytest.param([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]], [[[[0,7],4],[7,[[8,4],9]]],[1,1]]),
    ],    
)
def test_explode(original, expected):
    #print(f"DEBUG: original={original}")
    node = create_binary_tree_node_from_list(original)

    explode_leftmost_node(node)

    assert node.to_list() == expected
    
"""