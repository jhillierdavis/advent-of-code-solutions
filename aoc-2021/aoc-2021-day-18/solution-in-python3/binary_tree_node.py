class BinaryTreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.parent = None
        self.set_left(left)
        self.set_right(right)
        

    def set_left(self, child):
        # Validate
        if child is not None and (not type(child) is BinaryTreeNode):
            raise ValueError(f"Invalid child of type: {type(child)}")

        self.left = child
        if child:
            child.parent = self

    def set_right(self, child):
        # Validate
        if child is not None and (not type(child) is BinaryTreeNode):
            raise ValueError(f"Invalid child of type: {type(child)}")
        
        self.right = child
        if child:
            child.parent = self

    def has_parent(self):
        return self.parent != None
    
    def is_root(self):
        return False == self.has_parent()
    
    def has_children(self):
        return self.left != None or self.right != None
    
    def to_list(self):
        result = []
        if self.has_children():
            if self.left:
                if self.left.has_children():
                    result.append(self.left.to_list())
                else:
                    result.append(self.left.value)

            if self.right:
                if self.right.has_children():
                    result.append(self.right.to_list())
                else:
                    result.append(self.right.value)


        return result


def create_binary_tree_node_from_list(input_list:list):

    if len(input_list) > 2:
        raise Exception("Not a pair")
    
    left = input_list[0]
    right = input_list[1]

    if type(left) == int:
        left_node = BinaryTreeNode(left)
    elif type(left) == list:
        left_node = create_binary_tree_node_from_list(left)

    
    if type(right) == int:
        right_node = BinaryTreeNode(right)
    elif type(right) == list:
        right_node = create_binary_tree_node_from_list(right)

    return BinaryTreeNode(None, left_node,  right_node)
