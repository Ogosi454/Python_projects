# This program is to create a student portal that:
# 1. Authenticate the user through log in 
# 2. Collect student and course details
# 3. Accept marks for multiple subjects
# 4. Calculate the grade and remark for each subject
# 5. Compute total and average marks
# 6. Display a neat report card
# 7. (Bonus) Convert temperature from celcius to Fahrenheit


# Log in section
stored_username = "Harry254"
stored_password = "65Y3e203"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Successfully logged in!")

    
    # Student information
    name = input("Enter your full name: ")
    course = input("Enter your course name: ")
    number_of_subjects = int(input("Enter the number of subjects: "))


    # Collect subject marks
       

else:
    print("Access denied! Incorrect username or password!")


