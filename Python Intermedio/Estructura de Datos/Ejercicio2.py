class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class DoubleEndedQueue:
    head: Node
    
    def __init__(self, head):
        self.head = head
        
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
    def push_left(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def push_right(self, data):
        new_node = Node(data)
        current_node = self.head
        
        if self.head is None:
            self.head = new_node
            return
        
        while current_node.next is not None:
            current_node = current_node.next 
        current_node.next = new_node
        
    def pop_left(self):
        if self.head:
            self.head = self.head.next
            
    def pop_right(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        
        while current_node.next.next is not None:
            current_node = current_node.next
            
        current_node.next = None

first_node = Node("I am the first Node")
my_double_ended_queue = DoubleEndedQueue(first_node)

my_double_ended_queue.push_left("I am the second Node")
my_double_ended_queue.push_right("I am the third Node")

my_double_ended_queue.print_structure()

print("POP LEFT")
my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure

print("POP RIGHT")
my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()
            