try:

    my_age = int(input("Please enter your age: "))

    if my_age < 13:
        if my_age < 1:
            print("That is an invalid age! Please input a valid age.")
        else:
            print("You are a child.")

    elif my_age < 20:
        print ("You are a teenager.")

    elif my_age < 59:
        print ("You are an adult.")

    elif my_age > 60:
        if my_age > 130:
            print("Invalid input! Please input a realistic human age.")

    else:
        print("Invalid input! Please enter only numbers.")


except ValueError:
    print("Invalid input! Please enter a numeric value.")
