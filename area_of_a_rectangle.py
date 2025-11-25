# This program calculates the area of a rectangle by asking the user length and width
#
while True:
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        area = length * width

        print("The area of the rectangle is:")
        print(f"Area = {length} x {width}")
        print(f"Area = {area}")
        break

    except ValueError:
        print("Input a number. Leters cannot be measurements")
