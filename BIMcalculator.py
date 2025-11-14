#BIM calculator

weight = float(input("Enter your weight in KGs: "))
height = float(input("Enter your height in Ms: "))

BIM = weight / (height * height)

if BIM < 18.5:
    print(f"{BIM} - Underweight")

elif BIM < 24.5:
    print(f"{BIM} - Normal weight")

elif BIM < 29.9:
    print(f"{BIM} - Overweight")

else:
    print(f"{BIM} - Obese")
