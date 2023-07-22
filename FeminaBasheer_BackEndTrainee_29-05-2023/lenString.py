#1. Write a Python program to calculate the length of a string(user input) without using len() method.

s=input("Enter a string:")
c=0
for i in s:
    c+=1
print("Length of string:",c)