# Get input from the user
num1 = float(input("Enter the first number: "))
op = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the user's input
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    # Check for division by zero
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation."

# Print the result
print(f"\nResult: {num1} {op} {num2} = {result}")

