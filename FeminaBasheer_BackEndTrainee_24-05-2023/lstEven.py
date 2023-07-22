#2 Write a Python function called find_even_numbers that takes a list of numbers as input and returns a
# new list containing only the even numbers from the input list.

def find_even_numbers(lst):
    even_lst=list(filter(lambda num:num%2==0,lst))

    print("List of even numbers:",even_lst)

num_lst=[]
n=int(input("Enter number of elements in list:"))
print("Enter list elements:")
for i in range(n):
    num=int(input())
    num_lst.append(num)
print("Number list:",num_lst)
find_even_numbers(num_lst)