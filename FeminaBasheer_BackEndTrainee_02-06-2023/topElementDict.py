#Q3: Write a Python program to find the top N elements with the highest values in a dictionary.

dict1={'a':12,'b':15,'c':80,'d':42,'e':25,'f':102,'g':150,'h':88,'i':47,'j':23}
print("Given Dictionary:",dict1)
n=int(input("Enter a number(1-10):"))
print("Top {} elements with the highest values:".format(n))
print("Keys:  Values:")
x=list(dict1.values())
d=dict()
x.sort(reverse=True)
x=x[:n]
for i in x:
    for j in dict1.keys():
        if(dict1[j]==i):
            print(str(j)+"  :   "+str(dict1[j]))
