#1) Write a Python program that calculates the area of a rectangle. Prompt the user to enter the length and width of the rectangle, and use the appropriate operators and conditional statements to calculate and display the area.

l=int(input("Enter length:"))
w=int(input("Enter width:"))
if l>w:
    area=l*w
    print("Area :",area)
else:
    print("Enter length greater than width!!!")