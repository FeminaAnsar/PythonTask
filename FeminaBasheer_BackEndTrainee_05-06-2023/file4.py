#4. Write a Python program to read last n lines of a file.

n = int(input("Enter number of lines to read (from the end): "))
f = open("text1.txt","r",encoding="utf8")
for i in (f.readlines() [-n:]):
            print(i, end ='')