#1. Write a Python program to read an entire text file.

f = open("text1.txt", "r",encoding="utf8")
c = f.read()
print(c)
f.close()
