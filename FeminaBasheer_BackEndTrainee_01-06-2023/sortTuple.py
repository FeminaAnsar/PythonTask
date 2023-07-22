# Q5: write a program to sort a list of tuples based on multiple keys in Python?

tuples=[(105,'Anu'),(104,'Cereena'),(130,'Nila'),(104,'Femina')]
new_list= sorted(tuples, key=lambda x: (x[0], x[1]))
print(new_list)