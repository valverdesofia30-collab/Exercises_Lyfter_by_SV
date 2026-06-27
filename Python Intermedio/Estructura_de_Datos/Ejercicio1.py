class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Stack:
    head: Node
    
    def __init__(self, head):
        self.head = head
        
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
    def push(self, new_node):
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        
    def pop(self):
        if self.head:
            current_node = self.head
            previous_node = None
            
            if self.head.next is None:
                self.head = None
                return
        
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            
            previous_node.next = None
            
first_node = Node("I am the first Node")
my_stack = Stack(first_node)

second_node = Node("I am the second Node")
my_stack.push(second_node)

third_node = Node("I am the third Node")
my_stack.push(third_node)

my_stack.print_structure()

print("POP")

my_stack.pop()
my_stack.print_structure()

print("POP")

my_stack.pop()
my_stack.print_structure()

print("POP")

my_stack.pop()
my_stack.print_structure()
