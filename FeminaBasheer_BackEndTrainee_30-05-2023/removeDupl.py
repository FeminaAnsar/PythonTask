#3. Write a program to remove duplicates in a string.

s=""
st=input("Enter a string:")
r=len(st)
for i in range(r):
    c=st[i]
    if c not in s:
        s+=c
print("After removing duplicates:",s)