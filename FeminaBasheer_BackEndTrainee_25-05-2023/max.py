#max()
num_lst=[]
n=int(input("Enter number of elements in list:"))
print("Enter list elements:")
for i in range(n):
    num=int(input())
    num_lst.append(num)
print("Largest element in list:",max(num_lst))