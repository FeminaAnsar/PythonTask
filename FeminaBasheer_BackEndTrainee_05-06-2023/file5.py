#write a python program to read a file line by line and store it into a list

f = open("text1.txt","r",encoding="utf8")
lst = [l.rstrip() for l in f]
print(lst)
f.close()
