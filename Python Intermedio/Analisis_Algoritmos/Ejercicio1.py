def bubble_sort(list_to_sort):          # O(1)

    for outer_index in range(0, len(list_to_sort) - 1):    # O(n)

        has_made_changes = False        # O(1)

        for index in range(0, len(list_to_sort) - 1 - outer_index):   # O(n)

            current_element = list_to_sort[index]          # O(1)
            next_element = list_to_sort[index + 1]         # O(1)

            print(f"-- Iteration {outer_index}, {index}. Actual Element: {current_element}, Next Element: {next_element}")   # O(1)

            if current_element > next_element:             # O(1)

                print("The current element is bigger than the next element")   # O(1)

                list_to_sort[index] = next_element         # O(1)
                list_to_sort[index + 1] = current_element  # O(1)

                has_made_changes = True                    # O(1)

    if not has_made_changes:                               # O(1)
        return                                             # O(1)

my_test_list = [1, 5, -6, 22, 8, -3]                       # O(1)

bubble_sort(my_test_list)                                 # Mejor: O(n)
                                                          # Promedio: O(n²)
                                                          # Peor: O(n²)

print(my_test_list)                                       # O(1)