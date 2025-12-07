def perform_calculation(num1, num2, operator):
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operator.")
    return result
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

num1_input = input("Enter the first number: ")
if not is_number(num1_input):
    print("Error: Please enter a valid number.")
else:
    num1 = float(num1_input)
    operator = input("Enter the operator (+, -, *, /): ")
    num2_input = input("Enter the second number: ")
    if not is_number(num2_input):
        print("Error: Please enter a valid number.")
    else:
        num2 = float(num2_input)
        result = perform_calculation(num1, num2, operator)
        if result is not None:
            print(f"\nThe result of {num1} {operator} {num2} is: {result}")
