# This program prints all even numbers from 1-50, their sum and counts
# It will also report how many even numbers and how many odd numbers are in the range.
#

total = 0
even_count = 0
odd_count = 0

for num in range(1, 51):
    if num % 2 == 0:
        print(f"{num} is even number")
        total += num
        even_count += 1
    else:
        odd_count += 1
        
print("Sum of even numbers from 1 to 50:", total)
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
