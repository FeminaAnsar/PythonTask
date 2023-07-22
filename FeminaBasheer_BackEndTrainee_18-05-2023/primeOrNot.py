#4)get a number as input, if it is a prime number print 'this is a prime number', else print ' this is not a prime number'

num=int(input("Enter a number:"))

t=0
if num>1:
    for i in range(2,num):
        if num%i==0:
            t+=1
if num<2:
    print("Enter a number greater than 1")
elif t==0:
    print("This is a prime number")
else:
    print("This is not a prime number")