#1) Write a function called "find_longest_word" that takes a sentence as a string and returns the longest
# word in the sentence. The function should ignore punctuation and consider only alphabetic characters.

import string
def find_longest_word(s):
    s=s.translate(str.maketrans('','',string.punctuation))
    s=s.split()
    print(max(s,key=len))
new_str=input("Enter a string:")
print("\nLongest word:")
find_longest_word(new_str)