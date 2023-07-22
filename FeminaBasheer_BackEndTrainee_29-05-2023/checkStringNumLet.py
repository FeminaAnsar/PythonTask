#3. Write a Python program to check if a string(user input) has at least one letter and one number.

s=input("Enter a string : ")
c1=0
c2=0
for i in s:
    if i.isalpha():
        c1=1
    if i.isdigit():
        c2=1
if c1==1 and c2==1:
    print("String contains at least one letter and one number")
else:
    print("String doesn't contain at least one letter and one number")


