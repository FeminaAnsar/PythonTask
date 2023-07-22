#5. Write a Python program to determine if a given sentence(user input) contains any numbers.
# If any numbers are present, remove them from the sentence.

str=input("Enter a string : ")
c=0
for i in str:
    if i.isdigit():
        c+=1
if c>0:
    print("Sentence contains numbers\n")
    fin = "".join(filter(lambda x: not x.isdigit(), str))
    print("String after removing numbers:", fin)
else:
    print("Sentence doesn't contain numbers")
