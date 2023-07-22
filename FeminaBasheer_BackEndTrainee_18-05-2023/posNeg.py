#3) take a number as user input, print positive if it's greater than zero, negative if it is less than zero, zero if it is zero
num=int(input("Enter a number:"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
elif num==0:
    print("Number is zero")