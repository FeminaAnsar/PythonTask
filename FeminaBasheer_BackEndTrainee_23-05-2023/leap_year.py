# 5) Write a program that determines if a given year is a leap year or not using a nested if-else
# statement. Prompt the user to enter a year, and check if it is divisible by 4. If it is, check if it
# is divisible by 100 and not divisible by 400. Display an appropriate message indicating whether it is a
# leap year or not.
year=int(input("Enter the year to check leapyear:"))
if year%4==0:
    if year%100==0:
        if year % 400 == 0:
            print(year," is a leap year")
        else:
            print(year," is not a leap year")
    else:
        print(year," is a leap year")
else:
    print(year," is not a leap year")
