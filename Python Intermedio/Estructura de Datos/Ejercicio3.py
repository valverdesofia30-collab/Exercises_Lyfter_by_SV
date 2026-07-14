class Node:
    data: str
    left: None
    right: None

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    
    def __init__(self, root):
        self.root= root
        
    def print_structure(self):
        self._print_node(self.root)
        
    def _print_node(self, node):
        if node is None:
            return
        
        print(node.data)
        
        self._print_node(node.left)
        self._print_node(node.right)