first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
operator = input ("Enter your operator: ")

if operator == "+":
    answer = first_number + second_number

elif operator == "-":
    answer = first_number - second_number

elif operator == "*":
    answer = first_number * second_number

elif operator == "/":
    answer = first_number / second_number

else:
    print ("Invalid operator! Please input the valid operator!")

print("your answer is:", answer)
