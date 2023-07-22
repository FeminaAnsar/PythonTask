#sorted()

num_lst=[]
n=int(input("Enter number of elements in list:"))
print("Enter list elements:")
for i in range(n):
    num=int(input())
    num_lst.append(num)
print("List before sorting:",num_lst)
print("List after sorting in ascending order:",sorted(num_lst))
print("List after sorting in descending order:",sorted(num_lst,reverse=True))