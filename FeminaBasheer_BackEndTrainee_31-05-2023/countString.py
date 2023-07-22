#1. Write a program to find the number of vowels, consonents, digits and white space characters in a string.

st=input("Enter a string:")
v,c,d,w,s=0,0,0,0,0
for i in range(0,len(st)):
    ch=st[i]
    if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
        ch=ch.lower()
        if ch in "aeiou":
            v+=1
        else:
            c+=1
    elif (ch>='0' and ch<='9'):
        d+=1
    elif(ch==" "):
        w+=1
    else:
        s+=1
print("Vowels:{}\nConsonents:{}\nDigits:{}\nWhite space:{}\nSpecial character:{}".format(v,c,d,w,s))
