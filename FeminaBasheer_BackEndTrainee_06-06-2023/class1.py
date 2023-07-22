#1) Create a class named Student with name, score as instance attributes. Assign values to both of these attributes using
# a constructor.Create 2 Student objects. And also define a method called 'display' in the Student class - which, when called
# should print the name and score of the student.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def display(self):
        print("Name:{}\tScore:{}".format(self.name,self.score))

student1=Student("Niya",95)
student2=Student("Ann",75)

student1.display()
student2.display()

