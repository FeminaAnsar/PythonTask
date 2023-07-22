#10    Find the sum of all odd numbers between the range given by user using while loop

l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
sum=0
while(l<=u):
    if l%2!=0:
        sum=sum+l
    l=l+1
print("Sum of odd numbers in the given range:",sum)
