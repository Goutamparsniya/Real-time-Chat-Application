def remove_empty_lists(original_list):
    return [item for item in original_list if item]
my_list = [1, 2, [], 3, [], 4, [], 5, [], []]
filtered_list = remove_empty_lists(my_list)
print("Original List:", my_list)
print("List after removing empty lists:", filtered_list)
