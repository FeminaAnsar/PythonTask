#1  Write a function that inputs a number and prints the multiplication table of that number

def mulTable(num):
    for i in range(1,11):
        print(i, "*", num, "=", i * num)
n=int(input("Enter a number:"))
mulTable(n)