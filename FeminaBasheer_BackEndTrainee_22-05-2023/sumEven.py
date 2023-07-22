#9    Find the sum of all even numbers between the range given by user
l=int(input("Enter starting range:"))
u=int(input("Enter ending range:"))
sum=0
for i in range(l,u):
    if i%2==0:
        sum=sum+i
print("Sum of even numbers in the given range:",sum)
