num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter your operator: ")

if operator == "+":
    print (f"Your answer is: {num1 + num2}")

elif operator == "-":
    print (f"Your answer is: {num1 - num2}")

elif operator == "*":
    print (f"Your answer is: {num1 * num2}")

elif operator == "/":
    if num2 != 0:
        print (f"Your answer is: {num1 / num2}")
    else:
        print ("Invalid input! Number cannot be divided by zero!")

else:
    print ("Invalid operator! Please input the valid operators!")
