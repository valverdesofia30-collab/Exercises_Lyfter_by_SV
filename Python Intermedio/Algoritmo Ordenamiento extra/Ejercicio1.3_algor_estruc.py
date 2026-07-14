# Se define la clase Node que representa un nodo del árbol.
class Node:

    # Atributo donde se almacena el dato.
    data: int

    # Referencia al hijo izquierdo.
    left: None

    # Referencia al hijo derecho.
    right: None

    # Constructor de la clase.
    def __init__(self, data, left=None, right=None):

        # Se guarda el dato.
        self.data = data

        # Se guarda la referencia al hijo izquierdo.
        self.left = left

        # Se guarda la referencia al hijo derecho.
        self.right = right


# Se define la clase BinaryTree.
class BinaryTree:

    # Constructor que recibe la raíz del árbol.
    def __init__(self, root):

        # Se guarda la raíz.
        self.root = root

    # Método para imprimir el árbol.
    def print_structure(self):

        # Se llama al método recursivo.
        self._print_node(self.root)

    # Método recursivo para recorrer el árbol.
    def _print_node(self, node):

        # Si el nodo no existe termina el recorrido.
        if node is None:
            return

        # Se imprime el dato del nodo.
        print(node.data)

        # Se recorre el subárbol izquierdo.
        self._print_node(node.left)

        # Se recorre el subárbol derecho.
        self._print_node(node.right)

    # Método para guardar los datos del árbol en una lista.
    def get_data_list(self):

        # Se crea una lista vacía.
        data_list = []

        # Se llena la lista recorriendo el árbol.
        self._collect_data(self.root, data_list)

        # Se devuelve la lista.
        return data_list

    # Método recursivo para recopilar los datos.
    def _collect_data(self, node, data_list):

        # Si el nodo no existe termina.
        if node is None:
            return

        # Se agrega el dato a la lista.
        data_list.append(node.data)

        # Se recorre el hijo izquierdo.
        self._collect_data(node.left, data_list)

        # Se recorre el hijo derecho.
        self._collect_data(node.right, data_list)

    # Método Bubble Sort.
    def bubble_sort(self):

        # Se obtiene la lista de datos.
        data = self.get_data_list()

        # Se obtiene la cantidad de elementos.
        n = len(data)

        # Primer ciclo del Bubble Sort.
        for i in range(n):

            # Segundo ciclo para comparar elementos.
            for j in range(0, n - i - 1):

                # Si el elemento actual es mayor que el siguiente.
                if data[j] > data[j + 1]:

                    # Se intercambian los elementos.
                    data[j], data[j + 1] = data[j + 1], data[j]

        # Se devuelve la lista ordenada.
        return data


# Se crean los nodos del árbol.
root = Node(25)

# Se crea el hijo izquierdo.
root.left = Node(2)

# Se crea el hijo derecho.
root.right = Node(35)

# Se crea el árbol.
tree = BinaryTree(root)

# Se imprime el árbol original.
print("Original Tree:")

# Se muestran los nodos.
tree.print_structure()

# Se imprime un mensaje.
print("\nSort data with Bubble Sort:")

# Se imprime la lista ordenada.
print(tree.bubble_sort())