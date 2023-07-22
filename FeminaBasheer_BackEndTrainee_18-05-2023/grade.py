#6) get name and score of a student, print A+ if the score is 90-100, print A if the score is 80-89,.... print fail if less than 50 and if greater than 100 print invalid
name=input("Enter name of the student:")
score=int(input("Enter score:"))
if score>89 and score<101:
    grade="A+"
elif score>79 and score<90:
    grade="A"
elif score>69 and score<80:
    grade="B+"
elif score>59 and score<70:
    grade="B"
elif score>49 and score<60:
    grade="C+"
elif score<50:
    grade="Fail"
elif score>100:
    grade="Invalid"
print("Name:",name,"\nScore:",score,"\nGrade:",grade)