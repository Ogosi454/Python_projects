# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert number to string
    s = str(num)
    # Check if string is same when reversed
    return s == s[::-1]


# Main program
number = input("Enter a number: ")

# Validate that user enters digits only
if not number.isdigit():
    print("Please enter a valid number!")
else:
    number = int(number)
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")
