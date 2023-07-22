#4. Write a Python program to count the occurrence of each character in a word.

s=input("Enter a string:")
strDict={}
for i in s:
    if i in strDict:
        strDict[i]+=1
    else:
        strDict[i]=1
print("Occurrence of each character in a word:"+str(strDict))

