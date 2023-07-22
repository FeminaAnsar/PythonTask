#3. Write a program to make the string after the first occurrence of ',' and the string after the last
# occurrence of ',' in the string "Hello, Good Morning, have a great day".
st="Hello, Good Morning, have a great day"
new_st=st.split(",")

print("New string:",new_st[1]+new_st[-1])
