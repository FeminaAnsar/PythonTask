#3.Write a python program to sort dictionary by values (Ascending/ Descending)
newdict={"abc":12,"mnb":9,"hjk":22,"lkj":90,"poi":4,"ert":19,"dfg":2,"asd":89}
tempdict=sorted((value,key) for (key,value) in newdict.items())
sortdict=dict([(k,v) for v,k in tempdict])
print(sortdict)