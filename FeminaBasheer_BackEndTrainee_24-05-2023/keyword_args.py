# 3 Write a Python function called format_info that takes the following information as keyword arguments:
# name, age, city, country. The function should format the information into a string and return it.

def format_info(**kwargs):
    for key,value in kwargs.items():
        print("{} is {}\n".format(key,value))

print(format_info(Name="Ann",Age="21",City="Kochi",Country="India"))

