        # o
		# 1 1
		# 2 2 2
		# 3 3 3 3

n=int(input("Enter number of rows:"))
num = 0
for i in range(0, n):
    for j in range(0, i + 1):
         print(num, end=" ")
    num+=1
    print("\r")