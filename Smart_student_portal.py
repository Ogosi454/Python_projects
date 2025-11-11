# Goals of this program
# 1. Allow a student to log in 
# 2. Takes there name and course
# 3. Accept their marks
# 4. Calculate their grade and give feedback
# 5. Optionally converts temperature (Extra feature)
# 6. Display a clean, professional student report


# PROGRAM FLOW

# Welcome message   
print("Welcome to Smart Student Portal")


# Log in Section
stored_username = 'harry'
stored_password = '65Y3e203'

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == stored_username:
    print("You have successfully logged in. Proceed")

   
    # Student Information
    full_name = input("Please enter your full name: ")
    course_name = input("Please enter your course name: ")


    # Marks and grade calculation
    marks = float(input("Enter your marks (0 - 100): "))

    if marks >= 80:
        if marks > 100:
            print("Invalid marks! Marks cannot be more than 100. Enter a valid marks.")
        else:
            grade = "A"
            remark = "Excellent performance! Keep soaring up"

    elif marks >= 70:
        grade = "B"
        remark = "Very good! You are on the right track."

    elif marks >= 60:
        grade = "C"
        remark = "Good work! Aim a bit higher next time."

    elif marks > 50:
        grade = "D"
        remark = "Fair effort! You can do better with more practice"

    else:
        if marks < 0:
            print("Invalid input. Marks cannot be less than 0. Please input a valid marks.")
        else:
            grade = "Fail"
            remark = "Needs improvement! Dont give up, keep pushing."



    #Student Report Output
    print("STUDENT REPORT")
    print(f"Name: {full_name}")
    print(f"Course: {course_name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")


    #Bonus (Optional feature) - temperature converter
    yes_or_no = input(f"Hello {full_name}, would you like to convert the current temperature of your location from celcius to Fahrenheit: ").lower()

    if yes_or_no == 'yes':
        temperature = float(input("Input temperature in celcius: "))
        F = (temperature * 9/5) + 32 
        print(f"The temperatuer is {F}F")

    else:
        print("Thank you for your time.")


    #Final remark
    print("Thank you for using Smart Student Portal!")


else:
    print("Access denied! Invalid username or password")
