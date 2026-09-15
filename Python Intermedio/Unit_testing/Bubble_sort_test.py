def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):

        has_made_changes = False
        
        for index in range(0, len(list_to_sort) -1 -outer_index):
            
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
            

            print(f"-- Iteration {outer_index}, {index}. Actual Element: {current_element}, Next Element: {next_element}")
        

            if current_element > next_element:
                print("The current element is bigger than the next element")
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True


        if not has_made_changes:
            return
     
my_test_list = [1, 5, -6, 22, 8, -3]
bubble_sort(my_test_list)

print(my_test_list)