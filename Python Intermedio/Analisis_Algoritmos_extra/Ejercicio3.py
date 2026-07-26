#La función tiene dos ciclos for anidados que recorren todas las claves del diccionario.

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1} - {key2}")
#Complejidad temporal: O(n²)
#¿Por qué? Porque por cada clave del diccionario, 
# el segundo ciclo vuelve a recorrer todas las claves. 
# Si el diccionario tiene n claves, se realizan n × n = n² iteraciones.

#Complejidad temporal: O(n²), porque tiene dos ciclos anidados que recorren todas las claves 
# del diccionario.
#Con 1 millón de claves, ejecutaría aproximadamente 1 billón (10) 
# de iteraciones, por lo que su ejecución sería extremadamente lenta 
# y no sería una solución eficiente para un conjunto de datos tan grande.