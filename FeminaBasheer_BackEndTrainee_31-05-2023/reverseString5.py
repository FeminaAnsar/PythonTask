#5. Write a Python function to reverses a string if its length is a multiple of 5.

def reverseString(st):
    if len(st)%5==0:
        print("Reversed string:",st[::-1])
    else:
        print("String length is not a multiple of 5!")
str=input("Enter a string:")
reverseString(str)

