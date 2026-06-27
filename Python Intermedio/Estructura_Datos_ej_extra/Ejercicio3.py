# Clase que representa un nodo de una lista doblemente enlazada
class Node:
    def __init__(self, data):
        self.data = data      # Guarda el valor del nodo
        self.next = None      # Apunta al siguiente nodo
        self.prev = None      # Apunta al nodo anterior


# Clase que representa la lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Primer nodo de la lista
        self.tail = None      # Último nodo de la lista

    # Método para agregar un nodo al final
    def append(self, data):

        # Crea un nuevo nodo con el dato recibido
        new_node = Node(data)

        # Si la lista está vacía
        if self.head is None:
            self.head = new_node   # El nuevo nodo será el primero
            self.tail = new_node   # Y también será el último
        else:
            # El último nodo actual apunta al nuevo nodo
            self.tail.next = new_node

            # El nuevo nodo apunta al último nodo actual
            new_node.prev = self.tail

            # El nuevo nodo pasa a ser el último
            self.tail = new_node

    # Método para agregar un nodo al inicio
    def prepend(self, data):

        # Crea un nuevo nodo con el dato recibido
        new_node = Node(data)

        # Si la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # El nuevo nodo apunta al primer nodo actual
            new_node.next = self.head

            # El primer nodo actual apunta hacia atrás al nuevo nodo
            self.head.prev = new_node

            # El nuevo nodo pasa a ser el primero
            self.head = new_node

    # Método para eliminar el primer nodo con el valor indicado
    def delete(self, data):

        # Empieza a recorrer desde el primer nodo
        current = self.head

        # Busca el nodo con el dato deseado
        while current is not None and current.data != data:
            current = current.next

        # Si no se encontró el dato, termina el método
        if current is None:
            return

        # Si el nodo a eliminar es el primero
        if current == self.head:
            self.head = current.next

            # Si existe un nuevo primer nodo, elimina su referencia anterior
            if self.head is not None:
                self.head.prev = None

        # Si el nodo a eliminar no es el primero
        else:
            # El nodo anterior saltará al siguiente nodo
            current.prev.next = current.next

        # Si el nodo a eliminar es el último
        if current == self.tail:
            self.tail = current.prev

            # Si existe un nuevo último nodo, elimina su referencia siguiente
            if self.tail is not None:
                self.tail.next = None

        # Si el nodo a eliminar no es el último
        else:
            # El nodo siguiente apuntará al nodo anterior
            current.next.prev = current.prev

    # Método para imprimir desde el inicio hacia el final
    def print_forward(self):

        # Comienza desde el primer nodo
        current = self.head

        # Recorre todos los nodos
        while current is not None:

            # Imprime el dato actual
            print(current.data, end="")

            # Si hay otro nodo después, imprime una flecha
            if current.next is not None:
                print(" -> ", end="")

            # Avanza al siguiente nodo
            current = current.next

        # Salto de línea al finalizar
        print()

    # Método para imprimir desde el final hacia el inicio
    def print_backward(self):

        # Comienza desde el último nodo
        current = self.tail

        # Recorre todos los nodos hacia atrás
        while current is not None:

            # Imprime el dato actual
            print(current.data, end="")

            # Si hay un nodo anterior, imprime una flecha
            if current.prev is not None:
                print(" -> ", end="")

            # Retrocede al nodo anterior
            current = current.prev

        # Salto de línea al finalizar
        print()