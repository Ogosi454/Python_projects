num = int(input("Enter a number: "))

total = 0
for i in range(1, num):
    if i % 2 == 0:
        total += i

print (f"The sum of even numbers = ", total)

