# This program prints the fibonacci sequence upto nth term
#
n = int(input("Enter the number of terms in Fibonacci sequence: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 1

