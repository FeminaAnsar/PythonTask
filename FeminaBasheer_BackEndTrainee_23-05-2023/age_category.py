# 4) Write a Python program that takes a user's age as input and determines if they are a child,'
# teenager, adult, or senior citizen. Use conditional statements to check different age ranges and
# display the corresponding category based on the input.

age=int(input("Enter age :"))
if age>0:
    if age<=12:
        print("Child!")
    elif age<=18:
        print("Teenager!")
    elif age<=60:
        print("Adult!")
    elif age<=100:
        print("senior citizen")
else:
    print("Invalid input!")
