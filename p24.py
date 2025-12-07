def remove_tuples_of_length_k(tuple_list, k):
    return [tup for tup in tuple_list if len(tup) != k]
tuple_list = [(1, 2, 3), ('a', 'b'), (10, 20, 30), ('x', 'y', 'z'), ('apple', 'orange', 'banana')]
k = int(input("Enter the length k to remove tuples: "))
filtered_tuples = remove_tuples_of_length_k(tuple_list, k)
print(f"\nList of tuples after removing tuples of length {k}:")
print(filtered_tuples)
