def get_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)  # Try converting to integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Ask for the first integer
num1 = get_integer("Enter the first integer: ")

# Ask for the second integer
num2 = get_integer("Enter the second integer: ")

# Calculate and print the sum
total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")
