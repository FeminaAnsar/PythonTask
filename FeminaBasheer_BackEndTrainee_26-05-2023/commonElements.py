#3) Create a function called "find_common_elements" that takes two lists as arguments and returns a
# new list containing the common elements between the two lists.

def find_common_elements(lst1,lst2):
    common=[i for i in lst1 if i in lst2]
    print("\nCommon Elements :",common)
a=[2,3,1,4,5,11,22,31,98]
b=[9,1,2,7,0,98,34,67,89]
print("Lists are:\n",a,"\n",b)
find_common_elements(a,b)

