#8    Find the factorial of a number taken as input using while loop

num=int(input("Enter a number:"))
fact=1
while num>=1:
    fact=fact*num
    num=num-1
print("Factorial :",fact)