#4. Write a Python program to get a string from a given string where all the repeated character replaced
# with "_" except the first occurrences of character itself (eg: "hello" -> "hel_o").

s=""
st=input("Enter a string:")
r=len(st)
for i in range(r):
    c=st[i]
    if c not in s:
        s+=c
    else:
        s+="_"
print("Repeated character replaced by _:",s)
