password = input("Enter your password: ")

if len(password) < 8:
    print("This is a weak password. Too short. Enter another password.")

elif password.isalpha() or password.isdigit():
    print("This is a medium stength password.")

else:
    print("This is a strong password.")
