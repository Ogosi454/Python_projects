def max_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


# Main program
print("Enter three numbers:")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maximum = max_of_three(num1, num2, num3)

print("The maximum number is:", maximum)
