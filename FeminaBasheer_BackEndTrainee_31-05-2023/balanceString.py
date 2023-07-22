#10. Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced
# if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

def balanceString(str1,str2):
    t=0
    for ch in str1:
        if ch in str2:
            continue
        else:
            t = 1
    if t==0:
        print("Strings are balanced")
    else:
        print("Strings are unbalanced")
s1=input("Enter first string:")
s2=input("Enter second string:")
balanceString(s1,s2)
