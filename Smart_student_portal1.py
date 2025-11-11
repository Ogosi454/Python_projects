# 🎓 Smart Student Portal
print("===== Welcome to Smart Student Portal =====")

# Step 1: Login Section
stored_username = "student"
stored_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("\nLogin successful! Welcome to your portal.")
    
    # Step 2: Student Information
    name = input("\nEnter your full name: ")
    course = input("Enter your course name: ")

    # Step 3: Marks and Grading
    marks = float(input("Enter your marks (0-100): "))

    if marks >= 80:
        grade = "A"
        remark = "Excellent performance! Keep soaring high."
    elif marks >= 70:
        grade = "B"
        remark = "Very good! You’re on the right track."
    elif marks >= 60:
        grade = "C"
        remark = "Good work! Aim a bit higher next time."
    elif marks >= 50:
        grade = "D"
        remark = "Fair effort. You can do better with more practice."
    else:
        grade = "Fail"
        remark = "Needs improvement. Don’t give up, keep pushing."

    # Step 4: Display Student Report
    print("\n===== STUDENT REPORT =====")
    print(f"Name       : {name}")
    print(f"Course     : {course}")
    print(f"Marks      : {marks}")
    print(f"Grade      : {grade}")
    print(f"Feedback   : {remark}")
    print("============================")

    # Step 5: Bonus – Temperature Conversion (fun extra)
    choice = input("\nWould you like to convert today’s temperature from °C to °F? (yes/no): ").lower()
    if choice == "yes":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")

    print("\nThank you for using the Smart Student Portal! 🌟")

else:
    print("\nAccess Denied! Invalid username or password.")
