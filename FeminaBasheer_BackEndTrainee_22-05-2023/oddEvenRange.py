#5    Python program to print all even/odd numbers in the range given by user
l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
evenlst=list()
oddlst=list()
for i in range(l,u):
    if i%2==0:
        evenlst.append(i)
    else:
        oddlst.append(i)
print("Even numbers:",evenlst)
print("Odd numbers:",oddlst)
