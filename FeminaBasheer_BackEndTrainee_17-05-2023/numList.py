#4.Write a Python program to print the numbers of a specified list after removing even numbers from it.(use list comprehension)
lst = [7,8, 120, 25, 44, 20, 27]
lst=[x for x in lst if x%2!=0]
print(lst)