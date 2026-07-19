class Node:
    
    data: int
    
    next: "Node"
    
    def __init__ (self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    
    def __init__(self, head):
        self.head = head
        
    def validate_bubble_sort(self):
        if self.head is None:
            
            raise ValueError ("The list is empty")
        
        current_node = self.head
        
        while current_node is not None:
            
            if not isinstance(current_node.data, (int, float)):
                raise ValueError ("The data is not a number") 
            current_node = current_node.next
        self.bubble_sort()
          
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

#Saber si la lista esta vacia          
    def bubble_sort(self):
        if self.head is None or self.head.next is None:
            return

#Le indica al programa si va a haber intercambios       
        swapped = True

#Se repiten mientras hayan intercambios   
        while swapped:

#El programa aun no tiene intercambios, esta empezando       
            swapped = False
        
            current = self.head
            
            while current.next is not None:
                
                if current.data > current.next.data:
                    #Intercambio
                    current.data, current.next.data = current.next.data, current.data
                    
                    swapped = True
                    
                current = current.next
                
first_node = Node(50)
second_node = Node(1)
third_node = Node(25)
    
first_node.next = second_node
second_node.next = third_node

my_queue = Queue(first_node)

my_queue.validate_bubble_sort()

my_queue.print_structure()