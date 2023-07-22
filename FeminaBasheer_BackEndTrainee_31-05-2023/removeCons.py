#2. Write a program to make a new string with all the consonents deleted from the string
# "Python's simplicity and readability make it a popular choice for beginners in programming.".

st="Python's simplicity and readability make it a popular choice for beginners in programming."
print("Given string:",st)
new_st=""
for i in range(0,len(st)):
    ch=st[i]
    if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
        ch=ch.lower()
        if (ch in "aeiou"):
            new_st+=ch
print("New string removing consonants:",new_st)
