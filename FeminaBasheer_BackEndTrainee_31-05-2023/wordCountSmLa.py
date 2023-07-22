#6. Write a Python program to find smallest and largest word in a given string.

st=input("Enter the String:")
print("\nLargest Word(s): ")
print(*[i for i in st.split() if len(i) == max([len(s) for s in st.split()])])
print("\nSmallest Word(s): ")
print(*[i for i in st.split() if len(i) == min([len(s) for s in st.split()])])


