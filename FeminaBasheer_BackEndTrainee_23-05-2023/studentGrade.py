# 2) Develop a program that takes a user's grade as input and provides a corresponding letter grade. ' \
# 'Use conditional statements to check different ranges of grades and assign the appropriate letter grade ' \
# '(e.g., A, B, C) based on the input.

name=input("Enter name of the student:")
score=int(input("Enter score:"))
if score>=90 and score<=100:
    grade="A+"
elif score>=80 and score<90:
    grade="A"
elif score>=70 and score<80:
    grade="B+"
elif score>=60 and score<70:
    grade="B"
elif score>=50 and score<60:
    grade="C+"
elif score<50:
    grade="Fail"
elif score>100:
    grade="Invalid"
print("Name:",name,"\nScore:",score,"\nGrade:",grade)
