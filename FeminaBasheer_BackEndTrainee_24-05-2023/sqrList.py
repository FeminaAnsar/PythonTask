# 1 Write a Python function called square_numbers that takes a list of numbers as input and returns
# a new list containing the square of each number.

def square_numbers(lst):
    sql_lst=list(map(lambda num:num**2,lst))
    print("List of squares:",sql_lst)

num_lst=[]
n=int(input("Enter number of elements in list:"))
print("Enter list elements:")
for i in range(n):
    num=int(input())
    num_lst.append(num)
print("Number list:",num_lst)
square_numbers(num_lst)




