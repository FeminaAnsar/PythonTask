#4. Write a Python program to count the number of occurrences of a specific character in a given sentence. Take both sentence and specific character from the user.

str=input("Enter a string : ")
s=input("Enter a character : ")
c=0
for i in str:
    if i == s:
        c+=1
print("Number of occurrences of ",s,":",c)