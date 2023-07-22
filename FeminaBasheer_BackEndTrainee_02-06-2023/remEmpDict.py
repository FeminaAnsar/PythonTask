#Q6: Write a Python program to remove empty dictionaries from a list.

dict1=[{'a':12},{},{'b':15,'c':80},{},{'d':42,'e':25},{}]
print("Given List:",dict1)
newDict=list(filter(None, dict1))
print("Remove empty dictionaries from list:",newDict)