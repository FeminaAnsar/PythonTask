#1. Write a python program which take user's first and last name and return user email like
# "first_name.last_name@beinex.com"

first=input("Enter first name:")
last=input("Enter last name:")
user_email=("{}.{}@beinex.com".format(first,last))
print("User email:",user_email)
