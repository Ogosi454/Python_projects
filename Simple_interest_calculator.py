
# Getting the principle amount, rate of interest, and time from the user.
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the number of years: "))

#Calculating the simple interest
simple_interest = principle * rate * time 

#Displaying the result
print("The simple interest is:", simple_interest)
