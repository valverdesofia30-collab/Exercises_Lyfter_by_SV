def bubble_sort(list_to_sort):
#Repetir la iteración de la lista por todos los elementos para moverse al final
    for outer_index in range(0, len(list_to_sort) -1):

#Usamos esta variable para revisar si hemos movido elementos
        has_made_changes = False
        
#Iterar la lista, para el indice en el rango 0, recorra la lista que se va a ordenar
#Se le resta 1 al len para que llegue hasta el penultimo elemento compare y no siga buscando más 
#Porque el ultimo ya va a ser el mayor
#Usamos el indice exterior para restar los elementos que ya estan ordenados al final
        for index in range(0, len(list_to_sort) -1 -outer_index):
            
#Guardamos los valores del elemento actual y el siguiente, al siguiente se le suma 1 y los dos guardan en el indice
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
            
#Se imprime el indice, el elemento actual y el siguiente
            print(f"-- Iteration {outer_index}, {index}. Actual Element: {current_element}, Next Element: {next_element}")
        
#Si el actual es mayor al siguiente, intercambiamos sus posiciones
            if current_element > next_element:
                print("The current element is bigger than the next element")
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True

#Si no hemos movido elementos, la lista ya esta ordenada
    if not has_made_changes:
        return
            
#test de prueba para que ordene los números        
my_test_list = [1, 5, -6, 22, 8, -3]
bubble_sort(my_test_list)

print(my_test_list)