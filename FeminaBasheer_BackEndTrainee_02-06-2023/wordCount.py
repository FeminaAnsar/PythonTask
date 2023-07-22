#Q7: Write a Python program to count the number of occurrences of each word in a given sentence.

str=input("Enter a string:")
c=dict()
words=str.split()
for word in words:
    if word in c:
        c[word] += 1
    else:
        c[word] = 1
print("Number of occurrences of each word:\n",c)
