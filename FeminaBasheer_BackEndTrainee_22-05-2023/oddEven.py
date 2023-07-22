#3.Python program to check the number taken as an input is even or odd,print invalid input if user enters anything other than  integers
while True:
    try:
        num=int(input("Enter a number:"))
    except ValueError:
        print("Invalid input!!!")
        continue
    else:
        break
if num%2==0:
    print(num,"is Even number")
else:
    print(num,"is Odd number")


