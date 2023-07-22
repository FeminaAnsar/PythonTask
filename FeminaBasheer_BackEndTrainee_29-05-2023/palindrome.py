#2. Write a Python program to check if a given string(user input) is a palindrome.

s=input("Enter a string to check palindrome: ")
c=0
rev=s[::-1]
if rev==s:
    print("Palindrome")
else:
    print("Not palindrome")
