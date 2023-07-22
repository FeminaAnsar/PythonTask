#2) Write a function called "reverse_string" that takes a string as an argument and returns the reverse
# of that string. Implement the function using a loop and without using built-in string reversal functions.

def reverse_string(str):
    rev_str=" "
    for i in str:
        rev_str=i+rev_str
    print(rev_str)
new_str=input("Enter a string:")
print("\nReversed string:")
reverse_string(new_str)

