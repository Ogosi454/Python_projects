
while int != True:
    number = int(input("Enter a number: "))

    if number > 0:
        print(f"{number} is a positive number")

    elif number < 0:
        print(f"{number} is a negative number")

    elif number == 0:
        print(f"This is {number}")

    else:
        if number != int:
            print(f"{number} is not an integer. Please input the integer number")

else:
    print("Input a valid number")
