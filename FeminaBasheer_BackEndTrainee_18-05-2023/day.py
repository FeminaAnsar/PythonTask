#5) get a day as input, print have a great week ahead, if it is monday, print 'happy weekend' if it is Friday, print 'Be happy' for other days
day=input("Enter a day (Sunday-Friday):")
week_day=day.lower()
if week_day=="monday":
    print("Have a great week ahead")
elif week_day=="friday":
    print("Happy weekend")
else:
    print("Be Happy")