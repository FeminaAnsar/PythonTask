#4    Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on...
#     print failed if the score is below 50, if score > 100 print invalid
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