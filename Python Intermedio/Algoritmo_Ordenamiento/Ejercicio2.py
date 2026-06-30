#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).
def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):
        has_made_changes = False
        
#ciclo interno, encargado de recorrer la lista y realizar comparaciones
#el -1 en el len nos indica que iniciamos en el ultimo elemento
#outer_index = 0, inicia de derecha a izquierda      
        for index in range(len(list_to_sort) -1, outer_index, -1):
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index -1]
            
            print(f"-- Iteration {outer_index}, {index}. Previous element {previous_element}. Current element {current_element}")
            
#si el elemento anterior > que el elemento actual         
            if previous_element > current_element:
                print("The previous element is bigger than the current element.")
                list_to_sort[index] = previous_element
 #Aca se obtiene el elemento inmediatamente anterior, el que interesa comparar el elemento de la izquierda             
                list_to_sort[index -1] = current_element
                
                has_made_changes = True
                
        if not has_made_changes:
            return
                
my_test_list = [-5, 6, 10, 2, 1, 7, -8]
bubble_sort(my_test_list)

print(my_test_list)
            