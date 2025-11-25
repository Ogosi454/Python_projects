while True:
    try:
        num1 = int(input("Enter an integer number: "))
        num2 = int(input("Enter a number integer: "))

        print(f"{num1} + {num2} = {num1 + num2}")
        break
    except ValueError:
        print("Invalid input! Please input an integer")
