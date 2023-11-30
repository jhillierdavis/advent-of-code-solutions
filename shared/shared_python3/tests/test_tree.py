import pytest

from helpers import tree

def test_create_tree():
    node = tree.Node("Root")

    list = ["Alpha", "Beta", "Gamma"]
    for item in list:
        node.add_child(tree.Node(item))

    children = node.get_children()
    assert len(children) == 3
    for child_node in children:
        assert child_node.get_data() in list
        