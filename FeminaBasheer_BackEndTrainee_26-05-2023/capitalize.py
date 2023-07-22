#4) Develop a function called "capitalize_words" that takes a sentence as a string and returns the sentence
# with each word capitalized.

import string
def capitalize_words(str):
    cap_str=string.capwords(str)
    print("Capitalized string:",cap_str)
new_str=input("Enter a string:")
capitalize_words(new_str)

