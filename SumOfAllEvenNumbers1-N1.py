N = int(input("Enter a number: "))

total = 0

i = 1

while i <= N:
    if i % 2 ==0:
        total +=i
    i +=1

print(f"Sum of even numbers = {total}")
