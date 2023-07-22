#2) Write a Python program that takes two numbers as input from the user and displays their sum, difference, product, and quotient using appropriate operators.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Select operator (+,-,*,/) :")
if op=='+':
    print("Sum of",num1,"and",num2,":",num1+num2)
elif op == '-':
    print("Difference of", num1, "and", num2, ":", num1-num2)
elif op=='*':
    print("Product of",num1,"and",num2,":",num1*num2)
elif op == '/':
    print("Quotient of", num1, "and", num2, ":", num1/num2)
else:
    print("Invalid operator!")


