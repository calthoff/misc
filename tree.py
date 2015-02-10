class Tree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.child = None

    def insert_child(self, new_node):
        self.child = Tree(new_node)