#6) Develop a function called "count_vowels" that takes a string as an argument and returns the number of
# vowels (a, e, i, o, u) in the string.

def count_vowels(str):
    v=['a','e','i','o','u']
    count=0
    str=str.lower()
    for i in str:
        if i in v:
            count+=1
    print("Number of vowels :",count)
new_str=input("Enter a string:")
count_vowels(new_str)


