#Write a Python program that take a password as user input and returns True if the password meets the
#following criteria, and False with error message otherwise:

	# 1. The password must be at least 8 characters long.
	# 2. The password must contain at least one uppercase letter.
	# 3. The password must contain at least one lowercase letter.
	# 4. The password must contain at least one digit.
	# 5. The password must contain at least one special character (such as "!@#$%^&*()_-+=").

pd=input("Enter password:")
sp="!@#$%^&*()_-+="
l,u,d,s=0,0,0,0
if len(pd)>=8:
    for i in pd:
        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            d += 1
        if i in sp:
            s += 1
if (l>=1 and u>=1 and s>=1 and d>=1):
    print("Valid Password")
else:
    print("Invalid password")

