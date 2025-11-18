# This is a simple calculator with functions for add, substruct, multiply and divide


# Function for addition
def add(a, b):
    return a + b


num1 = float(input("Enter the first number to be added: "))
num2 = float(input("Enter the second number to be added: "))

print(f"{num1} + {num2} = {add(num1, num2)}")


# Function for substruction
def substruct(a, b):
    return a - b


print(f"{num1} - {num2} = {substruct(num1, num2)}")


# Function for multiplication
def multiply(a, b):
    return a * b


print(f"{num1} * {num2} = {multiply(num1, num2)}")


# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by 0."
    return a / b


print(f"{num1} / {num2} = {divide(num1, num2)}")
