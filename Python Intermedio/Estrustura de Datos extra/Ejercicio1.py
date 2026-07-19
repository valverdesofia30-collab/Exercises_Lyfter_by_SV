# Clase que representa un nodo de la cola
class Node:
    def __init__(self, data):
        self.data = data      # Guarda el valor del nodo
        self.next = None      # Apunta al siguiente nodo (al inicio no hay ninguno)


# Clase que representa la cola (Queue)
class Queue:
    def __init__(self):
        self.front = None     # Guarda el primer nodo de la cola
        self.rear = None      # Guarda el último nodo de la cola

    # Método para agregar un elemento al final de la cola
    def enqueue(self, data):
        new_node = Node(data)     # Crea un nuevo nodo con el dato recibido

        # Verifica si la cola está vacía
        if self.front is None:
            self.front = new_node # El nuevo nodo será el primero
            self.rear = new_node  # Y también será el último
        else:
            self.rear.next = new_node # El último nodo apunta al nuevo nodo
            self.rear = new_node      # El nuevo nodo pasa a ser el último

    # Método para eliminar y devolver el primer elemento de la cola
    def dequeue(self):

        # Si la cola está vacía, no hay nada que eliminar
        if self.front is None:
            return None

        # Guarda el dato del primer nodo para devolverlo después
        data = self.front.data

        # Mueve el inicio de la cola al siguiente nodo
        self.front = self.front.next

        # Si después de eliminar quedó vacía, rear también debe quedar en None
        if self.front is None:
            self.rear = None

        # Devuelve el dato eliminado
        return data

    # Método para imprimir todos los elementos de la cola en orden
    def print_all(self):

        # Comienza desde el primer nodo
        current = self.front

        # Recorre la cola mientras existan nodos
        while current is not None:

            # Imprime el dato del nodo actual
            print(current.data, end="")

            # Si existe un siguiente nodo, imprime una flecha
            if current.next is not None:
                print(" -> ", end="")

            # Avanza al siguiente nodo
            current = current.next

        # Salto de línea al terminar de imprimir
        print()