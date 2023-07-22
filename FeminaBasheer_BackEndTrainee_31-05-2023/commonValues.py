#7. Write a Python program find the common values that appear in two given strings.

st1=input("Enter first string:")
st2=input("Enter second string:")
newst1=set(st1)
newst2=set(st2)
common=[i for i in newst1 if i in newst2]
print("\nCommon Values :",common)
