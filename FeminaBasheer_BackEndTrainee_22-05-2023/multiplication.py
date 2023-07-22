#6    Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)
num=int(input("Enter a number:"))
n=int(input("Enter end limit:"))
i=1
while i<=n:
    print(i,"*",num,"=",i*num)
    i+=1

