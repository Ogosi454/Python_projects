# This progarm checks whether the number is positive, negative or zero
#

while True:
    try:
        raw = input("Enter a number (press Enter to quit): ").strip()

        # Exit the loop when the user presses Enter without any input
        if raw == "":
            print("Exiting — goodbye!")
            break

        num = float(raw)

        if num < 0:
            print(f"{num} is a negative number.")

        elif num > 0:
            print(f"{num} is a positive number.")

        elif num == 0:
            print("You've entered zero(0).")

        else:
            break

    except ValueError:
        print("Input a number not a digit")
