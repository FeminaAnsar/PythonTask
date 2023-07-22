        # o
		# 1 2
		# 3 4 5
		# 6 7 8 9

n=int(input("Enter number of rows:"))
num = 0
for i in range(0, n):
    for j in range(0, i + 1):
         print(num, end=" ")
         num = num + 1
    print("\r")