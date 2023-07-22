#11   Print first 10 fibonacci numbers using  'while' loops

n1,n2=0,1
c=0
print("First 10 Fibonacci series using while loop:")
while c<10:
    print(n1,end=' ')
    fibo=n1+n2
    n1=n2
    n2=fibo
    c+=1

