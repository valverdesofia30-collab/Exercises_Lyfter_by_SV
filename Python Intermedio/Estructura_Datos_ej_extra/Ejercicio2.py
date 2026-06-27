# Clase que representa un nodo de la lista enlazada
class Node:
    def __init__(self, data):
        self.data = data      # Guarda el valor del nodo
        self.next = None      # Apunta al siguiente nodo (al inicio no apunta a ninguno)


# Clase que representa la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None      # Guarda el primer nodo de la lista

    # Método para insertar un nodo al inicio
    def insert_front(self, data):

        # Crea un nuevo nodo con el dato recibido
        new_node = Node(data)

        # El nuevo nodo apuntará al que actualmente es el primero
        new_node.next = self.head

        # El nuevo nodo pasa a ser el primer nodo de la lista
        self.head = new_node

    # Método para insertar un nodo al final
    def insert_back(self, data):

        # Crea un nuevo nodo con el dato recibido
        new_node = Node(data)

        # Si la lista está vacía, el nuevo nodo será el primero
        if self.head is None:
            self.head = new_node
            return

        # Empieza a recorrer desde el primer nodo
        current = self.head

        # Avanza hasta encontrar el último nodo
        while current.next is not None:
            current = current.next

        # El último nodo apuntará al nuevo nodo
        current.next = new_node

    # Método para eliminar el primer nodo con el valor indicado
    def delete(self, data):

        # Si la lista está vacía, no hay nada que eliminar
        if self.head is None:
            return

        # Si el primer nodo contiene el dato buscado
        if self.head.data == data:

            # El segundo nodo pasa a ser el primero
            self.head = self.head.next
            return

        # Comienza a recorrer desde el primer nodo
        current = self.head

        # Busca el nodo anterior al que contiene el dato
        while current.next is not None and current.next.data != data:
            current = current.next

        # Si se encontró el dato, se elimina saltando ese nodo
        if current.next is not None:
            current.next = current.next.next

    # Método para imprimir todos los elementos de la lista
    def print_all(self):

        # Comienza desde el primer nodo
        current = self.head

        # Recorre todos los nodos de la lista
        while current is not None:

            # Imprime el dato del nodo actual
            print(current.data, end="")

            # Si hay otro nodo después, imprime una flecha
            if current.next is not None:
                print(" -> ", end="")

            # Avanza al siguiente nodo
            current = current.next

        # Salto de línea al finalizar
        print()