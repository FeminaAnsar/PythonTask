#5  A lambda function that checks if a number is even.

num=int(input("Enter a number:"))
even_number=lambda:"Even number" if num%2==0 else "Odd number"
print(even_number())