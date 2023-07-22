#5) Write a function called "calculate_power" that takes two numbers as arguments, a base and an
# exponent, and returns the result of raising the base to the exponent.

import math
def calculate_power(b,e):
    power=math.pow(b,e)
    print(power)
base=int(input("Enter base number:"))
exp=int(input("Enter exponent:"))
print("{} raised to {} :".format(base,exp))
calculate_power(base,exp)