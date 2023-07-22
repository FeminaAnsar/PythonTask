# 3) Create a program that calculates the area and circumference of a circle. Prompt the user to
# enter the radius of the circle, and use the appropriate operators and conditional statements to
# calculate and display the area and circumference.

PI=3.14
r=float(input("Enter radius of circle:"))
if r!=0:
    a=PI*r*r
    c=PI*2*r
    print("Radius of circle:", r, "\nCircumference:","%.2f" %c, "\nArea:", "%.2f" %a)
else:
    print("Radius is 0!!!Enter radius greater than 0 !")

