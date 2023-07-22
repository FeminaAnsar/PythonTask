#2 Write a Python program to sort a list of dictionaries using Lambda

studList=[{"Name":"Meera","age":18},{"Name":"Ann","age":17},{"Name":"Arun","age":20},{"Name":"Ziya","age":19},
          {"Name":"Rahul","age":21},{"Name":"Niyas","age":16},{"Name":"Maya","age":18}]
print("List before sorting :\n",studList)
print("List after sorting by age and name:\n",)
print(sorted(studList,key=lambda x:(x['age'],x['Name'])))