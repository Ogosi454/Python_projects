try:
    grade = float(input("Enter your grade (0 - 100): "))

    if grade < 50:
        if grade < 0:
            print("Invalid input! Grade cannot be less than 0. Please input a valid grade.")
        else:
            print(f"{grade}% is a fail. Please retake the test.")

    elif grade < 60:
        print(f"{grade}% is D. Try next time to get a higher grade.")

    elif grade < 70:
        print(f"{grade}% is C. Try next time to get a higher grade.")

    elif grade < 80:
        print(f"{grade}% is B. You have tried, keep up the good work.")

    else:
        if grade > 100:
            print(f"{grade} is invalid, marks cannot be greater than 100, Please input a valid marks.")
        else:
            print(f"{grade}% is A. Congratulations!!! You have done a greate job. Keep it up for the more opportunities.")

except ValueError:
    print("Invalid input! Please enter a valid number between 0 - 100 so that I can give you your grade.")
