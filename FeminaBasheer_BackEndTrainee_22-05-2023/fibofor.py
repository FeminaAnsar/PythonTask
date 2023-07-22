#11   Print first 10 fibonacci numbers using 'for'  loops

n=10
n1,n2=0,1
print("First 10 Fibonacci Series using for loop:")
for i in range(0,n):
    if(i<=1):
        fibo=i
    else:
        fibo=n1+n2
        n1=n2
        n2=fibo
    print(fibo,end=' ')
