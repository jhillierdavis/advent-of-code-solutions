class Node():

    def __init__(self, data:any):
        self.data = data
        self.children = [] # Use a list to maintain order

    def get_data(self):
        return self.data
    
    def add_child(self, child):
        # Validate
        if not type(child) is Node:
            raise ValueError(f"Invalid child of type: {type(child)}")

        # Add (if not already present)
        if child and child not in self.children:
            self.children.append(child)

    def get_children(self):
        # TODO: Clone / deep copy to prevent modification
        return self.children
    
