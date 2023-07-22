#Q2: Write a Python program to merge two dictionaries and combine the values of common keys.

dict1={'a':12,'b':15,'c':80,'d':42,'e':25}
dict2={'z':12,'y':15,'a':80,'c':42,'w':25}
dict3={}
dict3.update(dict1)
dict3.update(dict2)
for i,j in dict1.items():
    for x,y in dict2.items():
        if i==x:
            dict3[i]=[j,y]
print(dict3)