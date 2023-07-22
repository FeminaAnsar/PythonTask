#5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.​
newlist= ['abc', 'xyz', 'aba', '1221','4554','ghjg','a']
c=0
for n in newlist:
    if len(n)>1 and n[0]==n[-1]:
        c+=1
print("Number of strings where string length is 2 or more and the first and last character are same : ",c)