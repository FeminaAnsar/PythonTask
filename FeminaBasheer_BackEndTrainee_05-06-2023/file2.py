#2. Write a Python program to read first n lines of a file.

n = int(input("Enter number of lines to read : "))
f = open("text1.txt","r",encoding="utf8")
for i in range(n):
	print(f.readline())