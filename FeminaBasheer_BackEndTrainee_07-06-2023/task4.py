# 4) Create a class Employee with name and id, salary attributes.
# The salary has to be calculated and should be initialized to zero.
# Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You can give no of hours to the
# method as an argument.
#
# Now create a child class ParttimeEmployee by inheriting the Employee class, and by using method overriding (create salary
# calculation method in this class also with the same name)
# get the salary of part time employee by multiplyig no of hours worked by 150.
# Also implement '+' operator overloading using __add__ to find the total expense of paying salaries to employees(Find the total
# salary of all the created employees and  parttime employees use __radd__ and implement chained addition).
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.salary=0
    def calcSalary(self,no_of_hours):
        self.salary=self.salary + (no_of_hours*200)
        print(f"--------Employee-------- \nName :{self.name}\nId :{self.id}\nSalary :{self.salary}")

    def __add__(self, other):
        return  self.salary+other.salary

    def __radd__(self, other):
        return  self.salary+other

class ParttimeEmployee(Employee):
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.salary=0
    def calcSalary(self,no_of_hours):
        self.salary= self.salary +(no_of_hours*150)
        print(f"--------Part_time_employee--------\nName :{self.name}\nId :{self.id}\nSalary :{self.salary}")

obj1=Employee("Ann","Id1")
obj1.calcSalary(1)

obj2=Employee("Niya","Id2")
obj2.calcSalary(1)

obj3=ParttimeEmployee("Ankitha","Id3")
obj3.calcSalary(1)

obj4=ParttimeEmployee("Salim","Id4")
obj4.calcSalary(1)
print("==================================================")
total=obj1 + obj2 + obj4 +obj3
print("Total Expense of paying salaries:",total)
