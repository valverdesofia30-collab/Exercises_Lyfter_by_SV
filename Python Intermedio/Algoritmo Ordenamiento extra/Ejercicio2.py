class Node:

    # Atributo que almacena el dato del nodo.
    data: int

    # Atributo que apunta al siguiente nodo.
    next: "Node"

    # Constructor que recibe el dato y opcionalmente el siguiente nodo.
    def __init__(self, data, next=None):

        # Guarda el dato recibido.
        self.data = data

        # Guarda la referencia al siguiente nodo.
        self.next = next


# Se define la clase Stack.
class Stack:

    # Atributo que almacena el primer nodo.
    head: Node

    # Constructor que recibe el nodo inicial.
    def __init__(self, head):

        # Se asigna el primer nodo.
        self.head = head

    # Método para imprimir todos los elementos.
    def print_structure(self):

        # Se comienza desde el primer nodo.
        current_node = self.head

        # Se recorre la lista hasta llegar al final.
        while current_node is not None:

            # Se imprime el dato del nodo actual.
            print(current_node.data)

            # Se avanza al siguiente nodo.
            current_node = current_node.next

    # Método para agregar un nodo al final.
    def push(self, new_node):

        # Se comienza desde el primer nodo.
        current_node = self.head

        # Se avanza hasta encontrar el último nodo.
        while current_node.next is not None:

            # Se mueve al siguiente nodo.
            current_node = current_node.next

        # Se enlaza el nuevo nodo al final.
        current_node.next = new_node

    # Método para eliminar el último nodo.
    def pop(self):

        # Se verifica que la pila no esté vacía.
        if self.head:

            # Se comienza desde el primer nodo.
            current_node = self.head

            # Variable para guardar el nodo anterior.
            previous_node = None

            # Si solo existe un nodo.
            if self.head.next is None:

                # Se elimina el único nodo.
                self.head = None

                # Finaliza el método.
                return

            # Se recorre hasta el último nodo.
            while current_node.next is not None:

                # Se guarda el nodo anterior.
                previous_node = current_node

                # Se avanza al siguiente nodo.
                current_node = current_node.next

            # Se elimina el último nodo.
            previous_node.next = None

    # Método Bubble Sort para ordenar los datos.
    def bubble_sort(self):

        # Si la lista está vacía o tiene un solo elemento no hay nada que ordenar.
        if self.head is None or self.head.next is None:
            return

        # Variable que controla si hubo intercambios.
        swapped = True

        # Inicio de contador de pasadas que se van a realizar
        iterations = 0

        # Inicio contador de intercambios que se van a realizar
        exchanges = 0

        # Se repite mientras existan cambios.
        while swapped:

            # Iniciamos una nueva pasada por la función
            iterations += 1

            # Al inicio se supone que no habrá cambios.
            swapped = False


            # Se inicia desde el primer nodo.
            current = self.head


            # Se recorre hasta el penúltimo nodo.
            while current.next is not None:

                # Si el dato actual es mayor que el siguiente.
                if current.data > current.next.data:

                    # Se intercambian los datos.
                    current.data, current.next.data = current.next.data, current.data

                    exchanges += 1

                    # Se indica que hubo un intercambio.
                    swapped = True

                # Se avanza al siguiente nodo.
                current = current.next

        # Para que el programa me devuelva una salida y no de error, debo pedirle que me retorne la cantidad de iteraciones e intercambios realizadas
        return iterations, exchanges
    
        

# Se crea el primer nodo.
first_node = Node(35)

# Se crea la pila con el primer nodo.
my_stack = Stack(first_node)

# Se crea el segundo nodo.
second_node = Node(25)

# Se agrega a la pila.
my_stack.push(second_node)

# Se crea el tercer nodo.
third_node = Node(10)

# Se agrega a la pila.
my_stack.push(third_node)

# Se imprime la lista original.
print("Original list:")

# Se muestran los elementos.
my_stack.print_structure()

# Se ordenan los datos usando Bubble Sort.
iterations, exchanges = my_stack.bubble_sort()

# Se imprime un mensaje.
print("\nSort list:")

# Se muestran los elementos ordenados.
my_stack.print_structure()

# Aquí imprimimos las iteraciones y los intercambios
print("Iterations: ", iterations)
print("Exchanges: ", exchanges) 

# Se imprime un mensaje.
print("\nPOP")

# Se elimina el último nodo.
my_stack.pop()

# Se imprime la estructura.
my_stack.print_structure()

# Se imprime un mensaje.
print("\nPOP")

# Se elimina el último nodo.
my_stack.pop()

# Se imprime la estructura.
my_stack.print_structure()

# Se imprime un mensaje.
print("\nPOP")

# Se elimina el último nodo.
my_stack.pop()

# Se imprime la estructura.
my_stack.print_structure()