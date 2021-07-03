# Make a function that receives three values, 'a', 'b' and 'c', which are coeficients of
# a second degree equation and returns the delta value, given by 'b² - 4ac'

import math

print("This program calculates and returns the Delta value of a "
      "second degree equation. Please, follow the instructions: ")

a = int(input("Input the value of 'a' coeficient: "))
b = int(input("Input the value of 'b' coeficient:  "))
c = int(input("Input the value of 'c' coeficient:  "))

delta = ((b*b)-(4*a*c))

print(f"The value of Delta is {delta}")
