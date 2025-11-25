# This program asks for two numbers and print their sum, differences, product and quotient
#
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} x {num2} = {num1 * num2}")
        print(f"{num1} / {num2} = {num1 / num2}")
        break

    except ValueError:
        print("Invalid number! Please input a valid number.")
