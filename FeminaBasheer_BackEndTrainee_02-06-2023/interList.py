#Q5: Write a Python program to find the intersection of two lists.

lst1=[7,8,120,25,44,20,27,56,32,12]
lst2=[12,90,78,56,25,44,56,11,98,100]
print("List 1: {}\nList 2: {}".format(lst1,lst2))
lst3 = [x for x in lst1 if x in lst2]
print("Intersection of 2 lists:",lst3)