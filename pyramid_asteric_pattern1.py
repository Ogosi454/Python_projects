# This program draw a pyramid pattern with asteric
#

asteric = "*"
space = " "

for i in range(10):
    print(f" {space * -i, asteric * i}")
