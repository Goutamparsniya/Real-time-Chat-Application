input_string = input("Enter a string: ")
reverse_string = input_string[::-1]
index_of_difference = next((i for i, (a, b) in enumerate(zip(input_string, reverse_string)) if a != b), None)
if index_of_difference is not None:
    print(f"The strings differ at index {index_of_difference}.")
else:
    print("The strings are the same.")
