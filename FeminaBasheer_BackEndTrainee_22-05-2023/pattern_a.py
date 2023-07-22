#             *
#            * *
#           * * *
#          * * * *
r=int(input("Enter number of rows:"))
n = r - 1
for i in range(0, r):
    for j in range(0, n):
        print(end=" ")
    n = n - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")