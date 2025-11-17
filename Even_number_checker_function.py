def check_even_number(numbers):
    
    if numbers % 2 == 0:
        print("This is an even number")

    else:
        print("This is not even number")

check_even_number(24)





def is_even(number):
    # Function to check if a number is even
    return number % 2 == 0


def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    # Check and display the result
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")


# Run the program
if __name__ == "__main__":
    main()

