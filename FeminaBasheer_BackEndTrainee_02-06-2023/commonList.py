#Q4: Write a Python program to check if two lists have any common elements.
lst1=[7,8,120,25,44,20,27,56,32,12]
lst2=[12,90,78,56,25,44,56,11,98,100]
print("List 1: {}\nList 2: {}".format(lst1,lst2))
slst1=set(lst1)
slst2=set(lst2)
if(slst1 & slst2):
    print("Common list:",list(slst1 & slst2))
else:
    print("No common elements")
