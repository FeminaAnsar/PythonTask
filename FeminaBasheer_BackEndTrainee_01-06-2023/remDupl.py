# Q1: write a program to remove duplicate elements from a list in Python while preserving the original order?
# hint: You can use a combination of a list comprehension and a conditional check to remove

lst=["abc","cvf","ghy",12,13,14,"ghy",12,34,78,13]
print("Given List:",lst)
new_lst=[]
[new_lst.append(i) for i in lst if i not in new_lst]
print("List after removing duplicates:",new_lst)
