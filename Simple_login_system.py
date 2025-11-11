username = input("Enter your username: ")
password = input("Enter your password: ")

user = 'admin'
pas = '12345'

if username == user and password == pas:
    print("Login successful!")

else:
    print("Access denied!")
