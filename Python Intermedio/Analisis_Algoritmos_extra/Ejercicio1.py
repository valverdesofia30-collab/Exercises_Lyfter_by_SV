#Primer código
def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

#Complejidad temporal: O(n)
#¿Por qué? Porque el ciclo for recorre todos los números desde 1 hasta n
# realizando una suma en cada iteración. 
# Si n aumenta, el número de operaciones también aumenta de forma proporcional

#Segundo código
def add_formula(n):
    return n * (n + 1) // 2

#Complejidad temporal: O(1)
#¿Por qué? Porque siempre realiza la misma cantidad de operaciones matemáticas 
#(una suma, una multiplicación y una división), sin importar el valor de n.

#manual_add(n) → O(n) porque recorre todos los números del 1 al n.
#add_formula(n) → O(1) porque siempre realiza un número constante de operaciones.
#Para n = 1 000 000 000, elegiría add_formula, 
# ya que es mucho más eficiente y calcula el resultado de manera inmediata sin necesidad de recorrer 
#todos los números.