#simple log in system

username = input("Enter your username: ")
password = input("Enter your password: ")

correct_username = 'harry'
correct_password = 'Harry254'

if username == correct_username and password == correct_password:
    print("Log in successfull!")

else:
    print("Incorrect username or password! Please try again.")
 

