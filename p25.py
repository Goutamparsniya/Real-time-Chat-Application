def convert_to_positions(input_string):
    result = ""

    for char in input_string:
        if char.isalpha():
            position = ord(char.lower()) - ord('a') + 1
            result += str(position) + ' '
        else:
            result += char
            return result.strip()

input_string = input("Enter a string: ")
result_string = convert_to_positions(input_string)
print(f"\nThe string with letters converted to their respective positions: {result_string}")
