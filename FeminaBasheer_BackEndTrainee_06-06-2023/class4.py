#4) Extend the above solution again and add another instance method called 'as_dict'. The method should return a dictionary
# with the data of the student. It should contain 'name', 'score', 'grade', 'ehs_status' keys and their respective values.
#Create Student 2 objects and call each of its methods.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade=self.calcGrade()
        self.ehs=self.get_ehs()
        self.as_d=self.as_dict()
    def calcGrade(self):
        if self.score >= 90 and self.score <= 100:
            return "A+"
        elif self.score >= 80 and self.score < 90:
            return "A"
        elif self.score >=70 and self.score < 80:
            return "B+"
        elif self.score >=60 and self.score < 70:
            return "B"
        elif self.score >=50 and self.score < 60:
            return "C+"
        elif self.score >=40 and self.score<50:
            return "C"
        elif self.score < 40:
            return "Failed"
        elif self.score > 100:
            return "Invalid"
    def get_ehs(self):
        if self.score>40:
            return True
        else:
            return False
    def as_dict(self):
        d={"Name":self.name,"Score":self.score,"Grade":self.calcGrade(),"EHS":self.ehs}
        print("Student Dictionary:",d)
        print()
    def display(self):
        print("Name:{}\tScore:{}\tGrade:{}\tEligible for higher studies:{}".format(self.name,self.score,self.calcGrade(),self.get_ehs()))

student1=Student("Niya",95)
student1.display()

student2=Student("Ann",34)
student2.display()