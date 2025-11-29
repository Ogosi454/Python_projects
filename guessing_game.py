# This is a guessing game where the user has to guess a number between 1 and 10 to come out of the loop
#

# Input from the user
num = int(input("Enter a number: "))

# The correct number
correct_num = 9

while num != 9:
    if num != 9:
        print("Ha ha ha! Muggle, you're stack in my loop. Try again.")

        num = int(input("Enter a number: "))

else:
    print("Congratulations Muggle, You've got the number.")
