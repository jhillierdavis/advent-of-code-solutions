import pytest

import binary_tree_node    

def test_root_node():
    node = binary_tree_node.BinaryTreeNode(None)

    assert node.has_parent() == False
    assert node.is_root() == True
    assert node.get_depth() == 0
    

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
    left_child.get_depth() == 1

    right_child = binary_tree_node.BinaryTreeNode(9)
    root_node.set_right(right_child)
    root_node.has_children() == True
    right_child.has_parent() == True
    right_child.get_depth() == 1
    left_child.get_depth() == 1

    root_node.set_left(None)
    root_node.has_children() == True
    left_child.has_parent() == False

    root_node.set_right(None)
    root_node.has_children() == False
    right_child.has_parent() == False
    right_child.get_depth() == 0


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