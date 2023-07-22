#3. Write a Python program to append text to a file and display the text.

f = open("text1.txt","a",encoding="utf8")
str = input("Enter text to append in text1.txt : ",)
f.write(str)
f = open("text1.txt","r",encoding="utf8")
print(f.read())
f.close()