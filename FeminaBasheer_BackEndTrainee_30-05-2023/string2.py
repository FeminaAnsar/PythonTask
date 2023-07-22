#2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.

s=input("Enter a string:")
if len(s)>=2:
    print(s[0:2]+s[-2:])
else:
    print("Empty")
