#3) Extend the above solution again and add an instance method named 'get_ehs' (short for eligible for higher studies) It should
# return a boolean. Return True if score is 40 and above.Modify the 'display' method to include this EHS status also while printing.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade=self.calcGrade()
        self.ehs=self.get_ehs()
    def calcGrade(self):
        if self.score >= 90 and self.score < 101:
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

    def display(self):
        print("Name:{}\tScore:{}\tGrade:{}\tEligible for higher studies:{}".format(self.name,self.score,self.calcGrade(),self.get_ehs()))

student1=Student("Niya",95)
student1.display()

student2=Student("Ann",34)
student2.display()